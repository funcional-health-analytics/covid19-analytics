import pandas as pd
import streamlit as st


@st.cache(suppress_st_warning=True)
def load_epidemy_data(data_folder: str = "data/") -> pd.DataFrame:
    df_epidemy_data = pd.read_csv(
        f"{data_folder}ourworldindata.org/coronavirus-source-data/full_data.csv",
        parse_dates=["date"],
    )
    df_locations_data = pd.read_csv(
        f"{data_folder}ourworldindata.org/coronavirus-source-data/locations.csv"
    )

    # enrich epidemy data with additional demographic information
    df_epidemy_data = df_epidemy_data.merge(df_locations_data, on="location")

    return df_epidemy_data
