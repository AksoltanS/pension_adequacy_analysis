from pathlib import Path

import pandas as pd

from pension_adequacy_analysis.analysis.build_analysis_data import (
    build_analysis_data,
)
from pension_adequacy_analysis.config import (
    ANALYSIS_DATA,
    ELDERLY_POVERTY_CLEAN,
    GDP_CLEAN,
    PENSION_REPLACEMENT_CLEAN,
)

_ANALYSIS_DEPS = {
    "elderly_poverty": ELDERLY_POVERTY_CLEAN,
    "pension_replacement": PENSION_REPLACEMENT_CLEAN,
    "gdp": GDP_CLEAN,
}


def task_build_analysis_data(
    script: Path = Path(__file__),
    data: dict[str, Path] = _ANALYSIS_DEPS,
    produces: Path = ANALYSIS_DATA,
) -> None:
    """Task to build the analysis dataset by merging cleaned datasets."""
    elderly_poverty = pd.read_parquet(data["elderly_poverty"])
    pension_replacement = pd.read_parquet(data["pension_replacement"])
    gdp_per_capita = pd.read_parquet(data["gdp"])
    analysis_data = build_analysis_data(
        elderly_poverty, pension_replacement, gdp_per_capita
    )
    analysis_data.to_parquet(produces, index=False)
