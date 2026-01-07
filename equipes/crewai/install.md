
## Passo a passo 1 – Setup inicial e criação da POC

Use sempre um diretório “pai” onde você guarda seus projetos de agentes.

1. Entrar na pasta base onde quer criar a POC  
   ```bash
   cd /caminho/para/seus_projetos
   ```

2. (Opcional, mas recomendável) criar e ativar venv para o novo projeto  
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```

3. Instalar CrewAI com tools  
   ```bash
   pip install "crewai[tools]"
   ```
   Isso instala framework + ferramentas padrão (incluindo file tools).[3][4]

4. Verificar versões de Python e CrewAI  
   ```bash
   python -V
   pip show crewai | grep Version
   ```

5. Criar um novo projeto CrewAI para a POC  
   ```bash
   crewai create crew meu-poc-agentes
   ```
   Isso gera a estrutura: `meu-poc-agentes/src/meu_poc_agentes/{config,crew.py,main.py,...}`.[2][1]

6. Entrar na pasta da POC  
   ```bash
   cd meu-poc-agentes
   ```

7. Criar `.env` com a chave do Gemini (LLM grátis)  
   ```bash
   cat > .env << 'EOF'
   GOOGLE_API_KEY=SEU_TOKEN_GEMINI_AQUI
   EOF
   ```
   (substitua pela sua chave real).[5]

Até aqui, o framework está instalado e o esqueleto base do projeto foi criado.

***


[15](https://www.scribd.com/document/841532683/CrewAi-docs-25-2-25)
[16](https://www.reddit.com/r/crewai/comments/1hrb4li/how_do_i_install_this_on_my_laptop/)
[17](https://deepwiki.com/lymanzhang/crewAI/5.1-cli-commands-reference)
[18](https://deepwiki.com/crewAIInc/crewAI/10.2-yaml-configuration)
[19](https://github.com/crewAIInc/crewAI/issues/1687)
[20](https://www.youtube.com/watch?v=VwC-fUpVLYY)
[21](https://www.piwheels.org/project/crewai-tools/)
