"""All the general configuration of the project."""

from pathlib import Path

import pandas as pd

pd.options.mode.copy_on_write = True


SRC: Path = Path(__file__).parent.resolve()
ROOT: Path = SRC.joinpath("..", "..").resolve()

BLD: Path = ROOT.joinpath("bld").resolve()


DOCUMENTS: Path = ROOT.joinpath("documents").resolve()

TEMPLATE_GROUPS: tuple[str, ...] = ("marital_status", "highest_qualification")


DATA_RAW = SRC / "data" / "raw"

# raw file paths

ELDERLY_POVERTY_RAW = DATA_RAW / "elderly_poverty.csv"

PENSION_REPLACEMENT_RAW = DATA_RAW / "pension_replacement.csv"

GDP_RAW = DATA_RAW / "gdp_per_capita.csv"
# output paths

BLD_DATA = BLD / "data"
BLD_FIGURES = BLD / "figures"
BLD_TABLES = BLD / "tables"

ELDERLY_POVERTY_CLEAN = BLD_DATA / "elderly_poverty_clean.parquet"
PENSION_REPLACEMENT_CLEAN = BLD_DATA / "pension_replacement_clean.parquet"
GDP_CLEAN = BLD_DATA / "gdp_clean.parquet"
ANALYSIS_DATA = BLD_DATA / "analysis_data.parquet"
FIG_POVERTY_BY_COUNTRY = BLD_FIGURES / "elderly_poverty_by_country.png"
FIG_PENSION_BY_COUNTRY = BLD_FIGURES / "pension_replacement_by_country.png"
FIG_PENSION_VS_POVERTY = BLD_FIGURES / "pension_vs_poverty_scatter.png"
