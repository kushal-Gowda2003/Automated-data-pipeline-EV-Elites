import seaborn as sns
import matplotlib.pyplot as plt

def plot_missing_values(before, after):

    plt.figure(figsize=(10,4))

    plt.subplot(1,2,1)
    sns.heatmap(before.isnull(), cbar=False)
    plt.title("Before Cleaning")

    plt.subplot(1,2,2)
    sns.heatmap(after.isnull(), cbar=False)
    plt.title("After Cleaning")

    plt.savefig("missing_values_comparison.png")
    plt.close()


def plot_distribution(data):

    num_cols = data.select_dtypes(include=['float64','int64']).columns

    if len(num_cols) == 0:
        print("No numeric columns for distribution plot")
        return

    for col in num_cols:
        plt.figure()
        sns.histplot(data[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.savefig(f"{col}_distribution.png")
        plt.close()