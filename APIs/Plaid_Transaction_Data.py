import plaid
from plaid import ApiClient
from plaid.api import plaid_api
from plaid.model import *

# Initialize Plaid client
client = ApiClient(client_id='your_client_id', secret='your_secret', environment='sandbox')

# Create API instance
plaid_api = plaid_api.PlaidApi(client)

# Define start and end date for the transaction fetch
start_date = '2024-01-01'
end_date = '2024-01-31'

# Define the access token (this will be obtained through the Plaid Link flow)
access_token = 'access_token_here'

# Prepare the request for fetching transactions
request = TransactionsGetRequest(
    access_token=access_token,
    start_date=start_date,
    end_date=end_date,
    count=250,  # Optional: Set the number of transactions per request (up to 250)
    offset=0     # Optional: For pagination, to fetch further transactions if there are more than 250
)

try:
    # Fetch transaction data from Plaid
    response = plaid_api.transactions_get(request)
    
    # Extract transaction data
    transactions = response['transactions']
    
    if not transactions:
        print("No transactions found for the given date range.")
    else:
        # Print the transactions (or store them in a database, file, etc.)
        for transaction in transactions:
            print(f"Transaction ID: {transaction.transaction_id}, Date: {transaction.date}, Amount: {transaction.amount}, Name: {transaction.name}")

except plaid.exceptions.PlaidApiException as e:
    print(f"Error fetching transactions: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
