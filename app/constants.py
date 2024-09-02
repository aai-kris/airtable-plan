BASE_URL = "https://airtable.com"
BASE_API_URL = "https://api.airtable.com/v0"
WORKSPACE_ID = "wsphJ8iveDIazmRjj"
SOURCE_ID = "appAZddmNYImc3Bxx"
SOURCE_TABLE = "tblbuSCqj6oR6vdTx"
TABLES = [
    {
        "description": "Baseline tasks for an Epic",
        "fields": [
            {
                "type": "multilineText",
                "name": "Activity"
            },
            {
                "type": "multipleSelects",
                "options": {
                    "choices": [
                        {
                            "name": "Technical Discovery",
                            "color": "blueLight2"
                        },
                        {
                            "name": "Initiation",
                            "color": "blueBright"
                        },
                        {
                            "name": "Development",
                            "color": "blueDark1"
                        },
                        {
                            "name": "Pre Deployment Checks",
                            "color": "purpleLight1"
                        },
                        {
                            "name": "Deployment",
                            "color": "tealLight2"
                        },
                        {
                            "name": "Early Access Release",
                            "color": "cyanLight2"
                        },
                        {
                            "name": "Launch",
                            "color": "tealDark1"
                        }
                    ]
                },
                "name": "Phase"
            },
            {
                "type": "multipleSelects",
                "options": {
                    "choices": [
                        {
                            "name": "TL",
                            "color": "blueLight2"
                        },
                        {
                            "name": "EM",
                            "color": "cyanLight2"
                        },
                        {
                            "name": "TPM",
                            "color": "tealLight2"
                        },
                        {
                            "name": "Product",
                            "color": "greenLight2"
                        },
                        {
                            "name": "Marketing",
                            "color": "redLight2"
                        },
                        {
                            "name": "DevRel",
                            "color": "orangeLight2"
                        },
                        {
                            "name": "Solutions",
                            "color": "tealLight1"
                        },
                        {
                            "name": "Support",
                            "color": "purpleLight2"
                        }
                    ]
                },
                "name": "Driver"
            },
            {
                "type": "multipleSelects",
                "options": {
                    "choices": [
                        {
                            "name": "TL",
                            "color": "blueLight2"
                        },
                        {
                            "name": "EM",
                            "color": "cyanLight2"
                        },
                        {
                            "name": "TPM",
                            "color": "tealLight2"
                        },
                        {
                            "name": "Product",
                            "color": "greenLight2"
                        },
                        {
                            "name": "Marketing",
                            "color": "redLight2"
                        },
                        {
                            "name": "DevRel",
                            "color": "orangeLight2"
                        },
                        {
                            "name": "Solutions",
                            "color": "tealLight1"
                        },
                        {
                            "name": "Support",
                            "color": "purpleLight2"
                        },
                        {
                            "name": "",
                            "color": "grayLight2"
                        }
                    ]
                },
                "name": "Consulted"
            },
            {
                "type": "date",
                "options": {
                    "dateFormat": {
                        "name": "local",
                        "format": "l"
                    }
                },
                "name": "Due Date"
            },
            {
                "type": "singleSelect",
                "options": {
                    "choices": [
                        {
                            "name": "To Do",
                            "color": "blueLight2"
                        },
                        {
                            "name": "In Progress",
                            "color": "blueLight1"
                        },
                        {
                            "name": "Done",
                            "color": "greenDark1"
                        },
                        {
                            "name": "Blocked",
                            "color": "redBright"
                        },
                        {
                            "name": "N/A",
                            "color": "grayBright"
                        }
                    ]
                },
                "name": "Status"
            },
            {
                "type": "singleCollaborator",
                "name": "Who Completed"
            },
            {
                "type": "number",
                "options": {
                    "precision": 0
                },
                "name": "Sort"
            }
        ],
        "name": "Tasks"
    }
]