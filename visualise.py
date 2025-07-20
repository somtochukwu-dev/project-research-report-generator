import os
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

def save_output_plot(fig, filename, output_folder):
    """
    Save a matplotlib figure to a specified output folder.
    """
    os.makedirs(output_folder, exist_ok=True)
    filepath = os.path.join(output_folder, filename)
    fig.savefig(filepath, bbox_inches='tight')
    plt.close(fig)
    return filepath


def plot_measurements_by_condition(df, measurement_col, condition_col, output_folder):
    """
    Create a boxplot for a measurement column grouped by condition.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(data=df, x=condition_col, y=measurement_col, ax=ax, palette="Set2")
    sns.stripplot(data=df, x=condition_col, y=measurement_col, ax=ax, color='black', size=3, jitter=True, alpha=0.4)
    ax.set_title(f"{measurement_col.replace('_', ' ').title()} by {condition_col.title()}")
    ax.set_ylabel("Value")
    ax.set_xlabel(condition_col.title())
    return save_output_plot(fig, f"{measurement_col}_by_{condition_col}.png", output_folder)


def plot_measurement_over_time(df, sample_col, time_col, measurement_col, output_folder):
    """
    Line plot showing how a measurement evolves over time by sample.
    """
    df_sorted = df.sort_values(by=time_col)
    fig, ax = plt.subplots(figsize=(10, 5))
    for sid in df_sorted[sample_col].unique():
        sub = df_sorted[df_sorted[sample_col] == sid]
        ax.plot(sub[time_col], sub[measurement_col], alpha=0.4)
    ax.set_title(f"{measurement_col.replace('_', ' ').title()} Over Time")
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Measurement Value")
    ax.tick_params(axis='x', rotation=45)
    return save_output_plot(fig, f"{measurement_col}_over_time.png", output_folder)
