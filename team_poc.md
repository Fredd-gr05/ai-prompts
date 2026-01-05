# Arquitetura da Equipe de Agentes IA - Fase 1

## 1. Visão Geral da Equipe

Equipe multi-agente especializada focada em **POCs rápidas, orientadas a código, com arquitetura limpa e contratos bem definidos**.

### Objetivo Principal
Criar uma **linha de montagem consultiva** que transforma requisitos em código executável, passando por camadas de especificação, geração de skeleton, design de contratos, orquestração e revisão.

### Estrutura da Equipe

```
Ryse (Otimização de Prompts)
  ↓
Spectrum (Especificação)
  ↓
Prism (Skeleton + Technology)
  ↓
Schema (Contratos de Dados)
  ↓
Synapse (Orquestração)
  ↓
Sentinel (Code Review)
  ↓
Ryse (Feedback Loop)
```

---

## 2. Agentes da Equipe - Responsabilidades

### 🎯 SPECTRUM – Scope Designer + Requirements Architect

**Entrada**: Briefing/requisitos do cliente (texto livre)

**Responsabilidades**:
- Transformar requisitos vagos em especificação técnica estruturada
- Definir escopo da POC (o que entra/sai)
- Mapear fluxos de trabalho e decisões
- Documentar constraints e assumpções
- Gerar JSON estruturado com especificação POC

**Saída**:
- `especificacao_poc.md` (Markdown conceitual)
- `especificacao_poc.json` (Estrutura técnica)
- Tabela de requisitos vs. decisões de design

**Handoff**: Entrega tudo para Prism

---

### ⚙️ PRISM – Skeleton Generator + Complete Core Implementation

**Entrada**: `especificacao_poc.md` + `especificacao_poc.json` (Spectrum)

**Responsabilidades**:
- Recomendar framework (CrewAI, LangChain, LangGraph, híbrida)
- Gerar **TODOS os arquivos core**:
  - `core/state.py` - Estado compartilhado (TypedDict/Pydantic)
  - `core/graph_builder.py` - Orquestração skeleton
  - `contracts/documentos.py` - Modelos Pydantic base
  - `agents/{agente}.py` - Stubs com assinatura
  - `config/settings.yaml` - Configurações
  - `requirements.txt` - Dependências
  - `main.py` - Entry point executável
  - `README.md` - Setup e arquitetura
- Mapear entradas/saídas de cada agente
- Marcar `# TODO: Schema:`, `# TODO: Synapse:` comentários

**Saída**: Skeleton completo, estrutura de código, documentação de interfaces

**Handoff**: Tudo para Schema

---

### 📋 SCHEMA – Agent Contract Designer

**Entrada**: `core/state.py` + `core/graph_builder.py` + `agents/` stubs (Prism)

**Responsabilidades**:
- Detalhar **contratos de dados** para cada agente
- Preencher `contracts/documentos.py` com modelos Pydantic reais
- Criar JSON Schema para cada saída de agente
- Documentar validações, constraints, tipos
- Criar tabela mestre de contratos (inputs/outputs)
- Validar tipagem e coerência entre agentes

**Saída**:
- `contracts/documentos.py` completo com Pydantic models
- `contracts/json_schemas/` com JSON Schema para cada saída
- Tabela de contratos de dados (matriz inputs/outputs)
- Documentação de validações

**Handoff**: Código + documentação para Synapse

---

### 🔄 SYNAPSE – Flow Orchestrator

**Entrada**: Código Prism + contratos Schema preenchidos

**Responsabilidades**:
- Implementar **orquestração concreta** do fluxo
- Codificar sequência exata de agentes
- Adicionar paralelismo (nós que rodam simultâneos)
- Adicionar sincronização (nós que aguardam)
- Implementar lógica de retry com backoff exponencial
- Implementar fallback strategies
- Adicionar validação de contratos entre etapas
- Implementar observabilidade (logging estruturado, trace IDs)

**Saída**:
- `core/graph_builder.py` completo com nós/edges
- `services/execution_manager.py` com retry/fallback logic
- `services/validation_engine.py` com validação de contratos
- `services/telemetry.py` com logging

**Handoff**: Código orquestrado completo para Sentinel

---

### 🛡️ SENTINEL – Code Review Architect

**Entrada**: Código completo (Prism + Schema + Synapse)

**Responsabilidades**:
- Revisar **robustez, segurança e conformidade**
- Validar tratamento de exceções
- Verificar segurança (OWASP, rate limiting, PII)
- Revisar cobertura de testes
- Testar cenários extremos
- Identificar race conditions, timeouts inadequados
- Sugerir hardening e refactorings
- Validate conformidade com especificação

**Saída**:
- Relatório de Issues (Crítico | Alto | Recomendação)
- Código de teste (test_execution_resilience.py)
- Código de segurança (security_checks.py)
- Sugestões para Ryse

**Handoff**: Feedback para Ryse, código pronto para produção

---

### 🔁 RYSE – Prompt Optimizer + Feedback Loop

**Entrada**: Feedback de Sentinel + saídas de cada agente

**Responsabilidades**:
- Analisar **qualidade** dos outputs de cada agente
- Identificar gaps entre esperado vs. entregue
- Refinar prompts baseado em resultados reais
- Documentar learnings e padrões
- Realinhar equipe com objetivos do negócio
- Melhorar iterativamente a POC

