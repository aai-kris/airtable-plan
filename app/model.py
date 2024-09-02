from pydantic import BaseModel
from typing import List, Dict, Any, Optional

# Define Pydantic models for schema components
# Define Pydantic models for schema components
class Choice(BaseModel):
    name: str
    color: str

class FieldOptions(BaseModel):
    choices: Optional[List[Choice]] = None
    dateFormat: Optional[Dict[str, Any]] = None

class Field(BaseModel):
    type: str
    name: str
    options: Optional[FieldOptions] = None

class Table(BaseModel):
    description: str
    fields: List[Field]
    name: str

class Schema(BaseModel):
    name: str
    workspaceId: str
    tables: List[Table]