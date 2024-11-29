import psycopg2
import random
from datetime import datetime, timedelta

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="transaction_data",  # Replace with your database name
    user="postgres",  # Replace with your username
    password="sbl214",  # Replace with your password
    host="localhost",  # If running locally
    port="5432"  # Default PostgreSQL port
)
cur = conn.cursor()

# Create the table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id BIGINT PRIMARY KEY,
        user_id INT NOT NULL,
        amount DECIMAL(10, 2) NOT NULL,
        type VARCHAR(50) NOT NULL,
        timestamp TIMESTAMP NOT NULL
    );
""")

# Define transaction types and insert 100 transactions
transaction_types = ['purchase', 'refund', 'transfer']

base_timestamp = datetime.now()

for i in range(1, 100):
    # Modify the month based on the index i (cycle through months)
    new_month = (base_timestamp.month + i - 1) % 12 + 1  # Ensure month stays between 1 and 12
    
    # Create a new timestamp with the modified month (keeping day, hour, minute, etc. unchanged)
    current_timestamp = base_timestamp.replace(month=new_month) + timedelta(minutes=i)
    
    # Generate transaction ID based on the timestamp (you can use any part of the timestamp here)
    transaction_id = int(current_timestamp.timestamp())  # Unix timestamp in seconds
    
    # Format the timestamp
    timestamp_str = current_timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')

    transaction = {
        'transaction_id': transaction_id,
        'user_id': random.randint(1, 100),
        'amount': round(random.uniform(10, 1000), 2),  # Random amount between 10 and 1000
        'type': random.choice(transaction_types),  # Random transaction type
        'timestamp': timestamp_str  # Timestamp for the transaction
    }

    # Insert transaction into the database
    cur.execute("""
        INSERT INTO transactions (transaction_id, user_id, amount, type, timestamp)
        VALUES (%s, %s, %s, %s, %s)
    """, (transaction['transaction_id'], transaction['user_id'], transaction['amount'], transaction['type'], transaction['timestamp']))

    # Create index for transaction types
    cur.execute("""
        CREATE INDEX IF NOT EXISTS idx_transaction_type
        ON transactions(type);
    """)

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()

print ('Synthetic Data successfully inserted to transactions table')
