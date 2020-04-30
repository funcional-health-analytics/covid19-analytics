import streamlit as st
import pandas as pd


def print_description() -> None:
    description = """
    Análise do surto de COVID19 no mundo empregando-se principalmente modelos epidemiológicos e de processos hospitalares. 

    >**ADVERTÊNCIA**: os modelos e números aqui apresentados não são afirmações formais médicas sobre o progresso da doença, 
    >mas apenas exercícios que demonstram técnicas de modelagem e cenários hipotéticos de aplicação.
    """
    # Description
    st.image("notebooks/logo.png")
    st.markdown("# **Análise da COVID19 no mundo**")
    st.write(description)


def print_date_info(df: pd.DataFrame) -> None:
    final_date = df["date"].max()
    st.markdown(f"*Última atualização da base de dados: {str(final_date)[:10]}*")
