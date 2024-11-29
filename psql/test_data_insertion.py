import psycopg2

def test_transaction_insert():
    conn = psycopg2.connect(
        host="localhost",
        database="transaction_data",
        user="postgres",
        password="sbl214"
    )
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM transactions;")
    count = cur.fetchone()[0]
    assert count > 0, "No data found in the transactions table"
    cur.close()
    conn.close()
