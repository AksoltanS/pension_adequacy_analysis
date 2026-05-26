import pandas as pd


def build_analysis_data(
    elderly_poverty: pd.DataFrame,
    pension_replacement: pd.DataFrame,
    gdp_per_capita: pd.DataFrame,
) -> pd.DataFrame:
    """Merge cleaned datasets into one analysis dataset.

    Args:
           elderly_poverty: Cleaned elderly poverty DataFrame.
           pension_replacement: Cleaned pension replacement DataFrame.
           gdp_per_capita: Cleaned GDP per capita DataFrame.

    Returns:
           Merged DataFrame with all variables aligned by country and year.
    """
    return (
        elderly_poverty.merge(
            pension_replacement, on=["country_code", "year"], how="inner"
        )
        .merge(
            gdp_per_capita[["country_code", "year", "gdp_per_capita"]],
            on=["country_code", "year"],
            how="inner",
        )
        .reset_index(drop=True)
    )
