from datetime import datetime
import pandas as pd
import os

from cleaning import clean_experiment_data
from validation import run_integrity_checks
from reporting import export_cleaned_data_and_summary


def main():
    print("🔬 Sci-Cle Log Processor Initialising...")

    # Load raw experiment data
    raw_data_path = os.path.join("data", "experiment_logs.csv")
    try:
        df = pd.read_csv(raw_data_path, encoding="utf-8")
        print("✅ Raw experiment logs loaded.")
    except Exception as e:
        print(f"❌ Failed to load data: {e}")
        return

    # Step 1: Clean the data
    print("🔄 Cleaning experiment data...")
    df_cleaned = clean_experiment_data(df)
    print("✅ Cleaning complete.")

    # Step 2: Run integrity checks
    print("🔍 Running integrity checks...")
    df_validated, summary_stats = run_integrity_checks(df_cleaned)
    print("✅ Integrity verification complete.")

    # Step 3: Export cleaned dataset and summary report
    print("💾 Exporting cleaned logs and summary report...")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_folder = os.path.join("outputs", f"experiment_run_{timestamp}")
    os.makedirs(output_folder, exist_ok=True)
    export_cleaned_data_and_summary(df_validated, summary_stats, output_folder)

    print("🎉 All tasks complete. Files saved in:", output_folder)


if __name__ == "__main__":
    main()
