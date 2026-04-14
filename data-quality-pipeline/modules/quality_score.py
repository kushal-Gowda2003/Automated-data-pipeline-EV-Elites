def calculate_quality_score(original, cleaned):

    total_cells = original.shape[0] * original.shape[1]

    # Missing values
    missing_before = original.isnull().sum().sum()
    missing_after = cleaned.isnull().sum().sum()

    missing_score = 0
    if missing_before != 0:
        missing_score = (missing_before - missing_after) / missing_before

    # Duplicates
    duplicates_before = original.duplicated().sum()
    duplicates_after = cleaned.duplicated().sum()

    duplicate_score = 0
    if duplicates_before != 0:
        duplicate_score = (duplicates_before - duplicates_after) / duplicates_before

    # Outlier / row reduction effect
    row_score = (len(original) - len(cleaned)) / len(original)

    # Weighted score (total = 1)
    final_score = (
            missing_score * 0.5 +
            duplicate_score * 0.3 +
            row_score * 0.2
    )

    return round(final_score * 100, 2)