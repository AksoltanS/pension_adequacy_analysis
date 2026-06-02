from pathlib import Path

import pandas as pd

from pension_adequacy_analysis.data_management.clean_data import (
    clean_elderly_poverty,
    clean_gdp_per_capita,
    clean_pension_replacement,
)

_EXPECTED_COUNT = 2


def test_clean_elderly_poverty_columns(tmp_path):
    raw = pd.DataFrame(
        {
            "REF_AREA": ["AUT", "DEU"],
            "Reference area": ["Austria", "Germany"],
            "TIME_PERIOD": [2022, 2022],
            "OBS_VALUE": [11.3, 8.4],
            "EXTRA_COL": ["x", "y"],
        }
    )
    path = tmp_path / "test.csv"
    raw.to_csv(path, index=False)
    result = clean_elderly_poverty(path)
    assert list(result.columns) == [
        "country_code",
        "country",
        "year",
        "elderly_poverty_rate",
    ]


def test_clean_elderly_poverty_no_missing(tmp_path):
    raw = pd.DataFrame(
        {
            "REF_AREA": ["AUT", "DEU", "FRA"],
            "Reference area": ["Austria", "Germany", "France"],
            "TIME_PERIOD": [2022, 2022, 2022],
            "OBS_VALUE": [11.3, None, 9.5],
        }
    )
    path = tmp_path / "test.csv"
    raw.to_csv(path, index=False)
    result = clean_elderly_poverty(path)
    assert len(result) == _EXPECTED_COUNT
    assert result["country"].tolist() == ["Austria", "France"]


def test_clean_elderly_poverty_year_dtype(tmp_path):
    raw = pd.DataFrame(
        {
            "REF_AREA": ["AUT"],
            "Reference area": ["Austria"],
            "TIME_PERIOD": ["2022"],
            "OBS_VALUE": [11.3],
        }
    )
    path = tmp_path / "test.csv"
    raw.to_csv(path, index=False)
    result = clean_elderly_poverty(path)
    assert result["year"].dtype == int


def test_clean_pension_replacement_columns(tmp_path):
    raw = pd.DataFrame(
        {
            "REF_AREA": ["AUT", "DEU"],
            "Reference area": ["Austria", "Germany"],
            "TIME_PERIOD": [2022, 2022],
            "OBS_VALUE": [45.6, 50.2],
            "MEASURE": ["NPRR50", "NPRR50"],
            "EXTRA_COL": ["x", "y"],
        }
    )
    path = tmp_path / "test.csv"
    raw.to_csv(path, index=False)

    result = clean_pension_replacement(path)
    assert list(result.columns) == [
        "country_code",
        "country",
        "year",
        "pension_replacement_rate",
    ]


def test_clean_gdp_per_capita_columns(tmp_path):
    raw = pd.DataFrame(
        {
            "Country Name": ["Austria", "Germany"],
            "Country Code": ["AUT", "DEU"],
            "Indicator Name": ["GDP per capita", "GDP per capita"],
            "Indicator Code": ["NY.GDP.PCAP.CD", "NY.GDP.PCAP.CD"],
            "2020": [50000.0, 55000.0],
            "2021": [51000.0, 56000.0],
            "2022": [52000.0, 57000.0],
        }
    )
    path = tmp_path / "test.csv"
    with Path.open(path, "w") as f:
        f.write("\n\n\n\n")
    raw.to_csv(path, mode="a", index=False)
    result = clean_gdp_per_capita(path)
    assert list(result.columns) == [
        "country",
        "country_code",
        "year",
        "gdp_per_capita",
    ]
