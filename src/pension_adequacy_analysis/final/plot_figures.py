"""Plotting functions for pension adequacy analysis figures."""

import numpy as np
import pandas as pd
from matplotlib.axes import Axes

from pension_adequacy_analysis.config import (
    COLOR_ACCENT,
    COLOR_PRIMARY,
    COLOR_SCATTER,
    COLOR_SECONDARY,
    FONT_LABEL,
    FONT_TICK,
    FONT_TITLE,
)


def plot_poverty_by_country(ax: Axes, df: pd.DataFrame) -> None:
    """Plot elderly poverty rate by country as a vertical bar chart.

    Args:
        ax: Matplotlib axes to draw on.
        df: DataFrame from build_poverty_by_country with country and
            elderly_poverty_rate columns.
    """
    df_sorted = df.sort_values("elderly_poverty_rate", ascending=False)
    x = range(len(df_sorted))
    ax.bar(x, df_sorted["elderly_poverty_rate"], color=COLOR_PRIMARY, width=0.8)
    ax.set_xlim(-0.5, len(df_sorted) - 0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(
        df_sorted["country"], rotation=45, ha="right", fontsize=FONT_TICK
    )
    ax.set_ylabel("At-risk-of-poverty rate (%)", fontsize=FONT_LABEL)
    ax.set_title(
        "Elderly Poverty Rate by Country (2024)",
        fontsize=FONT_TITLE,
        fontweight="bold",
        pad=15,
    )
    ax.tick_params(axis="y", labelsize=FONT_LABEL)
    ax.yaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)


def plot_pension_by_country(ax: Axes, df: pd.DataFrame) -> None:
    """Plot pension replacement rate by country as a horizontal bar chart.

    Args:
        ax: Matplotlib axes to draw on.
        df: DataFrame from build_pension_by_country with country and
            pension_replacement_rate columns.
    """
    df_sorted = df.sort_values("pension_replacement_rate", ascending=True)
    bars = ax.barh(
        df_sorted["country"], df_sorted["pension_replacement_rate"], color=COLOR_ACCENT
    )
    for bar, val in zip(bars, df_sorted["pension_replacement_rate"], strict=False):
        ax.text(
            val + 0.5,
            bar.get_y() + bar.get_height() / 2,
            f"{val:.1f}%",
            va="center",
            fontsize=FONT_TICK,
        )
    ax.set_xlabel("Net Pension Replacement Rate (%)", fontsize=FONT_LABEL)
    ax.set_title(
        "Pension Replacement Rate by Country (2024)",
        fontsize=FONT_TITLE,
        fontweight="bold",
        pad=15,
    )
    ax.tick_params(axis="both", labelsize=FONT_TICK)
    ax.xaxis.grid(True, alpha=0.3)
    ax.set_axisbelow(True)


def plot_pension_vs_poverty(ax: Axes, df: pd.DataFrame) -> None:
    """Plot pension replacement rate vs elderly poverty rate as a scatter plot.

    Args:
        ax: Matplotlib axes to draw on.
        df: DataFrame with country, pension_replacement_rate, and
            elderly_poverty_rate columns.
    """
    ax.scatter(
        df["pension_replacement_rate"],
        df["elderly_poverty_rate"],
        color=COLOR_SCATTER,
        s=60,
        zorder=3,
    )
    for _, row in df.iterrows():
        ax.text(
            row["pension_replacement_rate"] + 0.5,
            row["elderly_poverty_rate"] + 0.3,
            row["country_code"],
            fontsize=9,
        )
    m, b = np.polyfit(df["pension_replacement_rate"], df["elderly_poverty_rate"], 1)
    x_line = np.linspace(
        df["pension_replacement_rate"].min(), df["pension_replacement_rate"].max(), 100
    )
    ax.plot(
        x_line,
        m * x_line + b,
        color=COLOR_SECONDARY,
        linestyle="--",
        linewidth=2,
        label="OLS fit",
    )
    ax.legend(fontsize=FONT_TICK)
    ax.set_xlabel("Net Pension Replacement Rate (%)", fontsize=FONT_LABEL)
    ax.set_ylabel("At-risk-of-poverty rate (%)", fontsize=FONT_LABEL)
    ax.set_title(
        "Pension Replacement Rate vs Elderly Poverty Rate (2024)",
        fontsize=FONT_TITLE,
        fontweight="bold",
        pad=15,
    )
    ax.tick_params(axis="both", labelsize=FONT_TICK)
    ax.grid(True, alpha=0.3)
    ax.set_axisbelow(True)
