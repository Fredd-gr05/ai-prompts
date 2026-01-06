# POC Orchestrator - Multi-Agent Architecture Generation

> **Sistema de teste para os 5 agentes (Spectrum, Prism, Schema, Synapse, Sentinel)**
> **Nenhuma experiencia em programacao necessaria - apenas Python instalado!**

---

## Como Funciona (Em Termos Simples)

Imagine que voce quer construir um projeto. Em vez de fazer tudo manualmente, voce:

1. **Descreve o que quer** (ex: "quero uma API que processe tarefas com IA")
2. **Spectrum lê** sua descricao e cria um documento de especificacao
3. **Prism lê** o documento de Spectrum e gera a estrutura de pastas/arquivos
4. **Schema lê** o documento de Prism e adiciona definicoes de tipos
5. **Synapse lê** o documento de Schema e define como as partes se integram
6. **Sentinel lê** tudo e valida se esta 100% correto
7. **Resultado:** Um arquivo `orchestration_result.json` com toda a arquitetura pronta!

---

## Instalacao (5 Minutos)

### Passo 1: Instalar Python 3.10+
Descarregue em: https://www.python.org/downloads/

**Windows:** Marque "Add Python to PATH" durante instalacao

### Passo 2: Abrir Terminal/Prompt

**Windows:** Press `Win + R`, type `cmd`, press Enter
**Mac:** Press `Cmd + Space`, type `terminal`, press Enter
**Linux:** Ctrl + Alt + T

### Passo 3: Clonar o Repositorio

```bash
git clone https://github.com/Fredd-gr05/ai-prompts.git
cd ai-prompts/equipes/pco-ai_v10.2/poc_orchestrator
```

---

## Rodar o POC (3 Segundos)

### Comando:

```bash
python main_orchestrator.py
```

### O que vai acontecer:

```
######################################################################
# MULTI-AGENT ORCHESTRATOR POC
# Spectrum -> Prism -> Schema -> Synapse -> Sentinel
######################################################################

Requisitos: Criar sistema de gerenciamento de tarefas com API REST...

======================================================================
SPECTRUM: Analisando requisitos...
======================================================================
OK Specification criada: Multi-Agent System POC

======================================================================
PRISM: Gerando arquitetura base...
======================================================================
OK Arquitetura gerada com 5 arquivos

======================================================================
SCHEMA: Adicionando tipos e contratos...
======================================================================
OK Tipos e contratos adicionados

======================================================================
SYNAPSE: Validando fluxos de integracao...
======================================================================
OK Fluxos de integracao validados

======================================================================
SENTINEL: Executando QA final...
======================================================================
OK QA final passou

======================================================================
RESULTADO FINAL
======================================================================
Status: APPROVED - READY_FOR_DEPLOYMENT
Arquivos: 5

OK Resultado salvo em: orchestration_result.json
```

---

## Ver o Resultado

Apos executar, abra o arquivo `orchestration_result.json` com um editor de texto (Notepad, VS Code, etc):

```bash
# No Windows:
start orchestration_result.json

# No Mac:
open orchestration_result.json

# No Linux:
cat orchestration_result.json
```

Voce vera algo como:

```json
{
  "status": "APPROVED - READY_FOR_DEPLOYMENT",
  "project_name": "Multi-Agent System POC",
  "files": [
    {"path": "src/main.py", "type": "entry_point"},
    {"path": "src/config/settings.py", "type": "config"},
    {"path": "src/api/routes.py", "type": "api"},
    {"path": "src/agents/manager.py", "type": "agent"},
    {"path": "requirements.txt", "type": "dependencies"}
  ]
}
```

---

## Testar Com Seus Requisitos

Edite o arquivo `main_orchestrator.py` na ultima linha:

**Antes (padrao):**
```python
user_requirements = "Criar sistema de gerenciamento de tarefas com API REST, agentes IA, BD e cache"
```

**Depois (seu requisito):**
```python
user_requirements = "Quero um sistema de recomendacao de filmes com integracao com Netflix"
```

E rode novamente:
```bash
python main_orchestrator.py
```

---

## O Que Esta Acontecendo?

1. **Spectrum** = Le requisitos, cria especificacao
2. **Prism** = Le especificacao, cria design (quais arquivos precisa)
3. **Schema** = Le design, adiciona tipos de dados
4. **Synapse** = Le tudo, valida integracao entre partes
5. **Sentinel** = Le tudo, faz QA final, libera para producao

Cada um **transforma o documento anterior**, enriquecendo com mais informacao!

---

## Proximos Passos

### Com LLM Real (ChatGPT/Claude):

Em um proximo passo, voce pode:

1. Conectar a um LLM real (OpenAI, Claude, etc)
2. Cada agente chamaria o LLM em vez de simular
3. Receberia resposta mais inteligente de cada agente
4. BUILD.sh seria gerado automaticamente

### Atualmente:
Este POC **simula** os agentes para voce testar o fluxo sem depender de API externa.

---

## Problemas Comuns

### "python: command not found"
**Solucao:** Python nao esta instalado ou nao foi adicionado ao PATH. Reinstale marcando "Add Python to PATH".

### "FileNotFoundError: main_orchestrator.py"
**Solucao:** Certifique-se de estar na pasta correta. Execute `ls` ou `dir` para ver os arquivos.

### Nenhum arquivo foi criado
**Solucao:** Ele cria `orchestration_result.json` na mesma pasta. Procure na pasta onde rodou o comando.

---

## Estrutura do Projeto

```
poc_orchestrator/
├── main_orchestrator.py      # Script principal (o que voce roda)
├── README.md                  # Este arquivo
└── orchestration_result.json  # Criado automaticamente
```

---

## Documentacao dos Agentes

Cada agente esta totalmente documentado em:

```
../prompts_agentes/
├── 01_spectrum_requisitos_especificacao.md
├── 02_prism_gerador_arquitetura.md
├── 03_schema_designer_contratos.md
├── 04_synapse_orquestrador_fluxos.md
└── 05_sentinel_validador_qa_buildsh.md
```

Voce pode ler esses arquivos para entender exatamente o que cada agente faz.

---

## Suporte

Este e um POC para **demonstrar o conceito**. Se tiver duvidas:

1. Leia os arquivos de prompt (muito bem documentados)
2. Execute o script e veja o resultado
3. Modifique `user_requirements` e teste com seus proprios requisitos

**Boa sorte! Este e o primeiro passo para automatizar arquitetura de software com IA!** 🚀
