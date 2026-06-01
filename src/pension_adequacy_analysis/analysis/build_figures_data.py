"""Functions to build figure and table data for pension adequacy analysis."""

import pandas as pd


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
        .drop_duplicates(subset=["country_code"])
        .reset_index(drop=True)
    )
