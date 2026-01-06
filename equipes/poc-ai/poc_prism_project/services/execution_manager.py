from loguru import logger


class ExecutionManager:
    """
    TODO (Synapse): Implementar camada de execução que chama PocCrew,
    aplica validações e consolida resultados.
    """

    def run_once(self, inputs: dict) -> dict:
        logger.info("ExecutionManager.run_once chamado (stub).")
        return {"status": "not_implemented", "inputs": inputs}
