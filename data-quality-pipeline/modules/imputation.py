from sklearn.impute import SimpleImputer, KNNImputer
import numpy as np

def impute_missing_values(data):

    num_cols = data.select_dtypes(include=['float64','int64']).columns
    cat_cols = data.select_dtypes(include=['object']).columns

    # 🔹 Handle Numerical Columns
    if len(num_cols) > 0:

        # Check missing percentage
        missing_percent = data[num_cols].isnull().mean().mean()

        if missing_percent < 0.2:
            print("Using KNN Imputer for numerical data...")
            knn_imputer = KNNImputer(n_neighbors=3)
            data[num_cols] = knn_imputer.fit_transform(data[num_cols])
        else:
            print("Using Median Imputer for numerical data...")
            num_imputer = SimpleImputer(strategy="median")
            data[num_cols] = num_imputer.fit_transform(data[num_cols])

    # 🔹 Handle Categorical Columns
    if len(cat_cols) > 0:
        cat_imputer = SimpleImputer(strategy="most_frequent")
        data[cat_cols] = cat_imputer.fit_transform(data[cat_cols])

    return data