import math
import pandas as pd
from utils import aux_enforce_max_addition, aux_enforce_max_removal, param_at


def s(t, S, E, I, R, alpha, beta, gamma, population_size):
    delta = aux_enforce_max_removal(S, -((param_at(beta, t) * I * S) / population_size))

    return delta


def e(t, S, E, I, R, alpha, beta, gamma, population_size):
    delta_s = aux_enforce_max_addition(
        S, ((param_at(beta, t) * I * S) / population_size)
    )

    delta = aux_enforce_max_removal(E, param_at(delta_s, t) - param_at(alpha, t) * E)

    return delta


def i(t, S, E, I, R, alpha, beta, gamma):
    delta_e = aux_enforce_max_addition(E, param_at(alpha, t) * E)

    delta = aux_enforce_max_removal(I, param_at(delta_e, t) - param_at(gamma, t) * I)

    return delta


def r(t, S, E, I, R, alpha, beta, gamma):
    delta = aux_enforce_max_addition(I, param_at(gamma, t) * I)

    return delta


# how many new patients will be added to E
def e_delta(t, S, E, I, R, alpha, beta, gamma, population_size):
    delta_s = aux_enforce_max_addition(
        S, ((param_at(beta, t) * I * S) / population_size)
    )

    return delta_s


# how many new patients will be added to I
def i_delta(t, S, E, I, R, alpha, beta, gamma):
    delta_e = aux_enforce_max_addition(E, param_at(alpha, t) * E)

    return delta_e


# how many new patients will be added to R
def r_delta(t, S, E, I, R, alpha, beta, gamma):
    delta_r = aux_enforce_max_addition(I, param_at(gamma, t) * I)

    return delta_r


def simulate(
    S,
    E,
    I,
    R,
    alpha,
    beta,
    gamma,
    epidemic_start_date,
    epidemic_duration_in_days,
    population_size,
    s_func=s,
    e_func=e,
    i_func=i,
    r_func=r,
    e_delta_func=e_delta,
    i_delta_func=i_delta,
    r_delta_func=r_delta,
):

    generated_data = []  # initial data

    # changes start at 0
    E_delta = 0
    I_delta = 0
    R_delta = 0

    for t in range(0, epidemic_duration_in_days):
        generated_data.append((S, E, E_delta, I, I_delta, R, R_delta))

        # main model components
        S_next = S + s_func(t, S, E, I, R, alpha, beta, gamma, population_size)
        E_next = E + e_func(t, S, E, I, R, alpha, beta, gamma, population_size)
        I_next = I + i_func(t, S, E, I, R, alpha, beta, gamma)
        R_next = R + r_func(t, S, E, I, R, alpha, beta, gamma)

        # added information for later analyses
        I_delta = i_delta_func(t, S, E, I, R, alpha, beta, gamma)
        E_delta = e_delta_func(t, S, E, I, R, alpha, beta, gamma, population_size)
        R_delta = r_delta_func(t, S, E, I, R, alpha, beta, gamma)

        # lockstep updates
        S = S_next
        E = E_next
        I = I_next
        R = R_next

        assert math.isclose(
            S + E + I + R, population_size, rel_tol=1e-9, abs_tol=0.0
        ), "Population size must not change."

    df = pd.DataFrame(
        generated_data,
        columns=["S", "E", "E_delta", "I", "I_delta", "R", "R_delta"],
        index=pd.date_range(
            start=epidemic_start_date, periods=epidemic_duration_in_days, freq="D"
        ),
    )

    df["E+I"] = df["E"] + df["I"]
    df["E+I+R"] = df["E"] + df["I"] + df["R"]

    return df
