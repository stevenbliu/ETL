import psycopg2
import random
from datetime import datetime

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="transaction_data",  # Replace with your database name
    user="postgres",  # Replace with your username
    password="sbl214",  # Replace with your password
    host="localhost",  # If running locally
    port="5432"  # Default PostgreSQL port
)
cur = conn.cursor()

# Define transaction types and insert 100 transactions
transaction_types = ['purchase', 'refund', 'transfer']
for i in range(100):
    transaction = {
        'transaction_id': i,
        'user_id': random.randint(1, 100),
        'amount': round(random.uniform(10, 1000), 2),  # Random amount between 10 and 1000
        'type': random.choice(transaction_types),  # Random transaction type
        'timestamp': '2024-11-25T10:00:00Z'  # Timestamp for the transaction
    }
    
    # Insert transaction into the database
    cur.execute("""
        INSERT INTO transactions (transaction_id, user_id, amount, type, timestamp)
        VALUES (%s, %s, %s, %s, %s)
    """, (transaction['transaction_id'], transaction['user_id'], transaction['amount'], transaction['type'], transaction['timestamp']))

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()
