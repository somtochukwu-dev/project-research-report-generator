import pandas as pd
import numpy as np
from analyze import compute_group_stats, calculate_cv


def validate_row(row):
    """
    Apply row-level integrity checks and return a status label.
    """
    if pd.isna(row['timestamp_parsed']):
        return "Invalid Timestamp"
    if pd.isna(row['measurement_1']) or pd.isna(row['measurement_2']):
        return "Missing Measurement"
    if row['measurement_1'] < 0 or row['measurement_2'] < 0:
        return "Negative Value"
    if row['status'] not in ['Success', 'Fail', 'Contaminated', 'Pending Review']:
        return "Invalid Status"
    return "OK"


def run_integrity_checks(df):
    """
    Validate experiment data and generate summary stats.

    Returns:
        - df with a new 'status_flag' column
        - group-level summary stats
    """
    df['status_flag'] = df.apply(validate_row, axis=1)

    # Cleaned subset for summary stats (exclude flagged rows)
    valid_df = df[df['status_flag'] == 'OK'].copy()

    # Compute group statistics
    group_summary = compute_group_stats(valid_df, group_col='condition', measurement_cols=['measurement_1', 'measurement_2'])
    group_summary = calculate_cv(group_summary, ['measurement_1_mean', 'measurement_2_mean'])

    return df, group_summary
