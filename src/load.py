from sqlalchemy import create_engine


def load_data(df, config):
    connection_string = (
        f"postgresql://{config['user']}:{config['password']}"
        f"@{config['host']}:{config['port']}/{config['database']}"
    )

    engine = create_engine(connection_string)

    df.to_sql(
        "employees",
        engine,
        if_exists="append",
        index=False
    )

    print(f"Loaded {len(df)} records into employees table")