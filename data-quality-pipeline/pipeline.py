from modules.data_loader import load_data
from modules.data_quality import check_data_quality, remove_duplicates
from modules.imputation import impute_missing_values
from modules.outlier_detection import remove_outliers
from modules.report_generator import generate_report
from modules.visualization import plot_missing_values, plot_distribution
from modules.quality_score import calculate_quality_score

def run_pipeline(file):
    print("\n--- Starting Pipeline ---")

    # Load data
    data = load_data(file)
    if data is None:
        return

    original_data = data.copy()

    # Data Quality Check
    print("\nChecking Data Quality...")
    report = check_data_quality(data)

    print("\nMissing Values:\n", report["missing_values"])
    print("\nDuplicates:", report["duplicates"])
    print("\nData Types:\n", report["data_types"])

    # Remove duplicates
    print("\nRemoving duplicates...")
    data = remove_duplicates(data)

    # Impute missing values
    print("\nImputing missing values...")
    data = impute_missing_values(data)

    # Remove outliers
    print("\nRemoving outliers...")
    data = remove_outliers(data)

    # Final check
    print("\nFinal Dataset Shape:", data.shape)
    print("\nFinal Missing Values:\n", data.isnull().sum())

    # 🔹 Visualizations (Correct usage)
    print("\nGenerating visualizations...")
    plot_missing_values(original_data, data)
    plot_distribution(data)

    # Generate report
    print("\nGenerating report...")
    generate_report(data)
    score = calculate_quality_score(original_data, data)
    print(f"\n📊 Data Quality Score: {score}%")
    # Save clean data
    data.to_csv("clean_data.csv", index=False)

    print("\n✅ Pipeline completed successfully!")
    print("📁 Output files: clean_data.csv, data_report.html, images")


if __name__ == "__main__":
    run_pipeline("data/ev_messy_dataset.csv")