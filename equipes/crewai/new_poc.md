## Passo a passo 2 – Aplicar o modelo da “linha de montagem”

A ideia agora é sempre pegar esse padrão de 4 arquivos e adaptar só os YAMLs para cada POC.[6][7]

Dentro da pasta do projeto recém-criado (`meu-poc-agentes`):

1. Ajustar `agents.yaml` para a equipe padrão  
   ```bash
   cat > src/meu_poc_agentes/config/agents.yaml << 'EOF'
   spectrum:
     role: >
       Scope Designer e Requirements Architect
     goal: >
       Transformar o briefing do cliente em uma especificação técnica clara,
       estruturada e acionável para uma POC orientada a código.
     backstory: >
       Você é um arquiteto de requisitos especializado em transformar pedidos vagos
       em especificações técnicas completas. Sempre devolve uma visão clara de escopo,
       fluxos principais, entradas/saídas e restrições.

   prism:
     role: >
       Skeleton Generator e Core Architect
     goal: >
       A partir da especificação da POC, projetar a arquitetura base do projeto
       e gerar um skeleton completo de arquivos, módulos e pontos de extensão.
     backstory: >
       Você é um arquiteto de software focado em clean architecture. Gera a estrutura
       mínima de código necessária para viabilizar a POC, com TODOs claros indicando
       o que ainda deve ser detalhado depois.

   builder_guardian:
     role: >
       Implementation, Orchestration and Review Architect
     goal: >
       Transformar o skeleton e a especificação em código executável, definindo
       contratos de dados, orquestração e realizando uma revisão básica de robustez.
     backstory: >
       Você combina o papel de designer de contratos de dados, orquestrador de fluxo
       e revisor de código. A partir do skeleton e da especificação, entrega uma
       primeira versão funcional do projeto com foco em clareza e consistência.

   github_deployer:
     role: >
       GitHub Repository Deployer
     goal: >
       Gerar um plano claro para criar ou atualizar um repositório GitHub com o
       projeto resultante, incluindo comandos git e sugestão de estrutura.
     backstory: >
       Você é um especialista em versionamento e GitHub. Sempre devolve instruções
       passo-a-passo para inicializar o repositório local, conectar ao GitHub e
       fazer o primeiro push, usando boas práticas de organização.
   EOF
   ```

2. Ajustar `tasks.yaml` com o fluxo padrão + FileWriterTool  
   ```bash
   cat > src/meu_poc_agentes/config/tasks.yaml << 'EOF'
   spectrum_task:
     description: >
       A partir do briefing do cliente, gere uma especificação técnica estruturada
       para uma POC orientada a código, no contexto de uma linha de montagem de
       agentes de IA. Descreva claramente:
       - objetivo da projeto/POC
       - escopo (o que entra e o que fica fora)
       - principais fluxos de trabalho e decisões
       - entradas e saídas esperadas em cada etapa
       - constraints técnicas relevantes.
       No final, entregue o conteúdo completo do documento.
     expected_output: >
       Um documento em Markdown chamado `especificacao_poc.md` com seções claras
       e numeradas, pronto para ser usado como base de implementação.
     agent: spectrum
     output_file: especificacao_poc.md

   prism_task:
     description: >
       Usando o conteúdo de `especificacao_poc.md`, projete o skeleton do projeto
       que implementará essa linha de montagem de agentes usando CrewAI.
       Defina:
       - estrutura de pastas e arquivos principais
       - onde ficarão os agentes, tasks e configuração
       - pontos de extensão e TODOs.
       Não escreva o código completo ainda, apenas descreva a estrutura e
       forneça exemplos mínimos de cada arquivo quando necessário.
       No final, entregue o conteúdo completo do documento.
     expected_output: >
       Um documento em Markdown chamado `skeleton_projeto.md` descrevendo a estrutura
       de diretórios/arquivos e um esboço do conteúdo mínimo de cada arquivo.
     agent: prism
     output_file: skeleton_projeto.md

   implementation_task:
     description: >
       A partir de `especificacao_poc.md` e `skeleton_projeto.md`, gere a primeira
       versão funcional do projeto em CrewAI, focando no mínimo necessário para
       rodar o fluxo completo dos agentes. Concentre-se em:
       - definir os agentes e tasks em YAML (agents.yaml / tasks.yaml)
       - implementar um crew com Process.sequential
       - criar um main.py que recebe o briefing e executa o crew.
       Use TODOs nos pontos onde detalhes avançados (contratos rígidos, validações,
       observabilidade) serão adicionados em versões futuras.
       IMPORTANTE: ao final, use a ferramenta de escrita de arquivo (FileWriterTool)
       para salvar TODO o conteúdo que você gerou para esta etapa em um único
       arquivo Markdown chamado `implementation_output.md` dentro do diretório
       `outputs`.
       Use a ferramenta passando:
       - filename: "implementation_output.md"
       - content: o conteúdo completo que você gerou
       - directory: "outputs".
     expected_output: >
       Confirmação de que o arquivo `outputs/implementation_output.md` foi criado,
       seguida de um breve resumo do que foi escrito.
     agent: builder_guardian

   github_deploy_task:
     description: >
       Considere que o código gerado na etapa anterior foi salvo localmente na
       máquina do desenvolvedor. Gere um plano detalhado para criar um repositório
       no GitHub e fazer o primeiro push desse projeto. Inclua:
       - sugestão de nome de repositório
       - estrutura de diretórios esperada
       - comandos git passo-a-passo (git init, git remote add origin, git add,
         git commit, git push)
       - recomendações de arquivos para .gitignore.
       IMPORTANTE: ao final, use a ferramenta de escrita de arquivo (FileWriterTool)
       para salvar o guia em um arquivo chamado `github_deploy.md` dentro do
       diretório `outputs`.
       Use a ferramenta passando:
       - filename: "github_deploy.md"
       - content: o guia completo em Markdown
       - directory: "outputs".
     expected_output: >
       Confirmação de que o arquivo `outputs/github_deploy.md` foi criado,
       seguida de um breve resumo do conteúdo.
     agent: github_deployer
   EOF
   ```

