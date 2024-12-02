# PostgreSQL CLI Guide

This guide will help you set up a PostgreSQL database, connect to it, and create a table using the PostgreSQL command-line interface (CLI).

---

## Steps

### 1. Open the `psql` CLI

1. Open a terminal on your system.
2. Run the following command to connect to the PostgreSQL CLI:
   ```bash
   psql -U postgres
Replace postgres with your PostgreSQL superuser name (default is postgres).
3. When prompted, enter your PostgreSQL password. 4. After successfully connecting, you will see a prompt like:
    postgres=#
2. Create a Database
Use the CREATE DATABASE command to create a new database:
    CREATE DATABASE my_database;
Replace my_database with your desired database name.
Verify that the database was created by listing all databases:
    \l
3. Connect to the Database
Switch to the newly created database using the \c command:
    \c my_database
You should see a confirmation message like this:
    You are now connected to database "my_database" as user "postgres".
4. Create a Table in the Database
Create a table named transactions with the following fields:

transaction_id: A unique identifier for each transaction.
user_id: The ID of the user performing the transaction.
amount: The monetary value of the transaction.
type: The type of transaction (purchase, refund, transfer).
timestamp: The time of the transaction.
Run this command:
    CREATE TABLE transactions (
        transaction_id SERIAL PRIMARY KEY,
        user_id INT NOT NULL,
        amount NUMERIC(10, 2) NOT NULL,
        type VARCHAR(50) NOT NULL,
        timestamp TIMESTAMP NOT NULL
    );
Verify that the table was created by listing all tables:
    \dt
You should see transactions in the list.

View the schema of the transactions table:
    \d transactions
This will display details about the table's structure.

To check if a table is populated in PostgreSQL using the CLI, you can use the following command:
    SELECT * FROM table_name;

### PSQL Tasks
- [x] Set up + connect PSQL **Containerized** 
    - [x] Test updating records
- [x] Set up + connect PSQL **Local**
    - [x] Test updating records


## CLI COMMANDS:
