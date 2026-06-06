from extract import extract_data
from transform import transform_data
from load import load_data
from config import DB_CONFIG


def main():
    file_path = "data/employees.csv"

    df = extract_data(file_path)

    df = transform_data(df)

    load_data(df, DB_CONFIG)


if __name__ == "__main__":
    main()