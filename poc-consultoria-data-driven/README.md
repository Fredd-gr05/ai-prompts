# Consultoria Estratégica Data-Driven POC

## 📋 Visão Geral

Esta é uma **Prova de Conceito (POC)** para uma **linha de montagem consultiva** com 7 agentes de IA especializados que trabalham em conjunto para criar um plano estratégico data-driven, do briefing inicial até o plano executivo final.

## 🎯 Objetivo

Transformar o briefing de um cliente em artefatos estratégicos estruturados através de um fluxo orquestrado de agentes IA, garantindo qualidade, consistência e conformidade com contratos de documentação.

## 🏗️ Arquitetura

### Stack Tecnológico

- **Orquestração**: LangGraph (workflow como DAG com suporte a paralelismo)
- **LLM Framework**: LangChain
- **Provider LLM**: OpenAI (configurável)
- **Pydantic**: Validação e tipagem de estados
- **Loguru**: Observabilidade e logging estruturado

### 7 Agentes da POC

1. **Theron** - Imersão e Contexto
   - Input: Briefing livre do cliente
   - Output: Relatório de Imersão v0

2. **Lyric** - Diagnóstico Estratégico
   - Input: Relatório de Imersão v0
   - Output: Pacote Diagnóstico v0

3. **Nexis** - Canvas de Modelo de Negócio (em paralelo com Scout)
   - Input: Pacote Diagnóstico v0
   - Output: Canvas v0

4. **Scout** - Mercado e Personas (em paralelo com Nexis)
   - Input: Pacote Diagnóstico v0
   - Output: Personas v0, Análise de Mercado v0, Mapa de Oportunidades SEBRAE v0

5. **Shield** - Validação de Riscos e Conformidade
   - Input: Canvas v0, Análise de Mercado v0 (síncrono após Nexis + Scout)
   - Output: SWOT v0, Matriz de Riscos v0

6. **Synthesis** - Consolidação Estratégica
   - Input: Todos os artefatos anteriores
   - Output: Pacote Consolidado Estratégico v0

7. **Scribe** - Publicação e Formatação
   - Input: Pacote Consolidado Estratégico v0
   - Output: Plano Executivo POC v0 (markdown final)

## 📁 Estrutura de Pastas

```
poc-consultoria-data-driven/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py                           # Ponto de entrada
├── config/
│   ├── settings.yaml                 # Configurações da aplicação
│   └── llm.yaml                      # Configurações de LLM
├── core/
│   ├── state.py                      # Definição do estado compartilhado (Pydantic)
│   ├── graph_builder.py              # Construção do grafo LangGraph
│   └── logging_config.py             # Configuração de logging com loguru
├── agents/
│   ├── __init__.py
│   ├── base_agent.py                 # Classe abstrata para agentes
│   ├── theron.py
│   ├── lyric.py
│   ├── stratos.py
│   ├── nexis.py
│   ├── scout.py
│   ├── shield.py
│   ├── synthesis.py
│   └── scribe.py
├── contracts/
│   ├── __init__.py
│   ├── poc_spec.json                 # Especificação JSON da POC
│   ├── documentos.py                 # Validadores de artefatos
│   └── prompts/
│       ├── theron.md
│       ├── lyric.md
│       ├── nexis.md
│       ├── scout.md
│       ├── shield.md
│       ├── synthesis.md
│       └── scribe.md
├── services/
│   ├── __init__.py
│   ├── llm_provider.py               # Abstração para provider LLM
│   └── telemetry.py                  # Rastreamento de execução
└── data/
    ├── inputs/
    │   └── exemplo_briefing_cliente.md
    └── outputs/
        ├── relatorio_imersao_v0.md
        ├── pacote_diagnostico_v0.md
        ├── canvas_v0.md
        ├── personas_v0.md
        ├── analise_mercado_v0.md
        ├── mapa_oportunidades_sebrae_v0.md
        ├── swot_v0.md
        ├── matriz_riscos_v0.md
        ├── pacote_consolidado_estrategico_v0.md
        └── plano_executivo_poc_v0.md
```

## 🚀 Quick Start

### 1. Clonar e Instalar

```bash
git clone https://github.com/Fredd-gr05/ai-prompts.git
cd ai-prompts/poc-consultoria-data-driven
pip install -r requirements.txt
```

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
OPENAI_API_KEY=sk-...
```

### 3. Preparar Input

Coloque o briefing do cliente em `data/inputs/exemplo_briefing_cliente.md` ou use o padrão.

### 4. Executar a POC

```bash
python main.py
```

Os artefatos serão salvos em `data/outputs/`.

## 📚 Documentação Adicional

- **Especificação Técnica**: Veja `equipes/especificacao_poc.json` no repositório pai
- **Contracts**: Cada agente tem um prompt em `contracts/prompts/` definindo inputs, outputs e formato esperado
- **Estado**: `core/state.py` define a estrutura Pydantic que flui através do workflow

## 🔄 Fluxo de Execução

```
Briefing do Cliente
        ↓
    Theron (Imersão)
        ↓
     Lyric (Diagnóstico)
        ↓
    ┌─────────────────────┐
    ↓                     ↓
  Nexis              Scout
  (Canvas)      (Personas + Mercado)
    ↓                     ↓
    └─────────────────────┘
            ↓
    Shield (Riscos/SWOT)
        ↓
    Synthesis (Consolidação)
        ↓
    Scribe (Publicação)
        ↓
  Plano Executivo
```

## 🛠️ Desenvolvimento

### Adicionar um Novo Agente

1. Criar arquivo em `agents/novo_agente.py`
2. Herdar de `BaseAgent` e implementar `run(state: PocState) -> PocState`
3. Adicionar prompt em `contracts/prompts/novo_agente.md`
4. Registrar no grafo em `core/graph_builder.py`

### Validar Artefatos

Cada agente deve respeitar o contrato de saída. Use `contracts/documentos.py` para validar estrutura.

## 📊 Observabilidade

- Logs estruturados com `loguru` em `core/logging_config.py`
- Rastreamento de estado do workflow em cada etapa
- IDs únicos de execução para correlação

## 🤝 Contribuição

Esta é uma POC. Para sugestões de melhorias ou bugs, abra uma issue no repositório pai.

## 📝 Licença

Seguir a mesma licença do repositório pai `ai-prompts`.

---

**Status**: POC v0.1 | **Last Updated**: Janeiro 2026
