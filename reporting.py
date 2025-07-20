import os
from analyze import compute_group_stats, calculate_cv
from visualise import plot_measurements_by_condition, plot_measurement_over_time
from generate_report import create_report


def export_cleaned_data_and_summary(df_validated, summary_stats, output_folder):
    """
    Generate figures and final report for experiment results.

    Parameters:
        df_validated (pd.DataFrame): The cleaned + validated dataset
        summary_stats (pd.DataFrame): Group-level statistics
        output_folder (str): Folder to save report and assets
    """

    # 1. Save cleaned data
    cleaned_path = os.path.join(output_folder, "cleaned_data.csv")
    df_validated.to_csv(cleaned_path, index=False)
    print(f"📄 Cleaned data saved to: {cleaned_path}")

    # 2. Save summary stats
    stats_path = os.path.join(output_folder, "summary_stats.csv")
    summary_stats.to_csv(stats_path, index=False)
    print(f"📊 Summary stats saved to: {stats_path}")

    # 3. Generate visualisations
    vis_folder = os.path.join(output_folder, "figures")
    os.makedirs(vis_folder, exist_ok=True)

    fig_paths = []
    fig_paths.append(plot_measurements_by_condition(df_validated, 'measurement_1', 'condition', vis_folder))
    fig_paths.append(plot_measurements_by_condition(df_validated, 'measurement_2', 'condition', vis_folder))
    fig_paths.append(plot_measurement_over_time(df_validated, 'sample_id', 'timestamp_parsed', 'measurement_1', vis_folder))
    fig_paths.append(plot_measurement_over_time(df_validated, 'sample_id', 'timestamp_parsed', 'measurement_2', vis_folder))

    # 4. Generate the final DOCX report
    report_path = os.path.join(output_folder, "final_report.docx")
    create_report(
        template_path="templates/report_template.docx",
        output_path=report_path,
        stats_df=summary_stats,
        figure_paths=fig_paths,
        metadata={
            "title": "Biological Experiment Report",
            "author": "Sci-Cle Automation System",
            "date": None,
            "description": "This report summarises key outcomes and statistics from an automated experiment log analysis."
        }
    )
