import pandas as pd


def extract_data(file_path, logger):
    try:
        df = pd.read_csv(file_path)

        logger.info(
            f"Extracted {len(df)} records from CSV"
        )

        return df

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise

    except Exception as e:
        logger.error(f"Error during extraction: {e}")
        raise