def check_data_quality(data):

    report = {}

    report["missing_values"] = data.isnull().sum()
    report["duplicates"] = data.duplicated().sum()
    report["data_types"] = data.dtypes

    return report


def remove_duplicates(data):
    return data.drop_duplicates()