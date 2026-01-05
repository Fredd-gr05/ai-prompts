# Especificação POC - Equipe de Consultoria Estratégica Data-Driven

## Visão Geral da POC

A POC (Proof of Concept) da equipe de Consultoria Estratégica Data-Driven tem como objetivo demonstrar um **pipeline mínimo e completo** que leva a empresa "da imersão ao plano executivo", focando em estratégia consultiva e não em complexidade de engenharia de dados.

### O que a POC prova:
- Utilidade de uma "linha de montagem consultiva" com agentes bem definidos e orquestrados
- Padronização de templates e artefatos para o fluxo estratégico
- Capacidade de raciocínio integrado entre agentes da camada de imersão, núcleo e consolidação
- Prototipagem rápida de diagnósticos e planos executivos estruturados

### O que a POC NÃO prova (v1):
- Data warehouse multi-tenant ou pipelines ETL avançados
- Geração de dashboards interativos em tempo real
- Implementação de KPIs data-driven em código de produção
- Variabilidade setorial ou especialistas setoriais (Titan, Trade, Serve, Spark)
- Fases avançadas como pivotagem estratégica (Surge, Pivot) ou forecasting

---

## Agentes Incluídos na POC

### Camada Foundation (Entrada Obrigatória)

#### **Theron** - Imersão e Contexto
- **Papel**: Primeira porta de entrada consultiva
- **Inputs**: Briefing livre do cliente, documentos contextuais
- **Outputs**: Relatório de Imersão v0 (visão, contexto, objetivos, desafios priorizados)
- **Interação**: Realiza entrevista semiestruturada com o cliente para capturar intenções estratégicas

#### **Lyric** - Diagnóstico Preliminar
- **Papel**: Síntese diagnóstica da situação
- **Inputs**: Relatório de Imersão, documentos disponíveis do cliente
- **Outputs**: Pacote Diagnóstico v0 (áreas críticas, insights, hipóteses a validar)
- **Interação**: Consolida dados fornecidos e recomenda eixos de análise

#### **Stratos** - Orquestrador POC
- **Papel**: Gerencia fluxo padrão e sequenciamento
- **Inputs**: Relatório de Imersão + Pacote Diagnóstico
- **Outputs**: Roadmap POC Único (sequência determinística dos agentes)
- **Configuração**: Em v1, usa um **fluxo fixo padronizado** sem ramificações complexas

### Camada Core (Análise Estratégica)

#### **Nexis** - Modelo de Negócio (Canvas)
- **Papel**: Estruturação do Business Model Canvas
- **Inputs**: Pacote Diagnóstico v0
- **Outputs**: Canvas v0 (segmentos, proposta de valor, receitas, custos, etc.)
- **Documentação**: Seções obrigatórias em markdown com campos estruturados

#### **Scout** - Mercado e Personas
- **Papel**: Análise de mercado, personas e oportunidades
- **Inputs**: Pacote Diagnóstico v0
- **Outputs**:
  - Personas v0 (perfil, dores, objetivos)
  - Análise de Mercado v0 (tamanho, tendências, concorrentes)
  - Mapa de Oportunidades SEBRAE v0 (Indivíduo, Mercado, Negócio)
- **Paralelo**: Executa em paralelo com Nexis

#### **Shield** - Gestão de Riscos
- **Papel**: Identificação e análise de riscos e SWOT
- **Inputs**: Pacote Diagnóstico v0 + Canvas v0 + Análise de Mercado v0
- **Outputs**:
  - SWOT v0 (Forças, Fraquezas, Oportunidades, Ameaças)
  - Matriz de Riscos v0 (Probabilidade, Impacto, Nível, Ações de Mitigação)

### Camada Consolidação

#### **Synthesis** - Integração Diagnóstica
- **Papel**: Consolida todos os documentos em um pacote estratégico
- **Inputs**: Todos os outputs das camadas anteriores
- **Outputs**: Pacote Consolidado Estratégico v0
- **Função**: Cruza Canvas, Mercado, Personas, SWOT e Riscos em narrativa coerente

### Camada Output

#### **Scribe** - Documentação Executiva
- **Papel**: Gera Plano Executivo POC em markdown estruturado
- **Inputs**: Pacote Consolidado Estratégico v0
- **Outputs**: Plano Executivo POC v0
- **Seções**: Sumário Executivo, Contexto/Diagnóstico, Modelo de Negócio, Mercado, SWOT, Riscos, Plano de Ação 12 Meses, Próximos Passos

