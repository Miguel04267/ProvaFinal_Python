import pandas as pd
import openpyxl
import streamlit as st

df = pd.read_excel("dados-educacao.xlsx")

st.set_page_config(page_title="Painel IQVU - Belo Horizonte", layout="wide")


df_filtrado = df[
    (df["genero"].isin(["Masculino", "Feminino"])) &
    (df["escolaridade"] == "Mestrado")
].copy()

df_tabela = df_filtrado[["idade", "genero", "cor", "escolaridade", "área"]]

st.title("Painel Streamlit dos Dados Educação")

st.sidebar.header("Controles")
opcao = st.sidebar.radio("Selecione a visualização:", ["Tabela"])

if opcao == "Tabela":
    st.header("Tabela do ALuno (escolaridade)")
    st.dataframe(df_tabela, use_container_width=True, hide_index=True)

elif opcao == "Gráficos":
    st.header("Gráficos do Aluno — Masculino e Mestrado")

    st.subheader("1. Gráfico de Linha — Masculino")
    df_taquaril = df_tabela[df_tabela["NOMEUP"] == "Masculino"]

    fig_linha_taquaril = px.line(
        df_taquaril,
        x="idade",
        y="escolaridade",
        markers=True,
        title="Evolução do Aluno",
        template="plotly_dark"
    )
    fig_linha_taquaril.update_traces(line_color="#FF6B6B", line_width=3, marker_size=8)
    fig_linha_taquaril.update_xaxes(type="category")
    fig_linha_taquaril.update_layout(paper_bgcolor="#111827", plot_bgcolor="#111827")
    st.plotly_chart(fig_linha_taquaril, use_container_width=True)




