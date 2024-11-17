import pandas as pd
import streamlit as st
import plotly.express as px

# Configuração da página com layout "wide"
st.set_page_config(layout="wide", page_title="Visualização de Competições")

# Tema escuro para a página
bg_color = "#0e1117"
text_color = "white"

st.markdown(
    f"""
    <style>
    body {{
        background-color: {bg_color};
        color: {text_color};
    }}
    select {{
        background-color: #1c1e26;
        color: white;
        border: 1px solid #4a4a4a;
        padding: 5px;
        border-radius: 5px;
    }}
    option {{
        background-color: #1c1e26;
        color: white;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Carregar os dados da planilha Excel
try:
    df = pd.read_excel("familia.xlsx")  # Substitua pelo caminho correto do arquivo

    # Verificar se as colunas necessárias existem
    if "Competição" in df.columns and "Público" in df.columns:
        # Caixa de seleção para escolher a competição
        st.title("Visualização de Competição e Público")
        st.subheader("Selecione a competição para visualizar os dados:")
        competicoes = df["Competição"].unique()  # Valores únicos da coluna "competição"
        competicao_selecionada = st.selectbox(
            "Selecione uma competição:",
            competicoes,
            help="Escolha uma competição para visualizar as informações do público."
        )

        # Filtrar os dados com base na competição selecionada
        dados_filtrados = df[df["Competição"] == competicao_selecionada]

        # Exibir os dados filtrados em uma tabela
        st.subheader(f"Dados para a competição: {competicao_selecionada}")
        st.dataframe(dados_filtrados, width=1200)

        # Criar gráfico interativo do público
        if not dados_filtrados.empty:
            fig = px.bar(
                dados_filtrados,
                x=dados_filtrados.index,
                y="Público",
                text="Público",
                title=f"Público na competição: {competicao_selecionada}"
            )
            fig.update_traces(textposition="outside")
            fig.update_layout(
                plot_bgcolor=bg_color,
                paper_bgcolor=bg_color,
                font=dict(color=text_color)
            )
            st.plotly_chart(fig)
        else:
            st.warning("Nenhuma informação disponível para a competição selecionada.")
    else:
        st.error("As colunas 'Competição' e/ou 'Público' não foram encontradas na planilha.")
except Exception as e:
    st.error(f"Erro ao carregar a planilha: {e}")


