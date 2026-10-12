# Project 1 — Sales Analysis

| | |
|---|---|
| **Dataset** | `datasets/sales_data.csv` (see the [data dictionary](../../datasets/README.md#1-sales_datacsv--1215-rows--11-columns)) |
| **Notebook** | `sales_analysis.ipynb` (starter, contains every task) |
| **Duration** | 1 week |
| **Objective** | Analyse sales performance and identify business insights |

## Scenario
You have joined the analytics team of a retail chain with outlets in 15 Indian cities. The head of sales wants a review of
2024 before planning next year's budget. The questions are: *Where does our revenue come from, when do we sell the most,
and where should we focus?*

## Tasks
| Section | Task | What you deliver |
|---|---|---|
| A. Data preparation | 1. Load and inspect | List of every data-quality problem |
| | 2. Clean the data | Each fix + a check proving it worked + justification |
| | 3. Feature engineering | `Revenue`, `Gross_Value`, `Discount_Amount`, `Month`, `Month_Name`, `Quarter` |
| B. Overview | 4. KPIs | Revenue, orders, units, AOV, discount given, effective discount rate |
| C. Revenue trends | 5. Monthly trend | Monthly revenue + MoM growth table; line chart with best and worst months marked; strongest quarter |
| D. Products & categories | 6. Top products | Top 10 by revenue vs top 10 by units; bar chart coloured by category |
| | 7. Category performance | Revenue share, AOV, discount dependence |
| E. Regional comparison | 8. Regions | Region table; region × category heatmap; best city per region |
| F. Monthly visualisation | 9. Monthly sales | Stacked monthly bar by category; month × region heatmap |
| G. Conclusions | 10. Insights | ≥ 5 insights with numbers, 3 recommendations, limitations |

## Skills assessed
Cleaning text, number and date columns · group-wise imputation · `groupby` / `pivot_table` · time-based aggregation ·
bar, line and heatmap charts · business communication.

## Tips
- Report money in **lakhs** (Rs. 1,00,000) so numbers stay readable.
- `Month_Name` sorts alphabetically (Apr, Aug, Dec …) unless you make it an *ordered categorical*.
- Volume (units) and value (revenue) answer different questions. Do not mix them up.
