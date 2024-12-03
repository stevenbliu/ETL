import csv
import random
import calendar
from datetime import datetime, timedelta

# Define transaction types
transaction_types = ['purchase', 'refund', 'transfer']

# Base timestamp
base_timestamp = datetime.now()

# File to save the dataset
output_file = 'problematic_transactions.csv'

# Function to introduce problems
def introduce_issues(transaction, issue_type):
    if issue_type == "schema_drift":
        if random.random() < 0.5:
            transaction['user_name'] = f"User_{transaction['user_id']}"  # Add a new field
        else:
            transaction.pop('amount', None)  # Remove a field
    elif issue_type == "missing_data":
        if random.random() < 0.5:
            transaction['user_id'] = None  # Set user_id to None
        else:
            transaction['amount'] = None  # Set amount to None
    elif issue_type == "incorrect_format":
        transaction['amount'] = f"{transaction['amount']} dollars"  # Add invalid format
    elif issue_type == "data_duplication":
        return [transaction, transaction]  # Duplicate transaction
    elif issue_type == "out_of_order_data":
        # Modify timestamp to shuffle chronological order
        offset = random.randint(-100, 100) * 60  # Offset in seconds
        transaction['timestamp'] = (datetime.fromisoformat(transaction['timestamp'][:-1]) +
                                    timedelta(seconds=offset)).strftime('%Y-%m-%dT%H:%M:%SZ')
    elif issue_type == "corrupted_data":
        transaction['timestamp'] = transaction['timestamp'].replace('-', '/', 1)  # Corrupt date
    elif issue_type == "conflicting_records":
        # Add a conflicting record with different values
        return [transaction, {**transaction, 'amount': round(random.uniform(10, 1000), 2)}]
    return [transaction]

# Generate transactions with issues
transactions = []
for i in range(1, 100):
    # Modify the month based on the index i
    new_month = (base_timestamp.month + i - 1) % 12 + 1
    _, last_day_of_month = calendar.monthrange(base_timestamp.year, new_month)
    new_day = min(base_timestamp.day, last_day_of_month)

    # Create a new timestamp
    current_timestamp = base_timestamp.replace(month=new_month, day=new_day) + timedelta(minutes=i)
    transaction_id = int(current_timestamp.timestamp())

    # Create the transaction record
    transaction = {
        'transaction_id': transaction_id,
        'user_id': random.randint(1, 100),
        'amount': round(random.uniform(10, 1000), 2),
        'type': random.choice(transaction_types),
        'timestamp': current_timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')
    }

    # Introduce random issues
    issue_types = ["schema_drift", "missing_data", "incorrect_format",
                   "data_duplication", "out_of_order_data", "corrupted_data", "conflicting_records"]
    issue = random.choice(issue_types)

    problematic_transactions = introduce_issues(transaction, issue)
    transactions.extend(problematic_transactions)

# Write to a CSV file
fieldnames = ['transaction_id', 'user_id', 'amount', 'type', 'timestamp']
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(transactions)

print(f"Problematic dataset generated and saved to {output_file}")
