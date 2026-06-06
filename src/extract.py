import pandas as pd


def extract_data(file_path, logger):
    """
    Read data from CSV file.
    """

    df = pd.read_csv(file_path)

    logger.info(f"Extracted {len(df)} records from CSV")

    return df