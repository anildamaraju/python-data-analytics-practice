# Project 3 — Weather Analysis

| | |
|---|---|
| **Dataset** | `datasets/weather_data.csv` (see the [data dictionary](../../datasets/README.md#3-weather_datacsv--2934-rows--7-columns)) |
| **Notebook** | `weather_analysis.ipynb` (starter, contains every task) |
| **Duration** | 1 week |
| **Objective** | Explore weather patterns and trends |

## Scenario
A city-planning consultancy wants a comparison of the climate in four major Indian cities to support decisions on
water supply, drainage and outdoor events. *How do temperature and rainfall vary across cities and seasons?*

## Definitions
- **Seasons:** Winter Dec–Feb · Summer Mar–May · Monsoon Jun–Sep · Post-monsoon Oct–Nov
- **Rainy day:** rainfall ≥ 2.5 mm (the India Meteorological Department's definition)
- **`-99`** is a sensor error code, not a reading

## Tasks
| Section | Task | What you deliver |
|---|---|---|
| A. Data preparation | 1. Load and inspect | Date range, rows per city, duplicates, missing values, error codes |
| | 2. Missing values | Remove duplicates; `-99` → NaN; interpolate within each city; justified rainfall strategy |
| | 3. Feature engineering | `Year`, `Month`, `Month_Name`, `Season`, `Temp_Range`, `Rainy_Day` |
| B. Temperature trends | 4. Monthly profile | Line chart per city; seasonal swing per city |
| | 5. Smoothing | Delhi daily max temperature + 30-day rolling mean; hottest and coldest days per city |
| | 6. Year-on-year | 2023 vs 2024 comparison, with a note on what counts as a meaningful difference |
| C. Seasonal analysis | 7. Season × city | Summary table; box plot of max temperature by season |
| | 8. Rain by season | 100% stacked bar of the seasonal rainfall share; explain Chennai |
| D. Rainfall visualisation | 9. Monthly rainfall | Faceted bar charts + city × month heatmap; wettest city-month |
| | 10. Rain vs temperature | Rainy vs dry monsoon days: temperature and humidity |
| E. Conclusions | 11. Insights | ≥ 5 insights with numbers, a practical use, limitations |

## Skills assessed
Time-series handling (`parse_dates`, `resample`, `rolling`) · interpolation within groups · custom season mapping ·
faceted charts and heatmaps · domain reasoning.

## Tips
- Always sort by `City` and `Date` before interpolating, and interpolate **within** each city (`groupby(...).transform`).
  Otherwise Chennai's last day will be filled using Delhi's first day.
- Rainfall should not be interpolated: rain does not change smoothly from day to day.
