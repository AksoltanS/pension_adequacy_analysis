"""Functions to build figure and table data for pension adequacy analysis."""

import pandas as pd
import statsmodels.api as sm


def build_poverty_by_country(df: pd.DataFrame) -> pd.DataFrame:
    """Build data for the elderly poverty by country figure."""
    return (
        df[["country", "country_code", "elderly_poverty_rate"]]
        .drop_duplicates(subset=["country_code"])
        .sort_values("elderly_poverty_rate", ascending=False)
        .reset_index(drop=True)
    )


def build_pension_by_country(df: pd.DataFrame) -> pd.DataFrame:
    """Build data for the pension replacement rate by country figure."""
    return (
        df[["country", "country_code", "pension_replacement_rate"]]
        .drop_duplicates(subset=["country_code"])  # ← add subset
        .sort_values("pension_replacement_rate", ascending=True)
        .reset_index(drop=True)
    )


def build_pension_vs_poverty(df: pd.DataFrame) -> pd.DataFrame:
    """Build data for the pension vs poverty scatter plot."""
    return (
        df[
            [
                "country",
                "country_code",
                "pension_replacement_rate",
                "elderly_poverty_rate",
                "gdp_per_capita",
            ]
        ]
        .drop_duplicates(subset=["country_code"])  # ← add subset
        .reset_index(drop=True)
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
