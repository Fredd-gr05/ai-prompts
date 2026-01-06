from loguru import logger

from crew import PocCrew


def main() -> None:
    logger.add("logs/crew_run.log", level="INFO", enqueue=True, backtrace=True, diagnose=True)

    briefing_text = "POC de orquestração de 6 agentes para geração de skeleton de projeto."
    contexto_cliente = "Cliente enterprise, foco em validação rápida de conceito."
    restricoes_negocio = "Sem integrações externas de produção, sem paralelismo."

    crew = PocCrew()
    result = crew.run(
        briefing_text=briefing_text,
        contexto_cliente=contexto_cliente,
        restricoes_negocio=restricoes_negocio,
    )
    logger.info(f"Resultado final da POC: {result}")


if __name__ == "__main__":
    main()
