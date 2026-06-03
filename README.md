# Pension Adequacy and Elderly Poverty: A Cross-Country Analysis

## Description

Pension replacement rates measure how much of pre-retirement earnings a pension
replaces. A country with a 80% replacement rate pays pensioners 80% of what they earned
while working. But does a higher replacement rate actually reduce elderly poverty? Not
always — it depends on wage levels, cost of living, and private savings. This project
examines 38 OECD countries in 2024 to estimate how much pension generosity matters for
elderly poverty, controlling for national wealth.

## Outputs

- **Figure 1** — Elderly poverty rate by country
- **Figure 2** — Pension replacement rate by country
- **Figure 3** — Pension vs poverty scatter plot with regression line
- **Table 1a** — Descriptive statistics
- **Table 1b** — OLS regression results

## How to run

Raw data is included — no download needed. Install [Pixi](https://pixi.sh/), then:

```bash
pixi install
pixi run pytask
pixi run pytest
```

Figures go to `bld/figures/` and tables to `bld/tables/`.

## Data

| File                      | Source                                                            | What it contains                                      |
| ------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------- |
| `elderly_poverty.csv`     | [OECD](https://data-explorer.oecd.org)                            | At-risk-of-poverty rate for 65+, 50% median threshold |
| `pension_replacement.csv` | [OECD](https://data-explorer.oecd.org)                            | Net pension replacement rate at 50% of average wage   |
| `gdp_per_capita.csv`      | [World Bank](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD) | GDP per capita in current USD                         |

## Project structure

```
src/pension_adequacy_analysis/
├── config.py                  ← shared paths and constants
├── data_management/           ← cleaning functions and tasks
├── analysis/                  ← merging, figure data, regression
└── final/                     ← plotting functions and tasks

bld/
├── data/      ← cleaned and merged data
├── figures/   ← PNG figures
└── tables/    ← LaTeX tables

tests/
├── analysis/
└── data_management/
```

## Regression

```
elderly_poverty_rate = β0 + β1 × pension_replacement_rate + β2 × gdp_per_capita + ε
```

## Key Findings

- Countries with lower pension replacement rates tend to have higher elderly poverty
- Korea (replacement rate 55%) has the highest elderly poverty (~40%) in the sample
- Nordic countries combine high replacement rates with low elderly poverty
- GDP per capita is negatively associated with elderly poverty controlling for pensions

## Credits

- OECD: https://data-explorer.oecd.org
- World Bank: https://data.worldbank.org
- Project template: https://github.com/OpenSourceEconomics/econ-project-templates

Author: Aksoltan Seyidova — Personal Project, University of Bonn, 2026
