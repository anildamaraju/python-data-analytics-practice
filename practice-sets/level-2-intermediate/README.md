# Level 2 — Intermediate: Cleaning, Selecting, Grouping and Merging

**Notebook:** `level2_cleaning_grouping_merging.ipynb` &nbsp;·&nbsp; **Datasets:** `sales_data.csv`, `student_performance.csv`
&nbsp;·&nbsp; **Suggested time:** 5–6 hours &nbsp;·&nbsp; **Prerequisite:** Level 1

## Topics
- Finding data-quality problems: `info`, `describe(include='all')`, `unique`, `isna`, `duplicated`
- Cleaning text (`.str.strip().str.title()`), converting types (`pd.to_numeric`, `pd.to_datetime`)
- Filling missing values with group-wise statistics (`groupby(...).transform('median')`)
- Date parts with the `.dt` accessor
- Label-based (`.loc`) vs position-based (`.iloc`) selection
- `groupby` with named aggregation, `pivot_table`, top-N within groups
- `merge` with inner / left / outer joins and `indicator=True`
- Saving cleaned data with `to_csv(index=False)`

## Exercises
| Part | Exercises |
|---|---|
| A. Inspecting raw data | 2.1 First inspection · 2.2 Missing values · 2.3 Duplicates |
| B. Cleaning | 2.4 Inconsistent text · 2.5 Numbers stored as text · 2.6 Missing values · 2.7 Dates · 2.8 Calculated column |
| C. Selecting | 2.9 `.loc` · 2.10 `.iloc` |
| D. Grouping | 2.11 Revenue by region · 2.12 Named aggregation · 2.13 Pivot table · 2.14 Top-N per group |
| E. Merging | 2.15 Targets table · 2.16 Join types |
| F. Student data | 2.17 Clean the student data · 2.18 Merge mentors · 2.19 Save cleaned data |

> Files you save in 2.19 (`*_clean.csv`) are ignored by Git (see `.gitignore`), so they will not be committed by accident.
