from crewai import Agent, Task


synapse_agent = Agent(
    role="Flow Orchestrator",
    goal=(
        "Implementar orquestração concreta, validação e observabilidade básica sobre o fluxo do Crew."
    ),
    backstory=(
        "Você é o agente Synapse. Usa o skeleton_graph, contratos e JSON Schemas para implementar "
        "services/execution_manager.py, services/validation_engine.py e services/telemetry.py."
    ),
    verbose=True,
)


synapse_task = Task(
    description=(
        "A partir de core/graph_builder.py, contracts/documentos.py e contracts/json_schemas/, "
        "defina o desenho de execução (execution_manager), as regras de validação (validation_engine) "
        "e os pontos mínimos de telemetria (telemetry)."
    ),
    agent=synapse_agent,
    expected_output=(
        "Referências para graph_builder atualizado, services/execution_manager.py, "
        "services/validation_engine.py e services/telemetry.py."
    ),
    async_execution=False,
)
