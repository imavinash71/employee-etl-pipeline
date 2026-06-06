from extract import extract_data
from transform import transform_data
from load import load_data
from config import DB_CONFIG
from logger import setup_logger


def main():

    logger = setup_logger()

    try:

        file_path = "data/employees.csv"

        df = extract_data(
            file_path,
            logger
        )

        df = transform_data(
            df,
            logger
        )

        load_data(
            df,
            DB_CONFIG,
            logger
        )

        print("Pipeline completed successfully")

    except Exception as e:

        logger.error(
            f"Pipeline failed: {e}"
        )

        print(
            f"Pipeline failed: {e}"
        )

        print(
            "DB_CONFIG =",
            DB_CONFIG
        )


if __name__ == "__main__":
    main()