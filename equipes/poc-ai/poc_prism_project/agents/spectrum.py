from crewai import Agent, Task


spectrum_agent = Agent(
    role="Scope Designer + Requirements Architect",
    goal=(
        "Transformar um briefing vago em uma especificação técnica estruturada de POC, "
        "em conformidade com o schema contracts/json_schemas/especificacao_poc.json."
    ),
    backstory=(
        "Você é o agente Spectrum. Seu foco é ler o briefing, entender o contexto do cliente "
        "e traduzir isso em uma especificação clara para os demais agentes."
    ),
    verbose=True,
)


scope_designer_task = Task(
    description=(
        "A partir de `briefing_text`, `contexto_cliente` e `restricoes_negocio`, "
        "produza `especificacao_poc.json` aderente ao contrato definido em "
        "contracts/json_schemas/especificacao_poc.json."
    ),
    agent=spectrum_agent,
    expected_output=(
        "Um dicionário JSON válido segundo contracts/json_schemas/especificacao_poc.json, "
        "incluindo sequence_A, agent_nodes e handoff_edges mapeados para CrewAI."
    ),
    async_execution=False,
)
