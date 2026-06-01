from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from pension_adequacy_analysis.config import (
    FIG_PENSION_BY_COUNTRY,
    FIG_PENSION_VS_POVERTY,
    FIG_POVERTY_BY_COUNTRY,
    PENSION_BY_COUNTRY_DATA,
    PENSION_VS_POVERTY_DATA,
    POVERTY_BY_COUNTRY_DATA,
)
from pension_adequacy_analysis.final.plot_figures import (
    plot_pension_by_country,
    plot_pension_vs_poverty,
    plot_poverty_by_country,
)


def task_plot_poverty_by_country(
    script: Path = Path(__file__),
    data: Path = POVERTY_BY_COUNTRY_DATA,
    produces: Path = FIG_POVERTY_BY_COUNTRY,
) -> None:
    """Plot and save elderly poverty by country figure."""
    df = pd.read_csv(data)
    fig, ax = plt.subplots(figsize=(42, 18))
    plot_poverty_by_country(ax, df)
    fig.savefig(produces, dpi=200, bbox_inches="tight")
    plt.close(fig)


def task_plot_pension_by_country(
    script: Path = Path(__file__),
    data: Path = PENSION_BY_COUNTRY_DATA,
    produces: Path = FIG_PENSION_BY_COUNTRY,
) -> None:
    """Plot and save pension replacement rate by country figure."""
    df = pd.read_csv(data)
    fig, ax = plt.subplots(figsize=(40, 40))
    plot_pension_by_country(ax, df)
    fig.tight_layout()
    fig.savefig(produces, dpi=200)
    plt.close(fig)


def task_plot_pension_vs_poverty(
    script: Path = Path(__file__),
    data: Path = PENSION_VS_POVERTY_DATA,
    produces: Path = FIG_PENSION_VS_POVERTY,
) -> None:
    """Plot and save pension replacement rate vs elderly poverty rate figure."""
    df = pd.read_csv(data)
    fig, ax = plt.subplots(figsize=(30, 16))
    plot_pension_vs_poverty(ax, df)
    fig.tight_layout()
    fig.savefig(produces, dpi=200)
    plt.close(fig)
