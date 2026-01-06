from crewai import Agent, Task


sentinel_agent = Agent(
    role="Code Review Architect",
    goal=(
        "Revisar robustez, segurança, testes e conformidade com a especificação da POC."
    ),
    backstory=(
        "Você é o agente Sentinel. Analisa o projeto, identifica issues e sugere testes e checks "
        "de segurança mínimos."
    ),
    verbose=True,
)


sentinel_task = Task(
    description=(
        "Ler o diretório do projeto e o core/graph_builder.py, identificar problemas de "
        "segurança, robustez e aderência aos contratos, e gerar relatórios e testes base."
    ),
    agent=sentinel_agent,
    expected_output=(
        "Geração lógica de reports/relatorio_issues.json, tests/test_execution_resilience.py "
        "e tests/security_checks.py, além de recomendações para Ryse."
    ),
    async_execution=False,
)
