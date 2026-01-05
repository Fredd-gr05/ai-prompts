## Resumo do escopo POC

Para o **cenário A_POC_simples** com **CrewAI**, recortamos para fluxo linear com os 6 agentes essenciais: Spectrum → Prism → Schema → Synapse → Sentinel → Ryse.  
Foco em viabilidade: validar handoffs via JSON schemas, sem paralelismo, sem rotas condicionais, sem workflows longos.  
Escopo mínimo: entrada é briefing + restrições de negócio; saída é projeto esqueleto com contratos, orquestração básica, relatório de issues e otimizações iniciais de prompts.

## Decisões de recorte

**O que entra na POC:**
- Sequência linear de 6 agentes com dependências explícitas (cada task espera output anterior).
- Mapeamento direto para CrewAI: cada agente = Agent/Task, handoff = `task.depends_on(previous_task)`.
- Validação de schemas em cada handoff (input/output JSON validados via `contracts/json_schemas/`).
- Features mínimas: `core/state.py` para estado compartilhado, `core/graph_builder.py` para definição de tarefas, `agents/` com prompts v0.

**O que sai da POC (para cenários B/C):**
- Paralelismo, rotas condicionais, `retry_policies`, `signals_timers`, workflows longos (Temporal).
- Features avançadas de observability, resiliência e telemetria complexa.
- Integrações externas (ex.: APIs de produção, bancos de dados reais).

**Trade-offs:**
- Linearidade garante simplicidade e debugabilidade rápida, mas sacrifica performance em cenários reais de produção.
- CrewAI é ideal para POC por abstrair orquestração, mas LangGraph seria mais flexível para B/C (decisão adiada).
- Validação de schemas em runtime adiciona overhead (~10-20% latência), mas garante robustez nos handoffs.

## Orientações por agente

**Spectrum (você aqui):**  
Gere `especificacao_poc.json` com `sequence_A`, `agent_nodes` e `handoff_edges` mapeados para CrewAI.

**Prism:**  
Gere skeleton de `crew.py`, `core/state.py`, `core/graph_builder.py` e pasta `agents/` com prompts v0.

**Schema:**  
Defina `contracts/documentos.py`, `contracts/json_schemas/especificacao_poc.json`, `contratos_matriz.md` com validação pydantic.

**Synapse:**  
Implemente execução via `execution_manager.py` e `validation_engine.py`, rodando o crew e coletando traces básicas.

**Sentinel:**  
Revise código gerado, gere `reports/relatorio_issues.json` com issues de segurança, testes unitários e checagens de contratos.

**Ryse:**  
Otimize prompts baseados em `relatorio_issues`, gere `prompts_otimizados/` e `learnings.md` com 3 lições principais.

Aguardando seu OK para gerar o `especificacao_poc.json` processável.
