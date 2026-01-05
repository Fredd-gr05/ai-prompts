# Especificação da POC - Cenário A (Simples)

**Data:** 05 de janeiro de 2026  
**Cenário:** A_POC_simples  
**Stack:** CrewAI + LangChain  
**Fonte de verdade:** team_poc.md

---

## 1. Resumo executivo

Esta POC implementa um fluxo **linear e determinístico** de seis agentes (Spectrum, Prism, Schema, Synapse, Sentinel, Ryse) para orquestração de geração de especificações e código de projeto, com foco em **escopo mínimo viável (MVP)**.

Não há paralelismo, roteamento condicional ou workflows de longa duração. O fluxo é síncrono, com handoffs explícitos entre agentes usando contratos (input_schema / output_schema).

---

## 2. Decisões de arquitetura

### 2.1 Por que cenário A (simples)?

- **Restrições iniciais:** Sem requisitos de longa duração, sem processamento paralelo crítico.
- **Vantagem:** Código legível, fácil debugging, rápida validação de conceito.
- **Trade-off:** Não otimizado para escalabilidade ou workflows complexos (será endereçado em cenários B/C).

### 2.2 Por que CrewAI?

- **Abstração alto nível:** Agents e Tasks já encapsulam prompts, tools e sequenciamento.
- **Integração LangChain:** Reutiliza modelos, chains e memory sem refatoring.
- **Prototipagem rápida:** Menos boilerplate que LangGraph puro.
- **Desvantagem:** Menos controle granular sobre DAG (será necessário em cenário C).

### 2.3 Artefatos principais

- **especificacao_poc.json:** Contrato processável para Prism, Schema, Synapse, Sentinel e Ryse. Define schemas de entrada/saída, sequência de agentes, e referências a arquivos.
- **especificacao_poc.md:** Este documento. Orientações, decisões, trade-offs, guia de integração.

---

## 3. Sequência de agentes (cenário A)

### Fluxo linear

Spectrum
↓ (especificacao_poc.json)
Prism
↓ (project_structure.json)
Schema
↓ (contracts_references.json)
Synapse
↓ (orchestration_artifacts.json)
Sentinel
↓ (relatorio_issues.json)
Ryse
↓ (prompts_otimizados/, learnings.md)


