import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# plt.style.use("seaborn-whitegrid")


def plot_simulation_output(df_simulated_data):
    df_simulated_data = df_simulated_data[["S", "E", "I", "R", "E+I", "E+I+R"]]

    fig1 = plt.figure()
    sns.despine()
    plt.grid()
    ax = sns.lineplot(data=df_simulated_data)
    ax.set_title("Visão Geral da Epidemia")

    fig2 = plt.figure()
    sns.despine()
    plt.grid()
    ax = sns.lineplot(data=df_simulated_data[["E", "I", "E+I", "E+I+R"]])
    ax.set_title("Apenas Expostos e Infectados")

    zoom_length = 30
    peak_date = df_simulated_data["I"].idxmax().date()
    zoom_on = (pd.Timestamp(peak_date) - pd.DateOffset(days=zoom_length)).date()

    zoom_end = (pd.Timestamp(peak_date) + pd.DateOffset(days=zoom_length)).date()
    fig3 = plt.figure()
    sns.despine()
    plt.grid()
    ax = sns.lineplot(
        data=df_simulated_data[["E", "I", "E+I"]][zoom_on:zoom_end], markers=True
    )
    ax.set_title(f"Zoom (de {zoom_on} a {zoom_end})")
    plt.xticks(fontsize=8, rotation=30)

    return st.pyplot(fig1), st.pyplot(fig2), st.pyplot(fig3)
