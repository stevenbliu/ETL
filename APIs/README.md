### API Interaction
  - [] Implement graceful error handling. Ex. PlaidApiException catches any specific errors from the Plaid API, while the generic Exception catches other unexpected errors.
  - [] Manage pagination for requests with large number of transactions by using count and offset. The count is set to the maximum number of transactions per request (250 in this case), and offset helps you retrieve subsequent pages of transactions if needed.
  - [] Response Handling. In the original code, you're accessing the transactions directly from the response object as response['transactions']. However, depending on the SDK version and response structure, this may need to be adjusted.
  - [x] Ensure that your ETL process is designed to handle rate-limiting and retries.
---