import pandas as pd


def transform_data(df, logger):

    initial_count = len(df)

    df = df.drop_duplicates()

    logger.info(
        f"Duplicates Removed: {initial_count - len(df)}"
    )

    missing_salary_count = df["salary"].isna().sum()

    df["salary"] = df["salary"].fillna(0)

    logger.info(
        f"Missing Salaries Fixed: {missing_salary_count}"
    )

    df["joining_date"] = pd.to_datetime(
        df["joining_date"]
    )

    return df