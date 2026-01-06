from typing import List
from crewai import Crew, Process
from loguru import logger

from agents.spectrum import scope_designer_task, spectrum_agent
from agents.prism import prism_agent, skeleton_generator_task
from agents.schema import schema_agent, schema_task
from agents.synapse import synapse_agent, synapse_task
from agents.sentinel import sentinel_agent, sentinel_task
from agents.ryse import ryse_agent, ryse_task


def build_poc_crew() -> Crew:
    """
    Constrói o Crew linear conforme orientacoes_implementacao_crewai.execution_flow = 'linear'.
    TODO (Synapse): integrar validação/telemetria mais profunda via services/.
    """
    logger.info("Construindo PocCrew com fluxo linear de 6 agentes.")

    tasks: List = [
        scope_designer_task,
        skeleton_generator_task,
        schema_task,
        synapse_task,
        sentinel_task,
        ryse_task,
    ]

    crew = Crew(
        agents=[
            spectrum_agent,
            prism_agent,
            schema_agent,
            synapse_agent,
            sentinel_agent,
            ryse_agent,
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )
    return crew
