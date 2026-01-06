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
