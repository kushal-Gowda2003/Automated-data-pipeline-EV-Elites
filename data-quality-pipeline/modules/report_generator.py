from ydata_profiling import ProfileReport

def generate_report(data):

    profile = ProfileReport(data, title="My Data Quality Report", explorative=True)
    profile.to_file("data_report.html")