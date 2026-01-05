from typing import Dict, Any, Optional
from pydantic import BaseModel


class PocState(BaseModel):
    """
    Estado compartilhado que flui pelo workflow dos 7 agentes.
    Cada agente lê e escreve neste estado Pydantic.
    """

    # Inputs iniciais
    briefing_livre_cliente: Optional[str] = None
    documentos_cliente_opcionais: Optional[Dict[str, Any]] = None

    # Artefatos intermediários
    relatorio_imersao_v0: Optional[str] = None
    pacote_diagnostico_v0: Optional[str] = None
    canvas_v0: Optional[str] = None
    personas_v0: Optional[str] = None
    analise_mercado_v0: Optional[str] = None
    mapa_oportunidades_sebrae_v0: Optional[str] = None
    swot_v0: Optional[str] = None
    matriz_riscos_v0: Optional[str] = None
    pacote_consolidado_estrategico_v0: Optional[str] = None
    plano_executivo_poc_v0: Optional[str] = None

    # Metadata
    execution_id: Optional[str] = None
    errors: Optional[Dict[str, str]] = None

    class Config:
        arbitrary_types_allowed = True

    def to_dict(self) -> Dict[str, Any]:
        return self.dict(exclude_none=True)

    def get_completed_artifacts(self) -> Dict[str, str]:
        """Retorna dict com todos os artefatos preenchidos."""
        artifacts = {}
        for field_name, field_value in self.dict().items():
            if field_value is not None and field_name not in [
                "briefing_livre_cliente",
                "documentos_cliente_opcionais",
                "execution_id",
                "errors",
            ]:
                artifacts[field_name] = field_value
        return artifacts
