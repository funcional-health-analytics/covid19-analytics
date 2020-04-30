import pandas as pd
import streamlit as st

from model.seir_model import run_seir_model
from visualization.plot_simulation import plot_simulation_output, display_peaks_from_simulation
from visualization.plot_data import plot_cases_deaths, display_last_rows, display_epidemy_start_numbers
from visualization.description import print_description, print_date_info
from visualization.sidebar_menus import get_target_location, get_model_parameters
from data.load_data import load_epidemy_data
from data.preprocessing import prepare_data, get_epidemy_start_numbers, get_peaks_from_simulation

pd.set_option(
    "display.float_format", lambda x: "%.3f" % x
)  # Granting that pandas won't use scientific notation for floating fields

print_description()

df_epidemy_data = load_epidemy_data(data_folder="data/")

print_date_info(df_epidemy_data)

target_location = get_target_location(df_epidemy_data)

model_params = get_model_parameters()

df_data_target = prepare_data(df_epidemy_data, target_location)

plot_cases_deaths(df_data_target, target_location)

display_last_rows(df_data_target, nrows=5)

epidemy_start_numbers = get_epidemy_start_numbers(df_data_target, ncases=50)
display_epidemy_start_numbers(epidemy_start_numbers, target_location)

simulate_trigger = st.sidebar.button("Simular!")
if simulate_trigger:
    df_simulation_data = run_seir_model(model_params, epidemy_start_numbers)

    plot_simulation_output(df_simulation_data, target_location)

    peak_value, peak_date = get_peaks_from_simulation(df_simulation_data, category="I")
    display_peaks_from_simulation(peak_value, peak_date, category="I")

