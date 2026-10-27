"""Test whether 2023 U.S. egg production differs by season."""

from pathlib import Path

import pandas as pd
from scipy.stats import f_oneway


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "egg_data.csv"
SEASON_MAP = {
    "DEC": "Winter", "JAN": "Winter", "FEB": "Winter",
    "MAR": "Spring", "APR": "Spring", "MAY": "Spring",
    "JUN": "Summer", "JUL": "Summer", "AUG": "Summer",
    "SEP": "Fall", "OCT": "Fall", "NOV": "Fall",
}


def main():
    df = pd.read_csv(DATA)
    df = df[df["Year"].eq(2023)].copy()
    df["Value"] = pd.to_numeric(df["Value"].astype(str).str.replace(",", "", regex=False), errors="coerce")
    df = df.dropna(subset=["Value", "Period"])
    df["season"] = df["Period"].map(SEASON_MAP)
    groups = [group["Value"].to_numpy() for _, group in df.groupby("season")]
    statistic, p_value = f_oneway(*groups)
    print(f"Rows analyzed: {len(df):,}")
    print(df.groupby("season")["Value"].agg(["count", "mean", "std"]).round(0))
    print(f"One-way ANOVA: F={statistic:.3f}, p={p_value:.3f}")
    print("Conclusion: no statistically significant seasonal difference at alpha=0.05." if p_value >= 0.05 else "Conclusion: seasonal differences are statistically significant at alpha=0.05.")


if __name__ == "__main__":
    main()
