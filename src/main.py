from extract import extract_data
from transform import transform_data


def main():
    file_path = "data/employees.csv"

    df = extract_data(file_path)

    df = transform_data(df)

    print("\nFinal Data")

    print(df)

    print("\nTotal Records After Cleaning:", len(df))


if __name__ == "__main__":
    main()