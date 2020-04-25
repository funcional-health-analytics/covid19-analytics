import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


def plot_cases_deaths(df: pd.DataFrame, target_location: str) -> None:
    st.markdown(f"# Numéro de Casos and Mortos - {target_location}")
    df[["total_cases", "total_deaths"]].plot()
    sns.despine()
    plt.grid()
    plt.title(f"Cases and Deaths - {target_location}")
    st.pyplot()


def display_last_rows(df: pd.DataFrame, nrows: int = 5) -> None:
    st.markdown(f"## **Últimos {nrows} dias**")
    st.dataframe(
        df[["total_cases", "total_deaths"]].tail(nrows)
    )


def display_epidemy_start_numbers(epidemy_start_numbers: dict, target_location: str) -> None:
    st.markdown(
        f"Data de início da epidemia (mortes > 50): **{str(epidemy_start_numbers['start_date'])[:10]}**"
    )
    st.markdown(f"Tamanho da população - {target_location}: **{int(epidemy_start_numbers['population_size'])}**")
