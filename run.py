import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import streamlit as st
import sys
import seaborn as sns

sys.path.insert(0, "src/")

pd.set_option(
    "display.float_format", lambda x: "%.3f" % x
)  # Granting that pandas won't use scientific notation for floating fields

description = """
                Análise do surto de COVID19 no Brasil empregando-se principalmente modelos epidemiológicos e de processos hospitalares. 
                ADVERTÊNCIA: os modelos e números aqui apresentados não são afirmações formais médicas sobre o progresso da doença, 
                mas apenas exercícios que demonstram técnicas de modelagem e cenários hipotéticos de aplicação.
                """
# Description
st.image("notebooks/logo.png")
st.write("*Análise da COVID19 no Brasil*")
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

# Location selector
locations = df_epidemy_data["location"].unique().tolist()
default_loc_index = locations.index("Brazil") if "Brazil" in locations else 0
target_location = st.sidebar.selectbox(
    "Selecione um local", locations, default_loc_index
)

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
plt.title(f"Cases and Deaths - {target_location}")
st.pyplot()
