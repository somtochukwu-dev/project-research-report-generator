import pandas as pd


def compute_group_stats(df, group_col, measurement_cols):
    """
    Compute descriptive statistics grouped by a categorical variable (e.g. 'condition').

    Parameters:
        df (pd.DataFrame): Cleaned experiment data
        group_col (str): Column to group by (e.g., 'condition')
        measurement_cols (list): List of measurement columns (e.g., ['measurement_1', 'measurement_2'])

    Returns:
        pd.DataFrame: Summary stats by group
    """
    stats = []

    for col in measurement_cols:
        group_summary = df.groupby(group_col)[col].agg(
            count='count',
            mean='mean',
            std='std',
            min='min',
            max='max'
        ).reset_index()
        group_summary.columns = [group_col] + [f"{col}_{metric}" for metric in group_summary.columns[1:]]
        stats.append(group_summary)

    # Merge all summaries on the group_col
    summary = stats[0]
    for s in stats[1:]:
        summary = pd.merge(summary, s, on=group_col)

    return summary.round(3)


def calculate_cv(df, measurement_cols):
    """
    Add Coefficient of Variation (CV%) for each measurement column.

    Parameters:
        df (pd.DataFrame): Cleaned data
        measurement_cols (list): Columns to calculate CV%

    Returns:
        pd.DataFrame: Data with CV columns added
    """
    for col in measurement_cols:
        mean = df[col].mean()
        std = df[col].std()
        if mean != 0:
            df[f"{col}_cv%"] = round((std / mean) * 100, 2)
        else:
            df[f"{col}_cv%"] = None
    return df
