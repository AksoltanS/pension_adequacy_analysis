"""Functions to clean raw datasets for pension adequacy analysis."""

from pathlib import Path

import pandas as pd


def clean_elderly_poverty(path: Path) -> pd.DataFrame:
    """Clean the elderly poverty rate dataset.

    Args:
        path: Path to the raw elderly poverty CSV file.

    Returns:
        DataFrame with country_code, country, year, elderly_poverty_rate columns.
    """
    df = pd.read_csv(path)
    # Select and rename relevant columns
    df = df[["REF_AREA", "Reference area", "TIME_PERIOD", "OBS_VALUE"]]
    # Rename columns to more descriptive names
    df = df.rename(
        columns={
            "REF_AREA": "country_code",
            "TIME_PERIOD": "year",
            "Reference area": "country",
            "OBS_VALUE": "elderly_poverty_rate",
        }
    )
    # Convert year to integer
    df["year"] = df["year"].astype(int)
    # Drop rows with missing elderly poverty rates
    df = df.dropna(subset=["elderly_poverty_rate"]).reset_index(drop=True)
    return df


def clean_pension_replacement(path: Path) -> pd.DataFrame:
    """Clean the pension replacement rate dataset.

    Args:
        path: Path to the raw pension replacement CSV file.

    Returns:
        DataFrame with country_code, country, year, pension_replacement_rate columns.
    """
    df = pd.read_csv(path)
    df = df[df["MEASURE"] == "NPRR50"]
    df = df[["REF_AREA", "Reference area", "TIME_PERIOD", "OBS_VALUE"]]
    # Filter for the measure of interest
    df = (
        df.groupby(["REF_AREA", "Reference area", "TIME_PERIOD"])["OBS_VALUE"]
        .mean()
        .reset_index()
    )

    df = df.rename(
        columns={
            "REF_AREA": "country_code",
            "TIME_PERIOD": "year",
            "Reference area": "country",
            "OBS_VALUE": "pension_replacement_rate",
        }
    )
    return df


def clean_gdp_per_capita(path: Path) -> pd.DataFrame:
    """Clean the GDP per capita dataset.

    Args:
        path: Path to the raw GDP per capita CSV file.

    Returns:
        DataFrame with country_code, country, year, gdp_per_capita columns.
    """
    df = pd.read_csv(path, skiprows=4)
    df = df.drop(columns=["Indicator Name", "Indicator Code"])
    df = df.loc[:, ~df.columns.str.startswith("Unnamed")]
    df = pd.melt(
        df,
        id_vars=["Country Name", "Country Code"],
        var_name="year",
        value_name="gdp_per_capita",
    )
    df = df.rename(columns={"Country Name": "country", "Country Code": "country_code"})
    df["year"] = df["year"].astype(int)
    return df.dropna(subset=["gdp_per_capita"]).reset_index(drop=True)
