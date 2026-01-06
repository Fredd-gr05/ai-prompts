#!/usr/bin/env bash
set -e

PROJECT_ROOT="poc_prism_project"

echo "Criando estrutura em: ${PROJECT_ROOT}"
mkdir -p ${PROJECT_ROOT}
cd ${PROJECT_ROOT}

# pastas principais
mkdir -p core agents contracts/json_schemas services reports tests prompts_otimizados logs

# requirements.txt
cat > requirements.txt << 'EOF'
python-dotenv
crewai
pydantic
langchain
loguru
EOF

# core/state.py
cat > core/state.py << 'EOF'
from typing import Any, Dict
from pydantic import BaseModel


class PocState(BaseModel):
    """
    Estado compartilhado entre os agentes da POC.
    TODO (Schema): especializar campos com base em contratos/documentos.py.
    """
    briefing_text: str | None = None
    contexto_cliente: str | None = None
    restricoes_negocio: str | None = None

    especificacao_poc: Dict[str, Any] | None = None
    skeleton_files: Dict[str, Any] | None = None
    contratos_info: Dict[str, Any] | None = None
    execucao_info: Dict[str, Any] | None = None
    relatorio_issues: Dict[str, Any] | None = None
    prompts_ajustados: Dict[str, Any] | None = None
EOF

# core/graph_builder.py
cat > core/graph_builder.py << 'EOF'
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
EOF

# core/__init__.py
cat > core/__init__.py << 'EOF'
# Core package for POC Prism project.
EOF

# crew.py
cat > crew.py << 'EOF'
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
EOF

# agents/__init__.py
cat > agents/__init__.py << 'EOF'
# Agents package for POC Prism project.
EOF

# agents/spectrum.py
cat > agents/spectrum.py << 'EOF'
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
EOF

# agents/prism.py
cat > agents/prism.py << 'EOF'
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
EOF

# agents/schema.py
cat > agents/schema.py << 'EOF'
from crewai import Agent, Task


schema_agent = Agent(
    role="Agent Contract Designer",
    goal="Definir contratos de dados, Pydantic models e JSON Schemas para o fluxo da POC.",
    backstory=(
        "Você é o agente Schema. A partir do skeleton gerado, cria contratos/documentos.py, "
        "contracts/json_schemas/ e contratos_matriz.md."
    ),
    verbose=True,
)


schema_task = Task(
    description=(
        "Receber informações sobre state.py, graph_builder.py e agents/ e projetar os contratos "
        "de dados necessários, incluindo Pydantic models e JSON Schemas."
    ),
    agent=schema_agent,
    expected_output=(
        "Referências concretas para contracts/documentos.py, contracts/json_schemas/ e contratos_matriz.md."
    ),
    async_execution=False,
)
EOF

# agents/synapse.py
cat > agents.synapse.py << 'EOF'
from crewai import Agent, Task


synapse_agent = Agent(
    role="Flow Orchestrator",
    goal=(
        "Implementar orquestração concreta, validação e observabilidade básica sobre o fluxo do Crew."
    ),
    backstory=(
        "Você é o agente Synapse. Usa o skeleton_graph, contratos e JSON Schemas para implementar "
        "services/execution_manager.py, services/validation_engine.py e services/telemetry.py."
    ),
    verbose=True,
)


synapse_task = Task(
    description=(
        "A partir de core/graph_builder.py, contracts/documentos.py e contracts/json_schemas/, "
        "defina o desenho de execução (execution_manager), as regras de validação (validation_engine) "
        "e os pontos mínimos de telemetria (telemetry)."
    ),
    agent=synapse_agent,
    expected_output=(
        "Referências para graph_builder atualizado, services/execution_manager.py, "
        "services/validation_engine.py e services/telemetry.py."
    ),
    async_execution=False,
)
EOF

# agents/sentinel.py
cat > agents/sentinel.py << 'EOF'
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
EOF

# agents/ryse.py
cat > agents/ryse.py << 'EOF'
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
EOF

# contracts/__init__.py
cat > contracts/__init__.py << 'EOF'
# Contracts package for POC Prism project.
EOF

# contracts/documentos.py (stub para Schema)
cat > contracts/documentos.py << 'EOF'
"""
TODO (Schema): definir Pydantic models e estruturas de dados
para todos os handoffs entre os agentes da POC.
"""
EOF

# contracts/json_schemas/especificacao_poc.json (stub)
cat > contracts/json_schemas/especificacao_poc.json << 'EOF'
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "EspecificacaoPOC",
  "type": "object",
  "description": "TODO (Schema): especializar campos deste schema conforme imput_prism.json.",
  "properties": {
    "sequence_A": {
      "type": "array",
      "items": { "type": "string" }
    }
  }
}
EOF

# services/__init__.py
cat > services/__init__.py << 'EOF'
# Services package for POC Prism project.
EOF

# services/execution_manager.py
cat > services/execution_manager.py << 'EOF'
from loguru import logger


class ExecutionManager:
    """
    TODO (Synapse): Implementar camada de execução que chama PocCrew,
    aplica validações e consolida resultados.
    """

    def run_once(self, inputs: dict) -> dict:
        logger.info("ExecutionManager.run_once chamado (stub).")
        return {"status": "not_implemented", "inputs": inputs}
EOF

# services/validation_engine.py
cat > services/validation_engine.py << 'EOF'
from loguru import logger


class ValidationEngine:
    """
    TODO (Synapse + Schema): aplicar validação de JSON Schemas
    em cada handoff usando contracts/json_schemas/.
    """

    def validate_handoff(self, agent_name: str, payload: dict) -> bool:
        logger.info(f"ValidationEngine.validate_handoff (stub) para {agent_name}.")
        return True
EOF

# services/telemetry.py
cat > services/telemetry.py << 'EOF'
from loguru import logger


class Telemetry:
    """
    TODO (Synapse): coletar traces básicos e logs de execução,
    respeitando observabilidade_minima.
    """

    def trace_event(self, event: str, data: dict | None = None) -> None:
        logger.info(f"Telemetry event={event} data={data}")
EOF

# reports stub
cat > reports/relatorio_issues.json << 'EOF'
{
  "status": "pending",
  "issues": []
}
EOF

# tests/__init__.py
cat > tests/__init__.py << 'EOF'
# Tests package for POC Prism project.
EOF

# tests/test_execution_resilience.py
cat > tests/test_execution_resilience.py << 'EOF'
"""
TODO (Sentinel): implementar testes de resiliência de execução do fluxo Crew.
"""
EOF

# tests/security_checks.py
cat > tests/security_checks.py << 'EOF'
"""
TODO (Sentinel): implementar checagens mínimas de segurança do código e configurações.
"""
EOF

# learnings.md (Ryse)
cat > learnings.md << 'EOF'
# Learnings (Ryse)

TODO (Ryse): registrar três principais aprendizados da POC.
EOF

# main.py
cat > main.py << 'EOF'
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
EOF

echo "Projeto criado em ${PROJECT_ROOT}. Para rodar:"
echo "  cd ${PROJECT_ROOT}"
echo "  pip install -r requirements.txt"
echo "  python main.py"
EOF
