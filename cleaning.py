import pandas as pd
from parser import parse_timestamp, normalise_column_names


def clean_experiment_data(df):
    """
    Clean and standardise biological experiment logs.

    Steps:
    - Normalise column names
    - Trim strings
    - Convert timestamps
    - Handle missing or malformed fields
    - Convert measurements to numeric
    """
    df = normalise_column_names(df)

    # Drop completely empty rows
    df.dropna(how='all', inplace=True)

    # Strip whitespace from string columns
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip()

    # Convert measurement columns to numeric
    for col in ['measurement_1', 'measurement_2']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Parse timestamps into datetime objects
    if 'timestamp' in df.columns:
        df['timestamp_parsed'] = df['timestamp'].apply(parse_timestamp)
        df['timestamp_parsed'] = pd.to_datetime(df['timestamp_parsed'], errors='coerce')

    # Standardise status field (capitalised)
    if 'status' in df.columns:
        df['status'] = df['status'].str.title()

    # Fill NAs in non-critical columns with 'Unknown' where relevant
    for col in ['researcher', 'condition', 'observation', 'status']:
        if col in df.columns:
            df[col] = df[col].fillna('Unknown')

    return df
