from app.model import Schema, Table, Field, FieldOptions, Choice


def get_schema(project_name: str, workspace_id: str):
    return Schema(
        name=f"{project_name}",
        workspaceId=f"{workspace_id}",
        tables=[
            Table(
                description="Baseline tasks for an Epic",
                name="Tasks",
                fields=[
                    Field(type="multilineText", name="Activity"),
                    Field(
                        type="multipleSelects",
                        name="Phase",
                        options=FieldOptions(
                            choices=[
                                Choice(name="Technical Discovery", color="blueLight2"),
                                Choice(name="Initiation", color="blueBright"),
                                Choice(name="Development", color="blueDark1"),
                                Choice(name="Pre Deployment Checks", color="purpleLight1"),
                                Choice(name="Deployment", color="tealLight2"),
                                Choice(name="Early Access Release", color="cyanLight2"),
                                Choice(name="Launch", color="tealDark1"),
                            ]
                        ),
                    ),
                    Field(
                        type="multipleSelects",
                        name="Driver",
                        options=FieldOptions(
                            choices=[
                                Choice(name="TL", color="blueLight2"),
                                Choice(name="EM", color="cyanLight2"),
                                Choice(name="TPM", color="tealLight2"),
                                Choice(name="Product", color="greenLight2"),
                                Choice(name="Marketing", color="redLight2"),
                                Choice(name="DevRel", color="orangeLight2"),
                                Choice(name="Solutions", color="tealLight1"),
                                Choice(name="Support", color="purpleLight2"),
                            ]
                        ),
                    ),
                    Field(
                        type="multipleSelects",
                        name="Consulted",
                        options=FieldOptions(
                            choices=[
                                Choice(name="TL", color="blueLight2"),
                                Choice(name="EM", color="cyanLight2"),
                                Choice(name="TPM", color="tealLight2"),
                                Choice(name="Product", color="greenLight2"),
                                Choice(name="Marketing", color="redLight2"),
                                Choice(name="DevRel", color="orangeLight2"),
                                Choice(name="Solutions", color="tealLight1"),
                                Choice(name="Support", color="purpleLight2"),
                                Choice(name="", color="grayLight2"),
                            ]
                        ),
                    ),
                    Field(
                        type="date",
                        name="Due Date",
                        options=FieldOptions(
                            dateFormat={
                                "name": "local",
                                "format": "l"
                            }
                        )
                    ),
                    Field(
                        type="singleSelect",
                        name="Status",
                        options=FieldOptions(
                            choices=[
                                Choice(name="To Do", color="blueLight2"),
                                Choice(name="In Progress", color="blueLight1"),
                                Choice(name="Done", color="greenDark1"),
                                Choice(name="Blocked", color="redBright"),
                                Choice(name="N/A", color="grayBright"),
                            ]
                        ),
                    ),
                    Field(type="singleCollaborator", name="Who Completed"),
                ]
            )
        ]
    )