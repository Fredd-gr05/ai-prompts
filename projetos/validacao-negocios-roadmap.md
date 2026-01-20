# Roadmap - Sistema de Validação de Negócios

**Projeto:** Assistente de IA para Validação e Estruturação de Novos Negócios  
**Versão:** 1.0 - Etapa 1 (Discovery e Roadmap)  
**Data:** 20 de Janeiro de 2026  
**Autor:** Fred Garcia

---

## 📋 Visão Geral do Projeto

Sistema de validação progressiva de ideias de negócio através de questionamento adaptativo estruturado em 5 etapas, culminando na geração automática de plano de negócios e resumo executivo.

### Objetivo
Guiar empreendedores desde a ideação até um plano de negócios estruturado, validando premissas de mercado, viabilidade e fit produto-mercado através de perguntas estratégicas e progressivas.

### Arquitetura Proposta (Etapa 1)
**Assistente Único** com fluxo conversacional adaptativo em 5 etapas sequenciais.

---

## 🎯 Fluxo Completo das 5 Etapas

```
INÍCIO → Etapa 1 (5Q) → Etapa 2 (3Q) → Etapa 3 (3Q) → Etapa 4 (3Q) → Etapa 5 (2Q) → OUTPUTS
         Discovery      Problema       Mercado        Viabilidade    MVP          Plano + Resumo
```

---

## 📊 ETAPA 1: Discovery Inicial (5 perguntas)

**Objetivo:** Mapear ideia básica, perfil do empreendedor e recursos disponíveis

### Perguntas

**P1.1 - Propósito do Negócio**  
*"Em uma frase: qual problema seu negócio resolve ou qual necessidade atende?"*

**Exemplo:**
> "Pequenos restaurantes perdem 30% das vendas porque não conseguem aceitar pagamentos digitais facilmente."

---

**P1.2 - Público-Alvo Inicial**  
*"Para quem exatamente é essa solução? (Seja específico: segmento, tamanho, localização)"*

**Exemplo:**
> "Restaurantes e lanchonetes com 1-5 funcionários em cidades do interior de SP (50-200mil habitantes)."

---

**P1.3 - Solução Oferecida**  
*"O que você vai oferecer para resolver isso? (Produto/serviço/plataforma?)"*

**Exemplo:**
> "App mobile que transforma qualquer smartphone em máquina de cartão, com taxa menor que as tradicionais."

---

**P1.4 - Motivação e Experiência Pessoal** ⭐ NOVA  
*"Por que VOCÊ quer fazer isso? Qual sua experiência ou conexão com esse problema?"*

**Exemplo:**
> "Trabalhei 5 anos em fintech e vejo minha família com restaurante perdendo clientes que só têm cartão."

---

**P1.5 - Recursos Disponíveis** ⭐ NOVA  
*"Quanto tempo e dinheiro você pode investir nos próximos 6 meses sem comprometer suas obrigações?"*

**Exemplo:**
> "Posso dedicar 20h/semana (tenho emprego atual) e investir R$ 15mil de economia pessoal."

---

## 🔍 ETAPA 2: Problema e Dor (3 perguntas)

**Objetivo:** Validar intensidade do problema e comportamento atual do cliente

**P2.1 - Intensidade da Dor**  
*"Quando um [público da P1.2] enfrenta [problema da P1.1], qual é o impacto real? (financeiro, tempo, frustração)"*

**Exemplo:**
> "Ticket médio R$ 45, acontece 8-12x/dia. Perda mensal de R$ 10-16mil + cliente insatisfeito."

---

**P2.2 - Alternativas Atuais**  
*"Como seu [público da P1.2] resolve/contorna esse problema hoje? O que usam?"*

**Exemplo:**
> "Têm maquininha tradicional (taxa 3-5% + R$ 50-90/mês) ou pedem Pix, ou perdem a venda."

---

**P2.3 - Frequência e Contexto**  
*"Com que frequência esse problema acontece? Em que situações específicas é mais crítico?"*

