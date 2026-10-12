"""
Generate the three practice datasets used in this repository.

The datasets are synthetic but realistic: they follow believable seasonal
patterns and relationships, and they deliberately contain the kinds of
problems found in real data (missing values, duplicate rows, inconsistent
text, wrong data types and impossible values) so that students can practise
data cleaning.

Run from the repository root:

    python datasets/generate_datasets.py

The random seed is fixed, so the files are reproduced exactly every time.
"""

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
OUT_DIR = Path(__file__).resolve().parent


# ---------------------------------------------------------------------------
# 1. Sales data
# ---------------------------------------------------------------------------
def make_sales(rng: np.random.Generator) -> pd.DataFrame:
    products = {
        # category: [(product, base unit price in Rs.)]
        "Electronics": [("Laptop", 52000), ("Smartphone", 18000), ("Headphones", 2500),
                        ("Smartwatch", 6500), ("Monitor", 11000)],
        "Furniture": [("Office Chair", 7500), ("Study Table", 9000),
                      ("Bookshelf", 5500), ("Sofa", 32000)],
        "Office Supplies": [("Notebook Pack", 250), ("Printer Ink", 1200),
                            ("Stapler", 180), ("Whiteboard", 1600), ("Pen Set", 120)],
        "Clothing": [("T-Shirt", 600), ("Jeans", 1500), ("Jacket", 2800), ("Saree", 3500)],
    }
    regions = {
        "North": ["Delhi", "Lucknow", "Chandigarh"],
        "South": ["Hyderabad", "Chennai", "Bengaluru"],
        "East": ["Kolkata", "Bhubaneswar", "Patna"],
        "West": ["Mumbai", "Pune", "Ahmedabad"],
        "Central": ["Bhopal", "Nagpur", "Indore"],
    }
    region_weight = np.array([0.22, 0.30, 0.14, 0.24, 0.10])
    cat_weight = np.array([0.30, 0.15, 0.35, 0.20])
    # festive peak in Oct-Nov, slight dip mid-year
    month_weight = np.array([0.075, 0.07, 0.08, 0.075, 0.07, 0.065,
                             0.07, 0.08, 0.085, 0.11, 0.12, 0.10])
    month_weight = month_weight / month_weight.sum()

    n = 1200
    months = rng.choice(np.arange(1, 13), size=n, p=month_weight)
    days = [rng.integers(1, pd.Timestamp(2024, m, 1).days_in_month + 1) for m in months]
    dates = pd.to_datetime({"year": 2024, "month": months, "day": days})

    region_names = list(regions)
    rows = []
    for i in range(n):
        region = rng.choice(region_names, p=region_weight)
        city = rng.choice(regions[region])
        cat = rng.choice(list(products), p=cat_weight)
        prod, base = products[cat][rng.integers(len(products[cat]))]
        price = round(base * rng.uniform(0.9, 1.1), 2)
        qty_max = 3 if base > 5000 else 10
        qty = int(rng.integers(1, qty_max + 1))
        discount = rng.choice([0, 0.05, 0.10, 0.15, 0.20], p=[0.4, 0.2, 0.2, 0.12, 0.08])
        if dates[i].month in (10, 11) and discount < 0.10 and rng.random() < 0.5:
            discount = 0.10  # festive offers
        rows.append({
            "Order_ID": f"ORD{10001 + i}",
            "Order_Date": dates[i].strftime("%Y-%m-%d"),
            "Region": region,
            "City": city,
            "Customer_Segment": rng.choice(["Consumer", "Corporate", "Small Business"], p=[0.55, 0.30, 0.15]),
            "Category": cat,
            "Product": prod,
            "Quantity": qty,
            "Unit_Price": price,
            "Discount": discount,
            "Payment_Mode": rng.choice(["UPI", "Credit Card", "Debit Card", "Cash", "Net Banking"],
                                       p=[0.40, 0.22, 0.15, 0.13, 0.10]),
        })
    df = pd.DataFrame(rows).sort_values(["Order_Date", "Order_ID"]).reset_index(drop=True)

    # --- inject data-quality problems -------------------------------------
    df["Quantity"] = df["Quantity"].astype("float")
    df["Unit_Price"] = df["Unit_Price"].astype("object")
    idx = rng.choice(len(df), 20, replace=False)
    df.loc[idx, "Quantity"] = np.nan                                  # missing quantity
    idx = rng.choice(len(df), 12, replace=False)
    df.loc[idx, "Unit_Price"] = np.nan                                # missing price
    idx = rng.choice(len(df), 25, replace=False)
    df.loc[idx, "Unit_Price"] = ["Rs." + str(v) if pd.notna(v) else v
                                 for v in df.loc[idx, "Unit_Price"]]  # price stored as text
    idx = rng.choice(len(df), 40, replace=False)
    df.loc[idx, "Region"] = [rng.choice([r.lower(), r.upper(), r + " ", " " + r])
                             for r in df.loc[idx, "Region"]]          # messy region labels
    idx = rng.choice(len(df), 10, replace=False)
    df.loc[idx, "Customer_Segment"] = np.nan                          # missing segment
    dups = df.sample(15, random_state=SEED)                           # exact duplicate rows
    df = pd.concat([df, dups]).sort_values("Order_Date", kind="stable").reset_index(drop=True)
    return df


