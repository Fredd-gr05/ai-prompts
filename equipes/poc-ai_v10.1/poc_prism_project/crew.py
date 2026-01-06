from loguru import logger

from core.graph_builder import build_poc_crew


class PocCrew:
    """
    Wrapper da POC para inicializar e executar o Crew.
    """

    def __init__(self) -> None:
        logger.info("Inicializando PocCrew.")
        self.crew = build_poc_crew()

    def run(self, briefing_text: str, contexto_cliente: str = "", restricoes_negocio: str = "") -> dict:
        """
        Executa o fluxo completo Spectrum → Prism → Schema → Synapse → Sentinel → Ryse.
        TODO (Synapse): plugar services.execution_manager / validation_engine.
        """
        logger.info("Iniciando execução do fluxo da POC.")
        inputs = {
            "briefing_text": briefing_text,
            "contexto_cliente": contexto_cliente,
            "restricoes_negocio": restricoes_negocio,
        }
        result = self.crew.kickoff(inputs=inputs)
        logger.info("Execução da POC concluída.")
        return result
