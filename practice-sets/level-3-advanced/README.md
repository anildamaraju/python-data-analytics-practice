# Level 3 — Advanced: Visualisation and End-to-End Analysis

**Notebook:** `level3_visualisation_and_analysis.ipynb` &nbsp;·&nbsp; **Datasets:** all three
&nbsp;·&nbsp; **Suggested time:** 5–6 hours &nbsp;·&nbsp; **Prerequisite:** Level 2

## Topics
- Matplotlib's figure / axes model, `plt.subplots`, `fig.suptitle`, `savefig`
- Seaborn: `histplot`, `boxplot`, `scatterplot`, `regplot`, `heatmap`, `barplot`, `countplot`, `catplot`
- Choosing the right chart for the question, and when to use a log scale
- Resampling time series (`resample('W')`) and rolling averages
- A complete workflow: question → check data → analyse → visualise → conclude
- Writing insights backed by numbers; correlation vs causation

## Exercises
| Part | Exercises |
|---|---|
| A. Visualisation toolkit | 3.1 Line · 3.2 Bar · 3.3 Histogram & log scale · 3.4 Box plot · 3.5 Scatter & regression · 3.6 Heatmap · 3.7 2×2 dashboard · 3.8 Saving figures |
| B. Case study: *Who buys, and how do they pay?* | 3.9 Frame questions · 3.10 Check data · 3.11–3.12 Analyse · 3.13 Visualise · 3.14 Conclude |
| C. Insight reporting | 3.15 Critique and redraw a poor chart |

## Chart checklist (applies to the mini-projects too)
- [ ] Title that says what the chart shows
- [ ] Axis labels **with units** (Rs. lakh, °C, %, mm)
- [ ] Legend whenever there is more than one series
- [ ] Sorted bars where order carries no meaning (largest first)
- [ ] No pie charts for more than 3–4 similar-sized parts
