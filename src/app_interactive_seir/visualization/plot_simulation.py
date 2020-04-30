import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# plt.style.use("seaborn-whitegrid")


def plot_simulation_output(df: pd.DataFrame, target_location: str):
    df = df[["S", "E", "I", "R", "E+I", "E+I+R"]]

    fig1 = plt.figure()
    sns.despine()
    plt.grid()
    ax = sns.lineplot(data=df)
    ax.set_title("Visão Geral da Epidemia")

    fig2 = plt.figure()
    sns.despine()
    plt.grid()
    ax = sns.lineplot(data=df[["E", "I", "E+I", "E+I+R"]])
    ax.set_title("Apenas Expostos e Infectados")

    zoom_length = 30
    peak_date = df["I"].idxmax().date()
    zoom_on = (pd.Timestamp(peak_date) - pd.DateOffset(days=zoom_length)).date()

    zoom_end = (pd.Timestamp(peak_date) + pd.DateOffset(days=zoom_length)).date()
    fig3 = plt.figure()
    sns.despine()
    plt.grid()
    ax = sns.lineplot(
        data=df[["E", "I", "E+I"]][zoom_on:zoom_end], markers=True
    )
    ax.set_title(f"Zoom (de {zoom_on} a {zoom_end})")
    plt.xticks(fontsize=8, rotation=30)

    return st.markdown(f"# Modelo SEIR - {target_location}"), st.pyplot(fig1), st.pyplot(fig2), st.pyplot(fig3)


def display_peaks_from_simulation(peak_value: int, peak_date: pd.DatetimeIndex, category: str = "I") -> None:
    category_dict = {
        "S": "Suscetíveis",
        "E": "Expostos",
        "I": "Infectados",
        "R": "Recuperados",
    }
    st.markdown(f"# Datas e Valores de Pico ({category_dict[category]})")
    st.markdown(f"Data: **{str(peak_date)[:10]}**")
    st.markdown(f"{category_dict[category]}: **{int(round(peak_value, 0))}**")
