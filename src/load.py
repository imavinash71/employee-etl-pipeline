from sqlalchemy import create_engine
import pandas as pd


def load_data(df, config, logger):

    connection_string = (
        f"postgresql://{config['user']}:{config['password']}"
        f"@{config['host']}:{config['port']}/{config['database']}"
    )

    engine = create_engine(connection_string)

    existing_df = pd.read_sql(
        "SELECT emp_id FROM employees",
        engine
    )

    existing_ids = set(existing_df["emp_id"])

    new_df = df[
        ~df["emp_id"].isin(existing_ids)
    ]

    if new_df.empty:
        logger.info("No new records found")
        print("No new records found")
        return

    new_df.to_sql(
        "employees",
        engine,
        if_exists="append",
        index=False
    )

    logger.info(
        f"Loaded {len(new_df)} new records"
    )

    print(
        f"Loaded {len(new_df)} new records"
    )