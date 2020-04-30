import pandas as pd


def prepare_data(df: pd.DataFrame, target_location: str) -> pd.DataFrame:
    df_data_target = (
        df[df["location"] == target_location].copy().set_index(["date"]).drop("location", axis=1)
    )

    df_data_target["total_cases_ESTIMATED"] = (df_data_target["total_deaths"] / 0.05).shift(
        -7
    )
    df_data_target["total_cases_ESTIMATED_2"] = 10 * df_data_target["total_cases"]

    return df_data_target


def get_epidemy_start_numbers(df: pd.DataFrame, ncases: int = 50) -> dict:
    epidemic_start_date = df[df["total_cases"] >= ncases][
        "total_cases"
    ].index[0]

    first_date_row = df.loc[epidemic_start_date]
    population_size = first_date_row["population"]
    initially_infected = first_date_row["total_cases"]

    epidemy_start_numbers = {
        "start_date": epidemic_start_date,
        "population_size": population_size,
        "initially_infected": initially_infected
    }

    return epidemy_start_numbers


def get_peaks_from_simulation(df: pd.DataFrame, category: str = "I") -> (int, pd.DatetimeIndex):
    return (
        df[category].max(),
        df[category].idxmax(),
    )
