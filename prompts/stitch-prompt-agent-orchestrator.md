# **PROMPT COMPLETO PARA STITCH - ORQUESTRADOR DE AGENTES IA**

## **Sistema Híbrido de Configuração e Orquestração: CrewAI + LangChain**

Quero um **protótipo profissional de aplicação web desktop** para gerenciar, configurar, testar e orquestrar execução de agentes de IA em **CrewAI e/ou LangChain**, com suporte completo a **pipelines de execução com passagem de dados entre agentes (handoffs)**.

***

### **VISÃO GERAL DAS TELAS**

1. **Dashboard Principal** - Visão geral do sistema
2. **Gerenciador de Agentes** - CRUD com 8 abas de config
3. **Gerenciador de Handoffs** - Conexões entre agentes  
4. **Gerenciador de Pipelines** - Sequências de execução
5. **Acompanhamento de Execução** - Real-time do pipeline em andamento
6. **Teste de Agente** - Testar agente isolado
7. **Comparador A/B** - Testar dois agentes em paralelo
8. **Configurações Globais** - Settings do app

***

## **TELA 1: DASHBOARD PRINCIPAL**

**Header**: Logo | Status Supabase | Notificações | Menu Usuário

**Sidebar**: Dashboard | Agentes | Pipelines | Handoffs | Execuções | Documentação | Configurações

**Conteúdo**:
- 4 Cards: Total Agentes | Pipelines Ativos | Execuções Hoje | Custo Estimado
- Section: Pipeline em Execução (se houver) com progresso visual
- Tabela: Agentes Mais Usados (Nome | Tipo | Execuções 7d | Taxa Sucesso | Última)
- Feed: Atividade Recente (timestamps com ícones)

***

## **TELA 2: GERENCIADOR DE AGENTES (CRUD)**

**Layout**: Coluna esquerda (lista) + Coluna direita (editor com abas)

### **ESQUERDA - Lista de Agentes**:
- Busca | Filtros (Tipo, Status)
- Cards com agentes (Nome | Tipo | Status | Última Atualização)
- "+ Novo Agente"

### **DIREITA - Editor com 8 Abas**:

**TAB 1 - Identidade**:
- agent_name (text, obrigatório, unique)
- role (textarea, obrigatório)
- goal (textarea, obrigatório)
- description (textarea)
- agent_type (select: CrewAI | LangChain | Hybrid)

**TAB 2 - Modelo e Parâmetros**:
- llm_model (select dropdown: gpt-4.1, gpt-4o-mini, gpt-4-turbo, claude-3-opus, claude-3-sonnet, custom)
- model_config (JSON editor com UI helpers):
  - temperature (slider 0-1, default 0.7)
  - max_tokens (input, default 2048)
  - top_p (slider 0-1, default 0.95)
  - frequency_penalty (slider 0-1, default 0)
  - presence_penalty (slider 0-1, default 0)

**TAB 3 - Execução e Limites**:
- max_iterations (input, default 20)
- max_execution_time (input em segundos, default 300)
- max_retry_limit (input, default 2)
- verbose (toggle, default true)
- enabled_for_crewai (toggle)
- enabled_for_langchain (toggle)

**TAB 4 - Prompts**:
- system_prompt (rich textarea com botão "Inserir Variável")
- user_prompt_template (rich textarea)
- output_format (select: text | json | structured)

**TAB 5 - CrewAI Específico** (visível se type = crewai/hybrid):
- backstory (textarea, OBRIGATÓRIO)
- cache (toggle, default true)
- allow_delegation (toggle, default false)
- reasoning (toggle, default false)
- allow_code_execution (toggle, default false)
- respect_context_window (toggle, default true)
- code_execution_mode (select: safe | unsafe)

**TAB 6 - LangChain Específico** (visível se type = langchain/hybrid):
- agent_type (select: ReAct | Tool Calling | Conversational | Custom)
- memory_type (select: Buffer | Summary | Token Buffer | Entity | KG)
- memory_max_size (input, default 10)
- memory_token_limit (input, default 2000)
- parser_type (select: JSON | Pydantic | CSV List | Structured | Custom)
- callbacks (multi-checkbox: LangSmith | Custom Webhook | Logging | Monitoring)
- early_stopping_method (select: force | generate)

**TAB 7 - Ferramentas**:
- Multi-select com busca de tools
- Tabela: Nome | Categoria | Descrição | Status | Ação
- "+ Adicionar Tool Customizada"

**TAB 8 - Metadados e Controle**:
- status (select: draft | active | testing | archived)
- version (read-only)
- created_by (read-only)
- created_at (read-only)
- updated_at (read-only)
- notes (textarea)
- Botões: [Salvar] [Salvar e Testar] [Cancelar] [Deletar]

***

## **TELA 3: GERENCIADOR DE HANDOFFS**

**Layout**: Fluxograma visual + Editor lateral

### **ESQUERDA - Fluxograma Visual**:
```
[Spectrum] → [Prism] → [Schema]
                ↓
          [Synapse]
          ↙        ↘
    [Sentinel]   [Ryse]
```
- Agentes como boxes | Setas clicáveis
- Cores: Verde (ativo) | Amarelo (aviso) | Vermelho (erro)

### **DIREITA - Editor de Handoff**:
Ao clicar em uma seta:
- Nome (text)
- Status (toggle)
- **Contrato de Dados**:
  - Input Schema (JSON editor)
  - Output Schema (JSON editor)
- **Validação**:
  - Requires Validation (toggle)
  - Custom Rules (JSON, opcional)
