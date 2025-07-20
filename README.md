# 🧪 Sci-Cle Research Report Generator

A Python-based automation system for cleaning, analysing, and reporting experimental biological data. Sci-Cle automatically processes raw experiment logs, validates data integrity, performs statistical analyses, and generates professional research reports in `.docx` format — complete with visualisations and summary statistics.

---

## 🚀 Features

✅ **Clean raw experimental logs**  
✅ **Validate and flag data issues** (missing values, invalid timestamps, etc.)  
✅ **Compute descriptive group-level statistics**  
✅ **Generate visualisations** (boxplots, line charts, etc.)  
✅ **Auto-build Word reports** using a customisable template  
✅ Fully automated end-to-end workflow from CSV to polished report  

---

## 🗂 Project Structure

sci-cle-research-report/
├── data/
│ └── experiment_logs.csv # Raw experiment data
├── outputs/
│ └── experiment_run_YYYY-MM-DD/ # Cleaned data, stats, figures, and reports
├── templates/
│ └── report_template.docx # Word template for reports
├── analyze.py # Statistical analyses
├── cleaning.py # Data cleaning functions
├── generate_report.py # DOCX report generator
├── main.py # Main automation pipeline
├── parser.py # Timestamp + column parsing utilities
├── reporting.py # Export logic for cleaned data & reports
├── validation.py # Data integrity checks
├── visualise.py # Matplotlib & seaborn charts
├── requirements.txt # Project dependencies
└── README.md # Project documentation



---

## ⚙️ Installation

1️⃣ **Clone this repository**

git clone https://github.com/yourusername/sci-cle-research-report.git
cd sci-cle-research-report
2️⃣ Install dependencies


pip install -r requirements.txt
3️⃣ Place your raw experiment data

Add your CSV file to the data/ folder as experiment_logs.csv.

4️⃣ (Optional) Customise the report template

Edit templates/report_template.docx to match your preferred style.

🧑‍🔬 Usage
Run the automation pipeline:

 
python main.py
✅ Cleaned data, summary statistics, charts, and a final research report will be saved in outputs/experiment_run_<timestamp>/.

📊 Example Outputs
Cleaned Dataset: outputs/cleaned_data.csv

Summary Statistics: outputs/summary_stats.csv

Visualisations:

Boxplots of measurements by condition

Line charts showing measurement trends over time

Final Report: outputs/final_report.docx

📦 Dependencies
pandas

numpy

matplotlib

seaborn

python-docx

Install all with:

 
pip install -r requirements.txt
🛡 Security
This system is designed for local processing of sensitive scientific data. It does not transmit data externally, making it suitable for private lab environments.

👨‍💻 Author
Somtochukwu O

License
This project is licensed for educational and portfolio purposes. Contact for commercial use.
