import streamlit as st
from pysentimiento import create_analyzer

# Função para carregar o CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Função para realizar a análise de sentimentos
def analyze_sentiment(user_input):
    modelo_analise_sentimento = create_analyzer(task="sentiment", lang="pt")
    result = modelo_analise_sentimento.predict(user_input)
    label = result.output.capitalize()
    score = result.probas[result.output]
    
    return label, score

# Função principal da aplicação
def main():
    # Configuração da página
    st.set_page_config(page_title="Analisador de Sentimentos", layout="centered")

    # Carrega o tema escuro
    load_css('dark_theme.css')

    # Título e descrição
    st.title("Analisador de Sentimentos")
    st.write("Digite o texto abaixo para analisar o sentimento.")

    # Caixa de texto para entrada do usuário
    user_input = st.text_area("Texto para análise:", "")

    # Quando o usuário clica no botão "Analisar Sentimento"
    if st.button("Analisar Sentimento"):
        if user_input:
            # Realiza a análise de sentimento
            label, score = analyze_sentiment(user_input)
            
            # Exibe o resultado na interface
            st.success("Análise concluída!")
            st.subheader("Resultado da Análise:")
            st.write(f"Sentimento: **{label}**")
            st.write(f"Confiança: **{score:.2f}**")
            
            # Visualização do resultado
            st.progress(score)
        else:
            st.warning("Por favor, insira um texto para análise.")

    # Rodapé
    st.markdown("---")
    
    # Sobre o Modelo
    with st.expander("Sobre o Modelo"):
        st.write("""
            Este analisador de sentimentos utiliza o modelo **bertweet-pt-sentiment** da Hugging Face, treinado especificamente para interpretar e classificar sentimentos em textos em português.
        """)
    
    # Informação dos Desenvolvedores
    st.markdown("Desenvolvido por **Arthur Galvíncio, Isaac Medeiros e Rodrigo Andrade**")

# Executa a função principal
if __name__ == "__main__":
    main()