- **Tratamento de Erro**:
  - On Error Action (select: Retry | Fallback | Alert | Abort)
  - Fallback Agent (select, visível se Fallback)
  - Max Retries (input, default 2)
- **Transformação**:
  - Transform Function (select: None | Auto-map | Custom)
- **Metadados**:
  - Sequence Order (input)
  - Is Parallel (toggle)
  - Parallel With (select)
- Botões: [Salvar] [Testar Contrato] [Deletar]

**Botões Globais**: "+ Novo Handoff" | "Validar Todos os Contratos" | "Exportar Mapa"

***

## **TELA 4: GERENCIADOR DE PIPELINES**

**Layout**: Coluna esquerda (lista) + Coluna direita (editor)

### **ESQUERDA - Lista de Pipelines**:
- Busca | Filtros
- Cards: Nome | Agentes | Modo | Status
- "+ Novo Pipeline"

### **DIREITA - Editor de Pipeline**:
- Nome (text)
- Descrição (textarea)
- **Configuração**:
  - Execution Mode (radio: Sequential | Parallel | Mixed)
  - Parallel Groups (se Mixed)
  - Handoff Sequence (drag-drop list ou visual)
- **Tratamento de Erro Global**:
  - Strategy (select: Fail Fast | Continue with Fallback | Manual Intervention)
- **Input Data** (JSON editor para dados iniciais)
- Botões: [Salvar] [Testar Pipeline] [Executar] [Deletar]

***

## **TELA 5: ACOMPANHAMENTO DE EXECUÇÃO** ⭐ (PRINCIPAL)

**Layout**: Fluxograma vertical com progresso

```
┌────────────────────────────────────────┐
│ POC: StartUp XYZ - Execução em Andamento
├────────────────────────────────────────┤
│                                          │
│  [1] ✓ Spectrum   Concluído (3.2s, $0.15)
│      ↓ (dados passando)                  │
│  [2] ✓ Prism      Concluído (2.1s, $0.10)
│      ↓                                    │
│  [3] ⏳ Schema     Executando... (1.8s)  │
│      ↓                                    │
│  [4] ⏱ Synapse    Aguardando...        │
│      ↓                                    │
│  [5] ⏱ Sentinel   Aguardando...        │
│      ↓                                    │
│  [6] ⏱ Ryse       Aguardando...        │
│                                          │
├────────────────────────────────────────┤
│ CONTEXTO COMPARTILHADO:                  │
│ variables: {client_name, budget, ...}   │
│ artifacts: {spec.md, skeleton/, ...}    │
│ Total: $2.15 | 45s decorridos           │
└────────────────────────────────────────┘
```

**Componentes**:
- Título com status overall
- Fluxograma vertical com cada agente como card:
  - Ícone status (✓ | ⏳ | ⏱ | ⚠️ | ❌)
  - Nome do agente
  - Status descritivo
  - Tempo decorrido
  - Custo parcial
  - [Detalhes] (expande para ver input/output)
- Seta de transição entre agentes (animada se passando dados)
- **Painel de Contexto Compartilhado**:
  - Abas: Variables | State | Artifacts
  - JSON view estruturado
  - Atualização em tempo real
- **Controles**:
  - Pausar | Retomar | Cancelar
  - Velocidade de atualização (real-time | 1s | 5s)
- **Resumo no Rodapé**:
  - Total de custo até agora
  - Tempo total
  - Progresso (X de 6 agentes)

***

## **TELA 6: TESTE DE AGENTE**

**Layout**: Esquerda (Input) | Direita (Output em abas)

### **ESQUERDA**:
- Seletor de agente (dropdown)
- Campo de input (textarea ou code editor)
- Variáveis adicionais (key-value table)
- Botão "Executar Teste"

### **DIREITA - Output em Abas**:
- **Aba "Resultado"**: Resposta formatada
- **Aba "Pensamentos"**: Step-by-step (intermediate_steps)
- **Aba "Logs"**: Output bruto + logs
- **Aba "Métricas"**: Tempo | Tokens | Iterações | Custo estimado

**Botões**: Executar Novamente | Copiar Resultado | Baixar Logs | Enviar Feedback

***

## **TELA 7: COMPARADOR A/B**

**Layout**: Tela horizontal 50/50

- Selectors: Agente A | Agente B
- Input Comum (campo para prompt/contexto)
- Botão "Comparar"
- Resultado lado a lado com highlighting de diferenças
- Métricas comparadas (tempo, tokens, custo)

***

## **TELA 8: CONFIGURAÇÕES GLOBAIS**

**Seções**:
- Conexão Backend (URL Supabase, API key, Status)
- Modelos (OpenAI/Anthropic API keys, Modelos disponíveis)
- Preferências (Tema Light/Dark, Idioma, Timezone)
- Integrações (LangSmith, Custom webhooks)

***

## **DESIGN E UX**

**Cores**: 
- Primária: Azul/Indigo
- Sucesso: Verde
- Aviso: Amarelo/Laranja
- Erro: Vermelho
- Info: Azul claro

**Componentes**:
- Cards com sombra e hover
- Buttons (primário, secundário, danger, text-only)
- Badges para status/tipos
- Modal para confirmações
- Toast notificações
- Spinner para loading
- Tabs navegáveis

**Responsividade**: Desktop only

***

## **DADOS DE EXEMPLO (PRÉ-CARREGADO)**

Um agente exemplo: `schema_validator` (hybrid) com todos os campos preenchidos conforme documentação Ryse v3.0

***
