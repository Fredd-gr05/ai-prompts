from pathlib import Path
from core.state import PocState
from services.llm_provider import LLMProvider
from core.graph_builder import build_graph


def load_briefing() -> str:
    """
    Carrega o briefing do cliente.
    TODO: substituir por input real (CLI, API, UI, etc.)
    """
    path = Path("data/inputs/exemplo_briefing_cliente.md")
    if path.exists():
        return path.read_text(encoding="utf-8")
    else:
        # Briefing padrão para demonstração
        return """
# Briefing do Cliente - POC Consultoria Estratégica

## Contexto
Empresa de tecnologia em fase de expansão mercado LATAM.

## Desafios
- Definição de novo modelo de negócio
- Posicionamento competitivo
- Estratégia de go-to-market

## Objetivo
Desenvolver plano estratégico executivo para os próximos 18 meses.
        """.strip()


def save_outputs(state: PocState) -> None:
    """
    Salva todos os artefatos de saída em data/outputs/.
    """
    out_dir = Path("data/outputs")
    out_dir.mkdir(parents=True, exist_ok=True)

    mapping = {
        "relatorio_imersao_v0": "relatorio_imersao_v0.md",
        "pacote_diagnostico_v0": "pacote_diagnostico_v0.md",
        "canvas_v0": "canvas_v0.md",
        "personas_v0": "personas_v0.md",
        "analise_mercado_v0": "analise_mercado_v0.md",
        "mapa_oportunidades_sebrae_v0": "mapa_oportunidades_sebrae_v0.md",
        "swot_v0": "swot_v0.md",
        "matriz_riscos_v0": "matriz_riscos_v0.md",
        "pacote_consolidado_estrategico_v0": "pacote_consolidado_estrategico_v0.md",
        "plano_executivo_poc_v0": "plano_executivo_poc_v0.md",
    }

    for field, filename in mapping.items():
        content = getattr(state, field, None)
        if content:
            (out_dir / filename).write_text(content, encoding="utf-8")
            print(f"  ✓ Salvo: {filename}")


def main():
    """
    Ponto de entrada principal da POC.
    """
    print("\n" + "="*60)
    print(" Consultoria Estratégica Data-Driven - POC v0.1")
    print("="*60)

    # 1. Carregar briefing
    print("\n[1/3] Carregando briefing do cliente...")
    briefing = load_briefing()
    print(f"  Briefing carregado: {len(briefing)} caracteres")

    # 2. Criar estado inicial
    print("\n[2/3] Inicializando workflow...")
    initial_state = PocState(briefing_livre_cliente=briefing)
    print("  Estado inicial criado")

    # 3. Executar workflow
    print("\n[3/3] Executando workflow (7 agentes em orquestração)...")
    try:
        llm_provider = LLMProvider()
        app = build_graph(llm_provider)
        final_state = app.invoke(initial_state)
        print("  Workflow completado com sucesso!")
    except Exception as e:
        print(f"  \u274c ERRO durante execução: {e}")
        raise

    # 4. Salvar outputs
    print("\n[Salvando artefatos]")
    save_outputs(final_state)

    print("\n" + "="*60)
    print(" POC executada com sucesso!")
    print(" Artefatos disponíveis em: data/outputs/")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
