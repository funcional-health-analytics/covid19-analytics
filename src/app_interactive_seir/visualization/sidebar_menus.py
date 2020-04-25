import streamlit as st
import pandas as pd


def get_target_location(df: pd.DataFrame) -> str:
    locations = df["location"].unique().tolist()
    default_loc_index = locations.index("Brazil") if "Brazil" in locations else 0
    target_location = st.sidebar.selectbox(
        "Selecione um local", locations, default_loc_index
    )

    return target_location


def get_model_parameters() -> dict:
    st.sidebar.text("Selecione os parâmetros do modelo SEIR")
    alpha = st.sidebar.slider("Alpha (E para I): ", 0.0, 1.0, 0.9)
    beta = st.sidebar.slider("Beta (S para E): ", 0.0, 1.0, 0.8)
    gamma = st.sidebar.slider("Gamma (I para R): ", 0.0, 1.0, 0.3)
    epidemic_duration_in_days = st.sidebar.number_input(
        "Duração da epidemia (dias): ", 1, 1000, 365
    )

    model_params = {
        "alpha": alpha,
        "beta": beta,
        "gamma": gamma,
        "epidemic_duration_in_days": epidemic_duration_in_days,
    }

    return model_params
