import pandas as pd
from datetime import datetime


def parse_timestamp(ts_string):
    """
    Parse a timestamp string into a datetime object.
    Supports multiple timestamp formats used across labs.
    """
    formats = ["%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M", "%Y-%m-%dT%H:%M:%S"]
    for fmt in formats:
        try:
            return datetime.strptime(ts_string, fmt)
        except ValueError:
            continue
    return None


def normalise_column_names(df):
    """
    Standardise all column names to lowercase and underscore-separated format.
    """
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
        .str.replace(r"[^\w_]", "", regex=True)
    )
    return df


def load_and_parse_data(file_path):
    """
    Load raw CSV data and normalise the structure.
    Returns a DataFrame with timestamp parsed and columns cleaned.
    """
    df = pd.read_csv(file_path, encoding="utf-8")

    df = normalise_column_names(df)

    if "timestamp" in df.columns:
        df["timestamp_parsed"] = df["timestamp"].apply(parse_timestamp)

    return df