3. Substituir `crew.py` pelo modelo da linha de montagem  
   ```bash
   cat > src/meu_poc_agentes/crew.py << 'EOF'
   from typing import List
   from crewai import Agent, Crew, Process, Task, LLM
   from crewai.project import CrewBase, agent, crew, task
   from crewai_tools import FileWriterTool
   import os


   @CrewBase
   class MeuPocAgentesCrew:
       """Crew padrão de linha de montagem para POCs"""

       agents_config = "config/agents.yaml"
       tasks_config = "config/tasks.yaml"

       def __init__(self):
           self.llm = LLM(
               model="gemini/gemini-flash-latest",
               api_key=os.getenv("GOOGLE_API_KEY"),
           )
           self.file_writer = FileWriterTool()

       @agent
       def spectrum(self) -> Agent:
           return Agent(
               config=self.agents_config["spectrum"],
               llm=self.llm,
               verbose=True,
           )

       @agent
       def prism(self) -> Agent:
           return Agent(
               config=self.agents_config["prism"],
               llm=self.llm,
               verbose=True,
           )

       @agent
       def builder_guardian(self) -> Agent:
           return Agent(
               config=self.agents_config["builder_guardian"],
               llm=self.llm,
               verbose=True,
               tools=[self.file_writer],
           )

       @agent
       def github_deployer(self) -> Agent:
           return Agent(
               config=self.agents_config["github_deployer"],
               llm=self.llm,
               verbose=True,
               tools=[self.file_writer],
           )

       @task
       def spectrum_task(self) -> Task:
           return Task(config=self.tasks_config["spectrum_task"])

       @task
       def prism_task(self) -> Task:
           return Task(config=self.tasks_config["prism_task"])

       @task
       def implementation_task(self) -> Task:
           return Task(config=self.tasks_config["implementation_task"])

       @task
       def github_deploy_task(self) -> Task:
           return Task(config=self.tasks_config["github_deploy_task"])

       @crew
       def crew(self) -> Crew:
           return Crew(
               agents=self.agents,
               tasks=self.tasks,
               process=Process.sequential,
               verbose=True,
           )
   EOF
   ```

4. Ajustar `main.py` para usar a nova classe  
   ```bash
   cat > src/meu_poc_agentes/main.py << 'EOF'
   #!/usr/bin/env python
   from meu_poc_agentes.crew import MeuPocAgentesCrew


   def run():
       """
       Executa o crew padrão de linha de montagem de POC.
       """
       briefing = input("Digite o briefing da POC: ")

       inputs = {
           "briefing": briefing,
       }

       MeuPocAgentesCrew().crew().kickoff(inputs=inputs)


   if __name__ == "__main__":
       run()
   EOF
   ```

5. Rodar a nova POC  
   ```bash
   source .venv/bin/activate   # se ainda não estiver
   export GOOGLE_API_KEY=SEU_TOKEN_GEMINI_AQUI
   crewai run
   ```

Depois da execução, você terá:

- `especificacao_poc.md` e `skeleton_projeto.md` na raiz.  
- `outputs/implementation_output.md` e `outputs/github_deploy.md` com código e guia de deploy.  

***

Com isso, para **qualquer novo POC** você só precisa:

- Rodar o passo a passo 1 para criar o projeto.  
- Rodar o passo a passo 2 ou, melhor ainda, manter esses quatro arquivos como “template” (até num repo seu) e só mandar o assistente gerar novas versões de `agents.yaml`, `tasks.yaml`, `crew.py` e `main.py` adaptadas ao novo contexto.[7][8]

[1](https://docs.crewai.com/en/quickstart)
[2](https://github.com/crewAIInc/crewAI)
[3](https://pypi.org/project/crewai/)
[4](https://github.com/crewAIInc/crewAI/issues/1759)
[5](https://docs.crewai.com)
[6](https://help.crewai.com/how-to-build-a-crew-for-crewai)
[7](https://deepwiki.com/crewAIInc/crewAI/9.3-configuration-patterns)
[8](https://blog.crewai.com/getting-started-with-crewai-build-your-first-crew/)
[9](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/64846027/28e2b9d2-104e-4259-8b96-d0eafef1a8f1/image.jpg)
[10](https://docs.crewai.com/en/installation)
[11](https://pypi.org/project/crewai/0.1.6/)
[12](https://www.youtube.com/watch?v=ZurSXWmo2yM)
[13](https://stackoverflow.com/questions/79678973/pip-installs-crewai-tools-successfully-but-package-is-empty-and-helpcrewai-to)
[14](https://crewai.mintlify.app/en/concepts/cli)
