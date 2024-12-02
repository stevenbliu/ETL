import psycopg2

# Connect to your containzierized PostgreSQL database
conn = psycopg2.connect(
    dbname="mydatabase",  # Replace with your database name
    user="myuser",  # Replace with your username
    password="mysecretpassword",  # Replace with your password
    host="localhost",  
    port="5433"  # Containerized PostgreSQL port set in docker-compose
    # host="psql-postgres-1",  # If running container python script from container db
    # port="5432"  # Default PostgreSQL port for local db
)

cur = conn.cursor()

# archive after 30 days
cur.execute(
'''SELECT cron.schedule(
  '0 0 * * *',  -- Run daily at midnight
  'WITH archived AS (
     INSERT INTO logs_archive (SELECT * FROM logs WHERE created_at < NOW() - INTERVAL ''30 days'')
     RETURNING *
   )
   DELETE FROM logs WHERE created_at < NOW() - INTERVAL ''30 days'';'
);'''
)

cur.execute(
    
# delete after 30 days
'''
SELECT cron.schedule(
  '0 0 * * *',  -- Run daily at midnight
  'DELETE FROM logs WHERE created_at < NOW() - INTERVAL ''30 days'';'
);
'''
)