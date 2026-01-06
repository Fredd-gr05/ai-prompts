from crewai import Agent, Task


schema_agent = Agent(
    role="Agent Contract Designer",
    goal="Definir contratos de dados, Pydantic models e JSON Schemas para o fluxo da POC.",
    backstory=(
        "Você é o agente Schema. A partir do skeleton gerado, cria contratos/documentos.py, "
        "contracts/json_schemas/ e contratos_matriz.md."
    ),
    verbose=True,
)


schema_task = Task(
    description=(
        "Receber informações sobre state.py, graph_builder.py e agents/ e projetar os contratos "
        "de dados necessários, incluindo Pydantic models e JSON Schemas."
    ),
    agent=schema_agent,
    expected_output=(
        "Referências concretas para contracts/documentos.py, contracts/json_schemas/ e contratos_matriz.md."
    ),
    async_execution=False,
)