**Exemplo:**
> "Diariamente, pior nos finais de semana (60% vendas). Crítico em delivery e almoço executivo."

---

## 💰 ETAPA 3: Viabilidade de Mercado (3 perguntas)

**Objetivo:** Entender disposição para pagar e canais de aquisição

**P3.1 - Disposição para Pagar**  
*"Quanto seu [público] estaria disposto a pagar por [sua solução da P1.3]? Por que esse valor faz sentido?"*

**Exemplo:**
> "Taxa de 1,8-2,5% por transação (vs. 3-5% atual) sem aluguel fixo. Economizam R$ 600-1500/mês."

---

**P3.2 - Canais de Distribuição**  
*"Como você pretende alcançar e convencer esses clientes? Quais canais fazem sentido?"*

**Exemplo:**
> "Visita presencial, parcerias com associações, anúncios Facebook/Instagram geo-localizados."

---

**P3.3 - Tamanho de Mercado**  
*"Quantos clientes potenciais existem? Como você chegou nesse número?"*

**Exemplo:**
> "SP: ~180 cidades 50-200k hab, média 120 restaurantes/cidade = 21.600 estabelecimentos (TAM: ~20mil)."

---

## ⚙️ ETAPA 4: Feasibility e Competição (3 perguntas)

**Objetivo:** Mapear recursos necessários, vantagens competitivas e riscos

**P4.1 - Recursos-Chave Necessários**  
*"Para entregar [sua solução], o que você precisa ter/desenvolver?"*

**Exemplo:**
> "(1) App mobile iOS/Android, (2) credenciadora parceira (Stone/PagSeguro), (3) licença instituição de pagamento, (4) time: 1 dev mobile + 1 backend + suporte comercial."

---

**P4.2 - Vantagem Competitiva**  
*"Por que um cliente escolheria você em vez das alternativas que já existem?"*

**Exemplo:**
> "Taxa menor (1,8% vs 3-5%), sem aluguel, sem burocracia, onboarding 10min. Grandes (Cielo/Rede) têm processo lento e taxas altas."

---

**P4.3 - Barreiras e Riscos Principais**  
*"Quais os 3 maiores riscos que podem fazer isso não funcionar?"*

**Exemplo:**
> "1) Regulação BC mudando regras subcredenciadoras, 2) Guerra de preços, 3) Baixa adesão por desconfiança."

---

## 🚀 ETAPA 5: MVP e Validação (2 perguntas)

**Objetivo:** Definir escopo mínimo e estratégia de validação pré-construção

**P5.1 - Feature Mínima Indispensável**  
*"Se você tivesse que lançar com APENAS uma funcionalidade, qual seria?"*

**Exemplo:**
> "Processar pagamento por aproximação (NFC) débito/crédito e receber em 1 dia. Sem boleto, sem parcelamento, sem relatórios complexos na v1."

---

**P5.2 - Estratégia de Validação**  
*"Como você vai confirmar que clientes realmente querem/pagariam ANTES de desenvolver tudo?"*

**Exemplo:**
> "Landing page + anúncio Facebook em 3 cidades-piloto. Capturar emails + ligar para 50 interessados validando dor e preço. Meta: 20% conversão email→call e 50% aceitarem demonstração."

---

## 📄 OUTPUTS FINAIS (Gerados Automaticamente)

Após completar as 5 etapas, o assistente gera:

### Output 1: Resumo Executivo (1 página)
```
RESUMO EXECUTIVO - [Nome do Negócio]

PROBLEMA: [Síntese P1.1 + P2.1 + P2.3]
SOLUÇÃO: [P1.3 + P5.1]
MERCADO: [P1.2 + P3.3]
MODELO DE RECEITA: [P3.1]
VANTAGEM COMPETITIVA: [P4.2]
INVESTIMENTO NECESSÁRIO: [P1.5 + P4.1]
VALIDAÇÃO PREVISTA: [P5.2]
PRINCIPAIS RISCOS: [P4.3]
```

