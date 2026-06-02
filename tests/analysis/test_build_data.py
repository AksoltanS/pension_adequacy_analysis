import pandas as pd
import pytest

from pension_adequacy_analysis.analysis.build_figures_data import (
    build_pension_vs_poverty,
    build_poverty_by_country,
)
from pension_adequacy_analysis.analysis.build_tables_data import (
    build_regression_results,
)


@pytest.fixture
def analysis_df():
    return pd.DataFrame(
        {
            "country_code": ["AUT", "DEU", "KOR", "FRA", "NLD"],
            "country": ["Austria", "Germany", "Korea", "France", "Netherlands"],
            "elderly_poverty_rate": [11.3, 8.4, 39.7, 5.5, 4.4],
            "pension_replacement_rate": [84.8, 62.3, 55.4, 66.1, 97.2],
            "gdp_per_capita": [52000.0, 50000.0, 31000.0, 44000.0, 58000.0],
        }
    )


def test_build_poverty_by_country_sorted(analysis_df):
    """Test poverty by country is sorted by poverty rate descending."""
    result = build_poverty_by_country(analysis_df)
    assert result["elderly_poverty_rate"].is_monotonic_decreasing


def test_build_pension_vs_poverty_one_row_per_country(analysis_df):
    """Test no duplicate countries in output."""
    result = build_pension_vs_poverty(analysis_df)
    assert result["country_code"].nunique() == len(result)


def test_build_regression_results_columns(analysis_df):
    """Test regression results has correct columns."""
    result = build_regression_results(analysis_df)
    assert list(result.columns) == [
        "variable",
        "coefficient",
        "std_error",
        "p_value",
        "ci_low",
        "ci_high",
    ]
