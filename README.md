# Python & Data Analytics – Practice Sets and Mini-Projects

**Course:** Python & Data Analytics (NumPy, Pandas, Data Visualization)
**Program:** B.Tech Technical Training – CSE A & B
**Trainer:** Dr. Anil Kumar
**Institution:** [Institution Name]

---

## 1. About This Repository

This repository contains practice sets, real-world datasets and guided mini-projects for the Python & Data Analytics course. It is designed to help students strengthen their understanding of NumPy, Pandas, Matplotlib and Seaborn through hands-on, application-oriented work.

## 2. Learning Objectives

After completing the material in this repository, students will be able to:

- Apply NumPy for array creation, indexing, broadcasting and vectorised operations
- Clean and transform raw data using Pandas (missing values, duplicates, formatting issues)
- Perform grouping, aggregation and merging on real-world datasets
- Create meaningful visualisations using Matplotlib and Seaborn
- Present insights from an end-to-end data analysis workflow

## 3. Repository Structure

```
python-data-analytics-practice/
│
├── datasets/
│   ├── README.md                     (data dictionary + known data-quality issues)
│   ├── generate_datasets.py          (reproducible generator, fixed seed)
│   ├── sales_data.csv
│   ├── student_performance.csv
│   └── weather_data.csv
│
├── practice-sets/
│   ├── level-1-basic/
│   │   ├── README.md
│   │   └── level1_numpy_and_loading.ipynb
│   ├── level-2-intermediate/
│   │   ├── README.md
│   │   └── level2_cleaning_grouping_merging.ipynb
│   └── level-3-advanced/
│       ├── README.md
│       └── level3_visualisation_and_analysis.ipynb
│
├── mini-projects/
│   ├── 01-sales-analysis/
│   │   ├── README.md
│   │   └── sales_analysis.ipynb
│   ├── 02-student-performance/
│   │   ├── README.md
│   │   └── student_performance_analysis.ipynb
│   └── 03-weather-analysis/
│       ├── README.md
│       └── weather_analysis.ipynb
│
├── solutions/                        (released after review)
│   ├── README.md
│   ├── practice-sets/                (level1–3 solution notebooks)
│   └── mini-projects/                (project solution notebooks)
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 4. Practice Sets

| Level | Focus Area | Topics Covered | Exercises | Notebook |
|-------|-----------|----------------|-----------|----------|
| **Level 1 – Basic** | Foundations | Loading data, NumPy arrays, basic statistics | 17 | [`level1_numpy_and_loading.ipynb`](practice-sets/level-1-basic/) |
| **Level 2 – Intermediate** | Data handling | Data cleaning, `.loc` / `.iloc`, groupby, merging | 19 | [`level2_cleaning_grouping_merging.ipynb`](practice-sets/level-2-intermediate/) |
| **Level 3 – Advanced** | Applied analysis | End-to-end analysis, visualisation, insight reporting | 15 | [`level3_visualisation_and_analysis.ipynb`](practice-sets/level-3-advanced/) |

Students should complete the levels in order. Each exercise has a collapsible hint, and each level ends with a self-check list.

## 5. Mini-Projects

Each project folder has a README with the scenario and task list, and a starter notebook with one section per task.

### Project 1: Sales Analysis ([folder](mini-projects/01-sales-analysis/))
- **Dataset:** `sales_data.csv`
- **Objective:** Analyse sales performance and identify business insights
- **Tasks:** Revenue trends, top-performing products, regional comparison, monthly sales visualisation

### Project 2: Student Performance Analysis ([folder](mini-projects/02-student-performance/))
- **Dataset:** `student_performance.csv`
- **Objective:** Understand factors affecting academic performance
- **Tasks:** Subject-wise averages, pass/fail analysis, correlation between attendance and marks, grade distribution plots

### Project 3: Weather Analysis ([folder](mini-projects/03-weather-analysis/))
- **Dataset:** `weather_data.csv`
- **Objective:** Explore weather patterns and trends
- **Tasks:** Handling missing values, temperature trends, seasonal analysis, rainfall visualisation

## 6. Getting Started

### Prerequisites
- Python 3.9 or higher
- Jupyter Notebook or JupyterLab
- Git (optional but recommended)

### Setup Instructions

1. **Clone the repository**
```bash
   git clone https://github.com/[your-username]/python-data-analytics-practice.git
   cd python-data-analytics-practice
```

2. **Install the required libraries**
```bash
   pip install -r requirements.txt
```

3. **Launch Jupyter Notebook**
```bash
   jupyter notebook
```

4. **Start with** `practice-sets/level-1-basic/level1_numpy_and_loading.ipynb` and run the setup cell first.
   Every notebook reads data from `../../datasets/`, so open notebooks from their own folder and do not move them.

### Required Libraries
```
numpy>=1.24
pandas>=2.2
matplotlib>=3.7
seaborn>=0.13
jupyter>=1.0
```

## 7. Submission Guidelines

1. Fork this repository to your own GitHub account
2. Complete each project in its starter notebook (`.ipynb`) in the project folder
3. Include comments, markdown explanations and a short summary of insights
4. Push your work to your forked repository
5. Share the repository link with the trainer before the deadline

| Project | Duration | Deadline |
|---------|----------|----------|
| Sales Analysis | 1 week | [Date] |
| Student Performance | 1 week | [Date] |
| Weather Analysis | 1 week | [Date] |

## 8. Evaluation Rubric

| Criteria | Weightage |
|----------|-----------|
| Data cleaning and preparation | 25% |
| Correct use of NumPy and Pandas | 25% |
| Quality of visualisations | 20% |
| Code readability and documentation | 15% |
| Insights and conclusions | 15% |

## 9. Guidelines for Students

- Attempt every task before viewing the solutions
- Write clean, well-commented code
- Do not copy code from classmates; originality is expected
- Ask for help early if you are stuck

## 10. Dataset Sources and Acknowledgements

| Dataset | Source |
|---------|--------|
| Sales Data | Synthetic, generated by `datasets/generate_datasets.py` (seed 42) |
| Student Performance | Synthetic, generated by `datasets/generate_datasets.py` (seed 42) |
| Weather Data | Synthetic, generated by `datasets/generate_datasets.py` (seed 42); seasonal patterns modelled on typical Indian climate |

The datasets are synthetic, so there are no licence or privacy restrictions. They are built to look realistic and include
**deliberate data-quality problems** (duplicates, inconsistent labels, wrong data types, impossible values and missing values)
for cleaning practice. See [`datasets/README.md`](datasets/README.md) for the full data dictionary.
To replace them with real data (e.g. Kaggle Superstore Sales, UCI Student Performance, Open-Meteo / IMD), keep the same
file and column names, or update the notebooks to match.

## 11. Contact

For queries or support:

**Anil Kumar**
Email: [anildamaraju@gmail.com]
Department: [Department Name]

---

*Last updated: October 2026*