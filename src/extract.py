import pandas as pd


def extract_data(file_path):
    """
    Read data from CSV file.
    """

    df = pd.read_csv(file_path)

    print("\nData Extracted Successfully")
    print(df.head())

    return df