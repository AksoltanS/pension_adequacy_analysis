from pathlib import Path

import pandas as pd

from pension_adequacy_analysis.analysis.build_tables_data import (
    build_descriptive_stats,
    build_regression_results,
)
from pension_adequacy_analysis.config import (
    ANALYSIS_DATA,
    TABLE_DESCRIPTIVE_STATS_TEX,
    TABLE_REGRESSION_RESULTS_TEX,
)

_TABLES_PRODUCES = {
    "descriptive_stats": TABLE_DESCRIPTIVE_STATS_TEX,
    "regression_results": TABLE_REGRESSION_RESULTS_TEX,
}


def task_build_tables_data(
    script: Path = Path(__file__),
    data: Path = ANALYSIS_DATA,
    produces: dict[str, Path] = _TABLES_PRODUCES,
) -> None:
    """Build and save descriptive statistics and regression results."""
    df = pd.read_parquet(data)
    desc = build_descriptive_stats(df)
    desc.to_csv(produces["descriptive_stats"], index=False)
    desc.to_latex(produces["descriptive_stats"].with_suffix(".tex"), index=False)
    reg = build_regression_results(df)
    reg.to_csv(produces["regression_results"], index=False)
    reg.to_latex(produces["regression_results"].with_suffix(".tex"), index=False)
