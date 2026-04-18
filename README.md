🌱 EcoBot - Assistente de Sustentabilidade (Com Interface Gráfica)

Trabalho Acadêmico - 3ª Tarefa: Desenvolvimento de um Agente utilizando LLM

📖 Descrição do Projeto

O EcoBot é um agente conversacional desenvolvido em Python. Ele possui uma interface gráfica moderna e atua como um assistente educacional exclusivo sobre o tema de Sustentabilidade e Meio Ambiente.

Funcionalidades Implementadas:

✅ Interface Gráfica Profissional: Utiliza a biblioteca Streamlit para um visual limpo de chat.

✅ Integração com LLM: Utiliza a nova API Oficial do Google (google-genai) utilizando o modelo atualizado gemini-2.5-flash.

✅ Restrição de Domínio (Guardrails): O agente foi treinado via instrução de sistema (system_instruction) para recusar educadamente qualquer pergunta que não seja sobre sustentabilidade (ex: desporto, tecnologia, política).

✅ Manutenção de Contexto: O bot possui memória da conversa atual utilizando a sessão de chat nativa da SDK do Google.

✅ Segurança de Credenciais: As chaves de API são geridas de forma segura através de variáveis de ambiente (ficheiro .env).

💻 Tecnologias Utilizadas

Linguagem: Python 3.8+

Biblioteca de Interface: streamlit (Framework web rápido para dados/IA)

Biblioteca LLM: google-genai (Nova SDK Oficial do Google)

Variáveis de Ambiente: python-dotenv

Modelo: Gemini 2.5 Flash

🚀 Instruções de Execução

Siga os passos abaixo para rodar o projeto na sua máquina:

1. Obtenha a sua Chave de API Gratuita
Aceda ao Google AI Studio (https://aistudio.google.com/app/apikey), faça login com a sua conta do Google e clique em "Create API Key".

2. Clone o repositório ou extraia o ficheiro
Garanta que os ficheiros agente_ecobot.py, requirements.txt e .env estejam na mesma pasta.

3. Instale as dependências
Abra o terminal na pasta do projeto e execute a instalação (ou atualização) das bibliotecas:

pip install -r requirements.txt --upgrade


4. Configure a sua Chave de API com segurança
Abra o ficheiro .env com o seu editor de código e garanta que ele tem o seguinte formato (sem aspas):
GEMINI_API_KEY=sua_chave_secreta_aqui

5. Execute a Aplicação (IMPORTANTE)
No terminal, execute o comando do Streamlit:

streamlit run agente_ecobot.py


Um separador do seu navegador padrão abrir-se-á automaticamente com a interface linda do chatbot pronta a usar!

🎥 Demonstração em Vídeo

(Para os alunos: Insiram aqui o link do vídeo a demonstrar o agente)

Link do Vídeo: [Adicione o seu link aqui]

Nota de Segurança: O ficheiro .env não deve ser enviado para o GitHub. Se usar controlo de versões, lembre-se de criar um ficheiro .gitignore e adicionar .env lá dentro.