import logging
from fastapi import FastAPI, HTTPException, Query
import requests
from dotenv import load_dotenv
import os
from typing import List
from app.constants import TABLES, BASE_API_URL, BASE_URL, WORKSPACE_ID, SOURCE_ID, SOURCE_TABLE

app = FastAPI()
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}


# Create new table
def create_base(project_name: str):
    data = {
        "name": f"{project_name}",
        "workspaceId": f"{WORKSPACE_ID}",
        "tables": TABLES
    }
    url = f'{BASE_API_URL}/meta/bases/'
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        resp = response.json();

        return {
            "base_id": resp.get('id', ''),
            "table_id": resp['tables'][0]['id']
        }
    else:
        logging.error(f"Error fetching records: {response.status_code}")
        return


# Get records from Airtable
def get_records(base_id: str, table_name: str):
    url = f'{BASE_API_URL}/{base_id}/{table_name}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('records', [])
    else:
        logging.error(f"Error fetching records: {response.status_code}")
        return []


# Function to copy records from one base to another using batch processing
def copy_records(dest_base_id: str, dest_table: str):
    records = get_records(SOURCE_ID, SOURCE_TABLE)
    sorted_records = sorted(records, key=lambda x: x['fields'].get('Sort', 0))

    batch_size = 10
    batch = []

    for record in sorted_records:
        batch.append({"fields": record['fields']})

        # Check if batch size limit reached
        if len(batch) == batch_size:
            send_batch(dest_base_id, dest_table, batch)
            batch = []

    # Send any remaining records in the batch
    if batch:
        send_batch(dest_base_id, dest_table, batch)


def send_batch(dest_base_id: str, dest_table: str, batch: List[dict]):
    data = {"records": batch}
    url = f'{BASE_API_URL}/{dest_base_id}/{dest_table}'
    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        logging.error(f"Error copying batch: {response.status_code}, {response.text}")
    else:
        logging.info(f"Successfully copied batch of {len(batch)} records")



# Endpoint to create a new AirTable
@app.get("/create")
def create_endpoint(project_name: str = Query(..., description="Name of the project")):
    try:
        # Create a new base with name provided
        name = create_base(project_name)

        # store the new base id and the table id
        base_id = name.get('base_id')
        table_id = name.get('table_id')

        # copy records from a template base into the new base
        copy_records(base_id, table_id)

        # return the new base url
        return {"url": f"{BASE_URL}/{base_id}/{table_id}/"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
