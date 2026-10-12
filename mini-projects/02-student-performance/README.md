# Project 2 — Student Performance Analysis

| | |
|---|---|
| **Dataset** | `datasets/student_performance.csv` (see the [data dictionary](../../datasets/README.md#2-student_performancecsv--246-rows--13-columns)) |
| **Notebook** | `student_performance_analysis.ipynb` (starter, contains every task) |
| **Duration** | 1 week |
| **Objective** | Understand the factors affecting academic performance |

## Scenario
The Head of the CSE department wants to understand last semester's results for Sections A and B before planning
remedial classes. *Which subjects are hardest, how much does attendance matter, and which students need help now?*

## Rules
- A subject is passed with **40 or more** marks out of 100. An absent subject counts as not passed.
- A student **passes overall** only if all five subjects are passed.
- Minimum attendance requirement: **75%**.
- Grades are based on percentage: O ≥ 90 · A+ 80–89 · A 70–79 · B+ 60–69 · B 50–59 · C 40–49 · F < 40 or failed overall.

## Tasks
| Section | Task | What you deliver |
|---|---|---|
| A. Data preparation | 1. Load and inspect | List of every data-quality problem |
| | 2. Clean the data | Duplicates, Gender, impossible values → NaN; missing marks kept as absent |
| B. Subject-wise analysis | 3. Subject averages | Statistics table; section-wise bar chart; hardest subject |
| | 4. Totals and result | `Total`, `Percentage`, `Subjects_Passed`, `Result` per student |
| C. Pass / fail | 5. Pass rates | By subject (chart), overall, and by Section / Gender / Accommodation / Internet |
| | 6. Failed subjects | How many subjects failing students failed |
| D. Attendance & marks | 7. Correlation | r values; scatter with regression and the 75% line; attendance bands |
| | 8. Heatmap | Correlation matrix of factors and subjects |
| E. Grades | 9. Grade distribution | Grades; histogram of percentage; count plot of grades by section |
| F. Support | 10. At-risk students | Students with attendance < 75% **and** an overall Fail |
| G. Conclusions | 11. Insights | ≥ 5 insights with numbers, 3 recommendations, what the data cannot prove |

## Skills assessed
Handling impossible and missing values correctly · row-wise calculations · `pd.cut` for bands and grades ·
correlation analysis · distribution plots · responsible interpretation (correlation ≠ causation).

## Tip
`NaN >= 40` evaluates to `False`. That means `(df[SUBJECTS] >= 40).sum(axis=1)` already treats an absent subject as not passed.
