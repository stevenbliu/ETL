import psycopg2
import random
from datetime import datetime, timedelta
import psql.utils.partition_methods as partition_utils

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="transaction_data",  # Replace with your database name
    user="postgres",  # Replace with your username
    password="sbl214",  # Replace with your password
    host="localhost",  # If running locally
    port="5432"  # Default PostgreSQL port
)
cur = conn.cursor()

def get_min_max_timestamps(cursor):
    cursor.execute("""
    SELECT MIN(timestamp) AS min_timestamp, MAX(timestamp) AS max_timestamp
    FROM transactions;
    """)
    return cursor.fetchone()  # Returns (min_timestamp, max_timestamp)

def create_partitions_for_range(cursor, min_timestamp, max_timestamp):
    current = min_timestamp.replace(day=1)  # Start at the first day of the month
    while current <= max_timestamp:
        next_month = (current + timedelta(days=32)).replace(day=1)  # Move to the next month's first day
        partition_name = f"transactions_{current.year}_{current.month:02d}"
        cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {partition_name}
        PARTITION OF transactions_partitioned
        FOR VALUES FROM ('{current}') TO ('{next_month}');
        """)
        print(f"Created partition: {partition_name}")
        current = next_month


min_timestamp, max_timestamp = get_min_max_timestamps(cur)
create_partitions_for_range(cur, min_timestamp, max_timestamp)


# Define date range for partitions
START_DATE = datetime(2023, 1, 1)  # Adjust to your data's start date
END_DATE = datetime(2025, 1, 1)    # Adjust to your desired end date

# Step 1: Create parent partitioned table
partition_utils.create_partitioned_table(cur)

# Step 2: Create monthly partitions
partition_utils.create_monthly_partitions(cur, START_DATE, END_DATE)

# Step 3: Migrate data into the partitioned table
partition_utils.migrate_data(cur)

print("Migration completed successfully!")

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()

print ('Synthetic Data successfully inserted to transactions table')
