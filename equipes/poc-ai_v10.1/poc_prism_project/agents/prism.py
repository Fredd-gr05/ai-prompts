from crewai import Agent, Task


prism_agent = Agent(
    role="Skeleton Generator + Core Implementation",
    goal=(
        "Gerar estrutura de projeto, arquivos core e stubs de agentes a partir da especificação da POC."
    ),
    backstory=(
        "Você é o agente Prism. Recebe a especificação da POC e devolve um skeleton de projeto Python "
        "executável, incluindo core/state.py, core/graph_builder.py, crew.py e arquivos em agents/."
    ),
    verbose=True,
)


skeleton_generator_task = Task(
    description=(
        "Usando a especificação de POC produzida por Spectrum, liste todos os arquivos do skeleton "
        "com path, kind (code/config/doc) e breve descrição."
    ),
    agent=prism_agent,
    expected_output=(
        "Objeto com campo `files`, array de objetos {path, kind, description}, "
        "conforme schema de saída de Prism."
    ),
    async_execution=False,
)
