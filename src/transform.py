import pandas as pd


def transform_data(df):
    print("\nStarting Transformation...")

    initial_count = len(df)

    # Remove duplicates
    df = df.drop_duplicates()

    final_count = len(df)

    print(f"Duplicates Removed: {initial_count - final_count}")

    # Fill missing salary
    missing_salary_count = df["salary"].isna().sum()

    df["salary"] = df["salary"].fillna(0)

    print(f"Missing Salaries Fixed: {missing_salary_count}")

    # Convert joining date
    df["joining_date"] = pd.to_datetime(df["joining_date"])

    print("Transformation Completed")

    return df