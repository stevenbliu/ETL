-- init_pg_cron.sql

-- Enable the pg_cron extension
CREATE EXTENSION IF NOT EXISTS pg_cron;

-- Optionally, configure cron job settings
ALTER SYSTEM SET cron.database_name = 'mydatabase';  -- Replace with your database name if necessary
