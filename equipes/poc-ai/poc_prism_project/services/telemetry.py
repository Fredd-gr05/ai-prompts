from loguru import logger


class Telemetry:
    """
    TODO (Synapse): coletar traces básicos e logs de execução,
    respeitando observabilidade_minima.
    """

    def trace_event(self, event: str, data: dict | None = None) -> None:
        logger.info(f"Telemetry event={event} data={data}")