### Output 2: Plano de Negócios Estruturado
```
1. VISÃO GERAL DO NEGÓCIO [P1.1 a P1.5]
2. ANÁLISE DE MERCADO
   2.1 Problema e Dor do Cliente [P2.1 a P2.3]
   2.2 Tamanho de Mercado [P3.3]
   2.3 Competição e Alternativas [P2.2 + P4.2]
3. PRODUTO/SERVIÇO
   3.1 Descrição da Solução [P1.3]
   3.2 MVP e Roadmap [P5.1]
   3.3 Recursos Necessários [P4.1]
4. ESTRATÉGIA DE GO-TO-MARKET
   4.1 Precificação [P3.1]
   4.2 Canais de Distribuição [P3.2]
   4.3 Plano de Validação [P5.2]
5. VIABILIDADE E RISCOS
   5.1 Recursos Disponíveis [P1.5]
   5.2 Principais Riscos [P4.3]
   5.3 Mitigação [Sugerida pelo assistente]
6. PRÓXIMOS PASSOS (30-60-90 dias) [Gerado pelo assistente]
```

### Output 3: Business Model Canvas (Opcional)
Markdown formatado com os 9 blocos preenchidos

---

## 🔄 Fluxo de Interação (Exemplo Completo)

**Assistente:** "Vamos validar sua ideia de negócio em 5 etapas. Começando pelo básico - Em uma frase: qual problema seu negócio resolve?"

**Usuário:** "Pequenos restaurantes perdem 30% das vendas porque não conseguem aceitar pagamentos digitais facilmente."

**Assistente:** "Entendi. Para quem exatamente é essa solução?..."

*[Continua até P1.5]*

**Assistente:** "Ótimo! Agora vamos entender a profundidade do problema. Quando um pequeno restaurante perde uma venda por não aceitar cartão, qual é o impacto real?"

*[Continua progressivamente até P5.2]*

**Assistente:** "Excelente! Com base em todas as suas respostas, preparei:
1. ✅ Resumo Executivo (1 página)
2. ✅ Plano de Negócios Estruturado (6 seções)
3. ✅ Business Model Canvas
4. ✅ Checklist de Próximos Passos"

---

## 🎯 Próximas Etapas do Projeto

### Etapa 2: Desenvolvimento do Prompt
- [ ] Estruturar prompt completo do assistente único
- [ ] Definir lógica de adaptação de perguntas baseada em respostas
- [ ] Criar templates de outputs (Resumo Executivo, Plano de Negócios, Canvas)
- [ ] Documentar edge cases e variações de contexto

### Etapa 3: Testes e Validação
- [ ] Testar com 5 casos de uso diferentes
- [ ] Ajustar tom de comunicação para diferentes perfis de empreendedores
- [ ] Validar qualidade dos outputs gerados

### Etapa 4: Deployment
- [ ] Criar Perplexity Space
- [ ] Documentar instruções de uso
- [ ] Publicar no repositório ai-prompts

---

## 📚 Referências e Metodologias

- **Predict-Validate-Iterate Framework** (2026)
- **11 Dimensões de Validação:** Problem-Solution Fit, Target Market Clarity, Value Proposition Strength, Initial Feasibility, Market Entry Barriers, Resource Requirements, Timing, Personal Fit, MVP Viability, Competition, Market Readiness
- **Padrões Multi-Agente** (Google 2026): Sequential Pipeline, Router Pattern, Orchestrator-Workers

---

## 📊 Métricas de Sucesso

- Tempo médio de conclusão: 25-35 minutos
- Taxa de conclusão das 5 etapas: >80%
- Qualidade percebida dos outputs: >4/5
- Ação pós-validação (iniciar MVP, buscar validação adicional, pivotar): >70%

---

**Status:** ✅ Etapa 1 Concluída - Roadmap Estruturado  
**Próximo:** Desenvolvimento do Prompt Completo (Etapa 2)
