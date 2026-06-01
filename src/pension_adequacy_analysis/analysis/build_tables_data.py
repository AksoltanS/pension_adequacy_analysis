"""Functions to build table data for pension adequacy analysis."""

from typing import Any, cast

import pandas as pd
import statsmodels.api as sm


def build_descriptive_stats(df: pd.DataFrame) -> pd.DataFrame:
    """Build descriptive statistics for Table 1a.

    Args:
        df: Analysis DataFrame with all variables.

    Returns:
        DataFrame with count, mean, std, min, max for key variables.
    """
    return (
        df[["elderly_poverty_rate", "pension_replacement_rate", "gdp_per_capita"]]
        .describe()
        .loc[["count", "mean", "std", "min", "max"]]
        .reset_index()
        .rename(columns={"index": "statistic"})
        .melt(id_vars="statistic", var_name="variable", value_name="value")
        .pivot_table(
            index="variable",
            columns="statistic",
            values="value",
            aggfunc=cast("Any", "first"),
        )
        .reset_index()
    )


def build_regression_results(df: pd.DataFrame) -> pd.DataFrame:
    """Build OLS regression results for Table 1b.

    Args:
        df: Analysis DataFrame with all variables.

    Returns:
        DataFrame with regression coefficients, standard errors, and p-values.
    """
    x_mat = sm.add_constant(df[["pension_replacement_rate", "gdp_per_capita"]])
    y = df["elderly_poverty_rate"]
    model = sm.OLS(y, x_mat).fit()

    return pd.DataFrame(
        {
            "variable": model.params.index,
            "coefficient": model.params.to_numpy(),
            "std_error": model.bse.to_numpy(),
            "p_value": model.pvalues.to_numpy(),
            "ci_low": model.conf_int()[0].to_numpy(),
            "ci_high": model.conf_int()[1].to_numpy(),
        }
    )