# ---------------------------------------------------------------------------
# 2. Student performance data
# ---------------------------------------------------------------------------
def make_students(rng: np.random.Generator) -> pd.DataFrame:
    n = 240
    section = np.repeat(["A", "B"], n // 2)
    gender = rng.choice(["Male", "Female"], size=n, p=[0.58, 0.42])
    attendance = np.clip(rng.normal(78, 11, n), 40, 100).round(1)
    study_hours = np.clip(rng.normal(10, 4, n), 1, 25).round(1)
    prev_gpa = np.clip(rng.normal(7.2, 1.0, n), 4.5, 10).round(2)
    internet = rng.choice(["Yes", "No"], size=n, p=[0.82, 0.18])
    hostel = rng.choice(["Hosteller", "Day Scholar"], size=n, p=[0.45, 0.55])

    ability = (attendance - 78) / 11 * 0.45 + (study_hours - 10) / 4 * 0.35 + (prev_gpa - 7.2) * 0.5
    subjects = {"Mathematics": (62, 15), "Physics": (64, 13), "Programming": (68, 14),
                "English": (72, 10), "Electronics": (60, 14)}
    df = pd.DataFrame({
        "Student_ID": [f"CSE{s}{i:03d}" for s, i in zip(section, np.tile(np.arange(1, n // 2 + 1), 2))],
        "Section": section,
        "Gender": gender,
        "Accommodation": hostel,
        "Internet_Access": internet,
        "Attendance_Pct": attendance,
        "Study_Hours_Per_Week": study_hours,
        "Previous_GPA": prev_gpa,
    })
    for subj, (mean, sd) in subjects.items():
        df[subj] = np.clip(mean + ability * sd * 0.8 + rng.normal(0, sd * 0.6, n), 5, 100).round().astype(int)

    # --- inject data-quality problems -------------------------------------
    for subj in subjects:
        df[subj] = df[subj].astype("float")
        idx = rng.choice(n, 4, replace=False)
        df.loc[idx, subj] = np.nan                                    # absent for exam
    idx = rng.choice(n, 18, replace=False)
    df.loc[idx, "Gender"] = df.loc[idx, "Gender"].map({"Male": "M", "Female": "F"})
    idx = rng.choice(n, 6, replace=False)
    df.loc[idx, "Gender"] = df.loc[idx, "Gender"].str.lower()
    df.loc[rng.choice(n, 3, replace=False), "Attendance_Pct"] = [104.0, 112.5, -5.0]   # impossible
    df.loc[rng.choice(n, 2, replace=False), "Mathematics"] = [-1.0, 150.0]            # entry errors
    df.loc[rng.choice(n, 5, replace=False), "Study_Hours_Per_Week"] = np.nan
    dups = df.sample(6, random_state=SEED)
    df = pd.concat([df, dups]).sort_values("Student_ID", kind="stable").reset_index(drop=True)
    return df


# ---------------------------------------------------------------------------
# 3. Weather data
# ---------------------------------------------------------------------------
def make_weather(rng: np.random.Generator) -> pd.DataFrame:
    dates = pd.date_range("2023-01-01", "2024-12-31", freq="D")
    doy = dates.dayofyear.to_numpy()
    month = dates.month.to_numpy()

    # (mean max temp, amplitude, peak day of year, temp range, humidity base,
    #  monthly rain probability, monthly mean rain on a wet day)
    cities = {
        "Hyderabad": dict(tmax=33, amp=5.5, peak=135, rng=10, hum=55,
                          p=[.02, .02, .05, .08, .15, .45, .55, .55, .50, .30, .10, .03],
                          r=[5, 5, 8, 10, 12, 14, 15, 17, 18, 14, 10, 5]),
        "Chennai": dict(tmax=33.5, amp=4.0, peak=150, rng=8, hum=72,
                        p=[.10, .03, .03, .05, .08, .25, .30, .35, .35, .55, .65, .40],
                        r=[8, 5, 5, 8, 10, 10, 11, 12, 13, 22, 28, 18]),
        "Delhi": dict(tmax=31, amp=10.5, peak=155, rng=12, hum=50,
                      p=[.12, .10, .08, .05, .08, .25, .55, .55, .35, .05, .03, .05],
                      r=[6, 6, 6, 5, 8, 14, 18, 17, 15, 8, 5, 5]),
        "Mumbai": dict(tmax=32, amp=2.5, peak=130, rng=7, hum=70,
                       p=[.01, .01, .01, .02, .05, .60, .85, .80, .60, .15, .05, .02],
                       r=[3, 3, 3, 5, 10, 28, 45, 30, 22, 12, 8, 3]),
    }
    frames = []
    for city, c in cities.items():
        seasonal = c["amp"] * np.cos(2 * np.pi * (doy - c["peak"]) / 365.25)
        p_rain = np.array(c["p"])[month - 1]
        wet = rng.random(len(dates)) < p_rain
        rain = np.where(wet, rng.gamma(1.5, np.array(c["r"])[month - 1] / 1.5), 0.0).round(1)
        cooling = np.where(wet, rng.uniform(1, 4, len(dates)), 0)    # rainy days are cooler
        tmax = (c["tmax"] + seasonal - cooling + rng.normal(0, 1.4, len(dates))).round(1)
        tmin = (tmax - c["rng"] + 0.4 * cooling + rng.normal(0, 1.2, len(dates))).round(1)
        hum = np.clip(c["hum"] + 30 * p_rain + np.where(wet, 8, 0)
                      + rng.normal(0, 6, len(dates)), 15, 100).round().astype(float)
        wind = np.clip(rng.gamma(4, 3, len(dates)) + 6 * p_rain, 1, None).round(1)
        frames.append(pd.DataFrame({"Date": dates.strftime("%Y-%m-%d"), "City": city,
                                    "Max_Temp_C": tmax, "Min_Temp_C": tmin,
                                    "Humidity_Pct": hum, "Rainfall_mm": rain,
                                    "Wind_Speed_kmh": wind}))
    df = pd.concat(frames, ignore_index=True)

    # --- inject data-quality problems -------------------------------------
    n = len(df)
    for col, k in [("Max_Temp_C", 70), ("Min_Temp_C", 65), ("Humidity_Pct", 90),
                   ("Rainfall_mm", 45), ("Wind_Speed_kmh", 30)]:
        df.loc[rng.choice(n, k, replace=False), col] = np.nan          # sensor gaps
    df.loc[rng.choice(n, 8, replace=False), "Max_Temp_C"] = -99.0      # sensor error code
    df.loc[rng.choice(n, 5, replace=False), "Humidity_Pct"] = -99.0
    dups = df.sample(10, random_state=SEED)
    df = pd.concat([df, dups]).sort_values(["City", "Date"], kind="stable").reset_index(drop=True)
    return df


def main() -> None:
    rng = np.random.default_rng(SEED)
    outputs = {
        "sales_data.csv": make_sales(rng),
        "student_performance.csv": make_students(rng),
        "weather_data.csv": make_weather(rng),
    }
    for name, df in outputs.items():
        df.to_csv(OUT_DIR / name, index=False)
        print(f"{name:<26} {df.shape[0]:>5} rows x {df.shape[1]} columns")


if __name__ == "__main__":
    main()
