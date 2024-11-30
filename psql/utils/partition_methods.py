from datetime import datetime, timedelta

def create_partitioned_table(cursor):
    """Creates the parent partitioned table."""
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions_partitioned (
        transaction_id BIGINT NOT NULL,
        user_id INTEGER NOT NULL,
        amount NUMERIC(10, 2) NOT NULL,
        type VARCHAR(50) NOT NULL,
        timestamp TIMESTAMP NOT NULL,
        PRIMARY KEY (transaction_id, timestamp)  -- Include timestamp in the primary key
    ) PARTITION BY RANGE (timestamp);
    """)
    print("Created parent partitioned table.")


def create_monthly_partitions(cursor, start_date, end_date):
    """Creates monthly partitions within the given date range."""
    current_date = start_date
    while current_date < end_date:
        partition_name = f"transactions_{current_date.strftime('%Y_%m')}"
        next_month = current_date + timedelta(days=31)
        next_month = next_month.replace(day=1)

        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {partition_name}
        PARTITION OF transactions_partitioned
        FOR VALUES FROM ('{current_date.strftime('%Y-%m-%d')}') TO ('{next_month.strftime('%Y-%m-%d')}');
        """)
        print(f"Created partition: {partition_name}")
        current_date = next_month

def migrate_data(cursor):
    """Migrates data from the original table to the partitioned table."""
    cursor.execute("""
    INSERT INTO transactions_partitioned (transaction_id, user_id, amount, type, timestamp)
    SELECT transaction_id, user_id, amount, type, timestamp
    FROM transactions;
    """)
    print("Migrated data from original table to partitioned table.")