**Saída**:
- Prompts otimizados para próxima iteração
- Documento de learnings
- Recomendações de ajustes

**Handoff**: Volta para Spectrum (próxima iteração) ou aprovação final

---

## 3. Fluxo de Dados e Handoffs

### Fase 1: Especificação (Spectrum)
```
Briefing Cliente
       ↓
Spectrum analisa
       ↓
especificacao_poc.md + .json
       ↓
    [HANDOFF → Prism]
```

### Fase 2: Skeleton Generation (Prism)
```
especificacao_poc.*
       ↓
Prism recomenda framework
       ↓
Gera: core/, contracts/, agents/, config/, requirements.txt, README
       ↓
    [HANDOFF → Schema]
```

### Fase 3: Contract Design (Schema)
```
core/state.py + agents stubs
       ↓
Schema detalha contratos
       ↓
contracts/documentos.py + JSON Schemas
       ↓
    [HANDOFF → Synapse]
```

### Fase 4: Orchestration (Synapse)
```
Código Prism + Contratos Schema
       ↓
Synapse implementa orquestração
       ↓
core/graph_builder.py completo + services/
       ↓
    [HANDOFF → Sentinel]
```

### Fase 5: Code Review (Sentinel)
```
Código completo Prism+Schema+Synapse
       ↓
Sentinel revisa e testa
       ↓
Relatório de Issues + sugestões
       ↓
    [HANDOFF → Ryse]
```

### Fase 6: Optimization (Ryse)
```
Issues + Feedback Sentinel
       ↓
Ryse analisa qualidade
       ↓
Prompts otimizados + Learnings
       ↓
    [LOOP → Spectrum ou APROVAÇÃO FINAL]
```

---

## 4. Interfaces de Entrada/Saída

### Spectrum Output → Prism Input
```json
{
  "especificacao_poc": {
    "agentes_envolvidos": [...],
    "fluxos": [...],
    "restricoes": {...},
    "assuncoes": [...]
  }
}
```

### Prism Output → Schema Input
```
core/
├── state.py          # ← Schema usa como referência
├── graph_builder.py  # ← Schema valida com contratos
contracts/
├── documentos.py     # ← Schema preenche aqui
agents/
└── *.py             # ← Schema documenta inputs/outputs
```

### Schema Output → Synapse Input
```
contracts/documentos.py (preenchido)
contracts/json_schemas/
├── relatorio_imersao.json
├── pacote_diagnostico.json
└── ...
contratos_matriz.md
```

---

## 5. Protocolos e Padrões

### Nomeação de Arquivos
- **Agentes**: `{agent_name}_lowercase.md` → `theron_imersao.md`
- **Contratos**: `{entidade}_schema.json` → `relatorio_imersao_schema.json`
- **Código**: PEP 8 Python + type hints

### Estrutura de Commits
```
feat(agente): descrição
refactor(agente): melhoria
fix(agente): correção
docs(agente): documentação
```

### TODO Comments
```python
# TODO: Schema: definir validações para este campo
# TODO: Synapse: implementar retry logic aqui
# TODO: Sentinel: adicionar teste para este cenário
```

---

## 6. Tecnologias Recomendadas

### Para Orquestração
- **LangGraph** (complex DAG workflows)
- **CrewAI** (simple multi-agent)
- **Temporal** (long-running workflows)

### Para Validação
- **Pydantic** (data validation)
- **JSON Schema** (contract specification)

### Para Observabilidade
- **Loguru** (logging estruturado)
- **Trace IDs** (request tracking)
- **Prometheus** (metrics)

### Para Testes
- **pytest** (unit/integration tests)
- **pytest-asyncio** (async tests)
- **mock** (mocking LLM calls)

---

## 7. Qualidade e SLAs

### Por Agente
| Agente | Latência | Qualidade | Retenção |
|--------|----------|-----------|----------|
| Spectrum | < 5 min | Spec completa | Sem estado |
| Prism | < 10 min | Código pronto | Sem estado |
| Schema | < 5 min | Contratos válidos | Documentação |
| Synapse | < 10 min | Orquestração funcionando | Testes |
| Sentinel | < 15 min | Issues claras | Relatório |
| Ryse | < 10 min | Prompts otimizados | Feedback loop |

### Métricas de Sucesso
- ✅ Especificação 100% clara para Prism
- ✅ Skeleton 100% executável no 1º ciclo
- ✅ Contratos 100% válidos e documentados
- ✅ Orquestração sem erros (0 race conditions)
- ✅ 0 issues críticas de segurança
- ✅ Iteração completa em < 1 hora

---

## 8. Próximos Passos

### Curto Prazo (1-2 semanas)
1. Testar fluxo completo com uma POC real
2. Refinar handoffs entre agentes
3. Criar templates para cada agente
4. Implementar Ryse optimization loop

### Médio Prazo (1 mês)
1. Adicionar suporte para diferentes tipos de POCs
2. Criar library de padrões reutilizáveis
3. Implementar versionamento de prompts
4. Criar dashboard de qualidade

### Longo Prazo (Fase 2)
1. Expandir para produção (não apenas POC)
2. Adicionar mais agentes especializados
3. Implementar auto-scaling e parallelismo
4. Integrar com CI/CD

---

**Versão**: 1.0  
**Data**: Janeiro 2026  
**Time Lead**: Você (Arquiteto Sênior)  
**Status**: Pronto para Primeira Execução
