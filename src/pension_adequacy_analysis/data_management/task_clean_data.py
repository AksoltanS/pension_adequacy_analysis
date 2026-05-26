from pathlib import Path

from pension_adequacy_analysis.config import (
    ELDERLY_POVERTY_CLEAN,
    ELDERLY_POVERTY_RAW,
    GDP_CLEAN,
    GDP_RAW,
    PENSION_REPLACEMENT_CLEAN,
    PENSION_REPLACEMENT_RAW,
)
from pension_adequacy_analysis.data_management.clean_data import (
    clean_elderly_poverty,
    clean_gdp_per_capita,
    clean_pension_replacement,
)


def task_clean_elderly_poverty(
    script: Path = Path(__file__),
    data: Path = ELDERLY_POVERTY_RAW,
    produces: Path = ELDERLY_POVERTY_CLEAN,
) -> None:
    """Clean and save the elderly poverty dataset."""
    clean_elderly_poverty(data).to_parquet(produces, index=False)


def task_clean_pension_replacement(
    script: Path = Path(__file__),
    data: Path = PENSION_REPLACEMENT_RAW,
    produces: Path = PENSION_REPLACEMENT_CLEAN,
) -> None:
    """Task to clean the pension replacement dataset."""
    clean_pension_replacement(data).to_parquet(produces, index=False)


def task_clean_gdp_per_capita(
    script: Path = Path(__file__),
    data: Path = GDP_RAW,
    produces: Path = GDP_CLEAN,
) -> None:
    """Task to clean the GDP per capita dataset."""
    clean_gdp_per_capita(data).to_parquet(produces, index=False)
