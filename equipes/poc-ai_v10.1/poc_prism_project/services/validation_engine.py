from loguru import logger


class ValidationEngine:
    """
    TODO (Synapse + Schema): aplicar validação de JSON Schemas
    em cada handoff usando contracts/json_schemas/.
    """

    def validate_handoff(self, agent_name: str, payload: dict) -> bool:
        logger.info(f"ValidationEngine.validate_handoff (stub) para {agent_name}.")
        return True
