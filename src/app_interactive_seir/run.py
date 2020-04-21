import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import streamlit as st
import sys
import seaborn as sns

#sys.path.insert(0, "src/")

from seir_model import simulate
from plot_simulation import plot_simulation_output

pd.set_option(
    "display.float_format", lambda x: "%.3f" % x
)  # Granting that pandas won't use scientific notation for floating fields

description = """
                Análise do surto de COVID19 no mundo empregando-se principalmente modelos epidemiológicos e de processos hospitalares. 
                
                >**ADVERTÊNCIA**: os modelos e números aqui apresentados não são afirmações formais médicas sobre o progresso da doença, 
                >mas apenas exercícios que demonstram técnicas de modelagem e cenários hipotéticos de aplicação.
                """
# Description
st.image("notebooks/logo.png")
st.markdown("# **Análise da COVID19 no mundo**")
st.write(description)

data_folder = "data/"
df_epidemy_data = pd.read_csv(
    f"{data_folder}ourworldindata.org/coronavirus-source-data/full_data.csv",
    parse_dates=["date"],
)
df_locations_data = pd.read_csv(
    f"{data_folder}ourworldindata.org/coronavirus-source-data/locations.csv"
)

# enrich epidemy data with additional demographic information
df_epidemy_data = df_epidemy_data.merge(df_locations_data, on="location")

# Sidebar
## Location selector
locations = df_epidemy_data["location"].unique().tolist()
default_loc_index = locations.index("Brazil") if "Brazil" in locations else 0
target_location = st.sidebar.selectbox(
    "Selecione um local", locations, default_loc_index
)

## SEIR model parameters
st.sidebar.text("Selecione os parâmetros do modelo SEIR")
alpha = st.sidebar.slider("Alpha (E para I): ", 0.0, 1.0, 0.9)
beta = st.sidebar.slider("Beta (S para E): ", 0.0, 1.0, 0.8)
gamma = st.sidebar.slider("Gamma (I para R): ", 0.0, 1.0, 0.3)
epidemic_duration_in_days = st.sidebar.number_input(
    "Duração da epidemia (dias): ", 1, 1000, 365
)

## Info about date
final_date = df_epidemy_data["date"].max()
st.markdown(f"*Última atualização da base de dados: {str(final_date)[:10]}*")

df_data_target = (
    df_epidemy_data[df_epidemy_data["location"] == target_location]
    .copy()
    .set_index(["date"])
    .drop("location", axis=1)
)

df_data_target["total_cases_ESTIMATED"] = (df_data_target["total_deaths"] / 0.05).shift(
    -7
)
df_data_target["total_cases_ESTIMATED_2"] = 10 * df_data_target["total_cases"]

# Plot cases and deaths
st.markdown(f"# Numéro de Casos and Mortos - {target_location}")
df_data_target[["total_cases", "total_deaths"]].plot()
sns.despine()
plt.grid()
plt.title(f"Cases and Deaths - {target_location}")
st.pyplot()

st.markdown("## **Últimos cinco dias**")
st.dataframe(
    df_data_target[["total_cases", "total_deaths"]].tail(5)
)  # First lines of DataFrame

epidemic_start_date = df_data_target[df_data_target["total_cases"] >= 50][
    "total_cases"
].index[0]

first_date_row = df_data_target.loc[epidemic_start_date]
population_size = first_date_row["population"]
initially_infected = first_date_row["total_cases"]

st.markdown(
    f"Data de início da epidemia (mortes > 50): **{str(epidemic_start_date)[:10]}**"
)
st.markdown(f"Tamanho da população - {target_location}: **{int(population_size)}**")

df_data_target = df_data_target[epidemic_start_date:]

# Simulation execution
simulate_trigger = st.sidebar.button("Simular!")
if simulate_trigger:
    df_simulation_data = simulate(
        S=population_size - initially_infected,
        E=initially_infected,
        I=0,
        R=0,
        alpha=alpha,
        beta=beta,
        gamma=gamma,
        epidemic_start_date=epidemic_start_date,
        epidemic_duration_in_days=epidemic_duration_in_days,
        population_size=population_size,
    )

    # Plots from simulation
    st.markdown(f"# Modelo SEIR - {target_location}")
    plot_simulation_output(df_simulation_data)

    # Max Points with date
    peak_infected, date_peak = (
        df_simulation_data["I"].max(),
        df_simulation_data["I"].idxmax(),
    )
    st.markdown(f"# Datas e Valores de Pico (Infectados)")
    st.markdown(f"Data: **{str(date_peak)[:10]}**")
    st.markdown(f"Infectados: **{int(round(peak_infected,0))}**")
