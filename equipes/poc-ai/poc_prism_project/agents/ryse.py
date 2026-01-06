from crewai import Agent, Task


ryse_agent = Agent(
    role="Prompt Optimizer + Feedback Loop",
    goal=(
        "Analisar qualidade dos outputs dos agentes e otimizar prompts com base em feedback e métricas."
    ),
    backstory=(
        "Você é o agente Ryse. Usa relatorio_issues.json e amostras de execução para refinar os prompts "
        "e registrar aprendizados."
    ),
    verbose=True,
)


ryse_task = Task(
    description=(
        "Com base no reports/relatorio_issues.json e em amostras de execução, "
        "propor ajustes de prompts para os agentes e registrar learnings.md."
    ),
    agent=ryse_agent,
    expected_output=(
        "Referências a prompts_otimizados/ e learnings.md, além de eventuais ajustes na especificação."
    ),
    async_execution=False,
)