---

## Fluxo Único da POC

```
Theron (Imersão)
    ↓
Lyric (Diagnóstico)
    ↓
Stratos (Orquestração → Roadmap POC Fixo)
    ↓
┌─→ Nexis (Canvas) ─────┐
│                        ├─→ Shield (SWOT + Riscos)
└─→ Scout (Mercado/Personas) ┘
    ↓
Synthesis (Consolidação)
    ↓
Scribe (Plano Executivo POC v0)
```

### Pontos-Chave do Fluxo:

1. **Entrada obrigatória**: Theron → Lyric. Sem este pipeline inicial, Stratos não ativa.
2. **Paralelismo**: Nexis e Scout rodam em paralelo após Stratos.
3. **Serialidade crítica**: Shield aguarda outputs de Nexis + Scout antes de gerar SWOT/Riscos.
4. **Consolidação única**: Synthesis integra todas as análises; não há bifurcação.
5. **Saída padronizada**: Scribe gera documento final em markdown com seções obrigatórias.

---

## Contratos v0 de Documentos

Cada artefato segue um contrato de seções mínimas obrigatórias em Markdown:

### **Relatório de Imersão v0**
- Contexto do Negócio
- Objetivos Estratégicos
- Fase do Negócio
- Setor / Segmento
- Desafios Priorizados
- Expectativas do Cliente

### **Pacote Diagnóstico v0**
- Resumo Executivo
- Diagnóstico por Área
- Insights Críticos
- Dados/Documentos Disponíveis
- Hipóteses a Validar

### **Canvas v0**
- Segmentos de Clientes
- Proposta de Valor
- Canais
- Relacionamento com Clientes
- Fontes de Receita
- Recursos-Chave
- Atividades-Chave
- Parcerias-Chave
- Estrutura de Custos

### **Personas v0**
- Lista de Personas
- Perfil Demográfico
- Dor Principal
- Objetivos
- Comportamento de Compra

### **Análise de Mercado v0**
- Tamanho de Mercado (Estimado)
- Tendências Relevantes
- Concorrentes Principais
- Posicionamento Sugerido

### **Mapa de Oportunidades SEBRAE v0**
- Indivíduo (Pessoa Física)
- Mercado (Contexto Externo)
- Negócio (Proposta Interna)
- Síntese de Oportunidades

### **SWOT v0**
- Forças
- Fraquezas
- Oportunidades
- Ameaças

### **Matriz de Riscos v0**
- Lista de Riscos
- Classificação: Probabilidade (Baixa/Média/Alta)
- Classificação: Impacto (Baixo/Médio/Alto)
- Nível de Risco (Baixo/Médio/Alto)
- Ações de Mitigação

### **Pacote Consolidado Estratégico v0**
- Resumo Executivo Integrado
- Síntese do Diagnóstico
- Proposta Estratégica (Canvas + Mercado)
- Prioridades de Ação
- Indicadores de Sucesso (Qualitativos)

### **Plano Executivo POC v0**
- Sumário Executivo
- Contexto e Diagnóstico
- Modelo de Negócio
- Mercado e Personas
- Análise SWOT e Riscos
- Plano de Ação 12 Meses
- Próximos Passos da Consultoria

---

## Escopo Técnico (v1)

### Incluído:
- Orquestração de fluxo linear (Stratos com roadmap fixo)
- Templates markdown com seções obrigatórias
- Handoff entre agentes via JSON (inputs/outputs)
- Prototipagem rápida com LLMs (prompts otimizados)

### Excluído (para Fase 2+):
- Camada 2.5 (Metra, Nexar, Cypher, Visor, Warden, Oracle)
- Especialistas setoriais ou segmentados
- Geração de código ou pipelines ETL
- Dashboards ou visualizações interativas
- Multi-tenancy ou isolamento de dados
- KPIs automatizados ou ML avançado

---

## Próximos Passos

1. Validar contrato JSON (especificacao_poc.json) com Prism/Schema/Synapse
2. Implementar prompts otimizados para cada agente
3. Testar fluxo com caso de uso piloto (startup ou PME)
4. Coletar feedback e iterar templates
5. Documentar lições aprendidas para Fase 2
