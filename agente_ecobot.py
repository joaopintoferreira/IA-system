import streamlit as st
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv


load_dotenv()

# =====================================================================
# 1. CONFIGURAÇÃO DA INTERFACE GRÁFICA 
# =====================================================================
st.set_page_config(page_title="EcoBot - Sustentabilidade", page_icon="🌱", layout="centered")

st.title("🌱 EcoBot")
st.caption("Seu assistente inteligente focado EXCLUSIVAMENTE em sustentabilidade e meio ambiente.")

# =====================================================================
# 2. CONFIGURAÇÃO DA API DO GEMINI E INSTRUÇÕES DO SISTEMA
# =====================================================================
CHAVE_API = os.getenv("GEMINI_API_KEY")

if not CHAVE_API or CHAVE_API == "sua_chave_aqui":
    st.warning("⚠️ ATENÇÃO: Por favor, verifique se o arquivo .env existe e contém a sua GEMINI_API_KEY.")
    st.stop()

instrucao_sistema = """Você é o EcoBot, um assistente amigável especialista APENAS em sustentabilidade, meio ambiente e práticas ecológicas. 

Mantenha as suas respostas sempre CURTAS, DIRETAS e RESUMIDAS (máximo de 2 a 3 parágrafos curtos ou em tópicos rápidos). Evite textos longos.

REGRA DE OURO (MUITO IMPORTANTE): Se o usuário perguntar sobre QUALQUER assunto fora desse escopo (como futebol, política, matemática, programação, culinária não-vegana, filmes, etc.), você DEVE recusar educadamente. 

EXEMPLO DE RECUSA: 'Poxa, sobre isso eu não sei falar! 😅 Meu foco é apenas em como cuidar do nosso planeta. Que tal me perguntar sobre energias renováveis?'"""

try:
    
    if "cliente_gemini" not in st.session_state:
        st.session_state.cliente_gemini = genai.Client(api_key=CHAVE_API)
except Exception as e:
    st.error(f"Erro ao configurar o cliente Gemini: {e}")
    st.stop()

# =====================================================================
# 3. MANUTENÇÃO DE CONTEXTO (MEMÓRIA)
# =====================================================================
if "chat" not in st.session_state:
    config = types.GenerateContentConfig(
        system_instruction=instrucao_sistema,
        temperature=0.3
    )
    st.session_state.chat = st.session_state.cliente_gemini.chats.create(
        model="gemini-2.5-flash",
        config=config
    )
    st.session_state.mensagens_tela = []

# =====================================================================
# 4. RENDERIZAR O HISTÓRICO NA TELA
# =====================================================================
for msg in st.session_state.mensagens_tela:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
# =====================================================================
# 5. ENTRADA DO USUÁRIO E RESPOSTA DA IA
# =====================================================================
entrada_usuario = st.chat_input("Faça uma pergunta sobre o meio ambiente...")

if entrada_usuario: 
    # Exibe e guarda a mensagem do usuário
    with st.chat_message("user"): 
        st.markdown(entrada_usuario) 
    st.session_state.mensagens_tela.append({"role": "user", "content": entrada_usuario})
    
    # Prepara o espaço para a resposta do bot
    with st.chat_message("assistant"):
        resposta_visual = st.empty()
        resposta_visual.markdown("Pensando... 🌱")
        
        try:
            # Envia a mensagem para a API e espera a resposta
            resposta_api = st.session_state.chat.send_message(entrada_usuario)
            texto_resposta = resposta_api.text 
            
            # Atualiza a tela com a resposta final
            resposta_visual.markdown(texto_resposta)
            st.session_state.mensagens_tela.append({"role": "assistant", "content": texto_resposta})
            
        except Exception as e:
            resposta_visual.error(f"Ocorreu um erro ao conectar com a IA: {e}")
            # Remove a mensagem com erro da tela para que o usuário possa tentar de novo
            st.session_state.mensagens_tela.pop()