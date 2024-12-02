FROM postgres:13

# Install nano
RUN apt-get update && apt-get install -y nano && apt-get clean
RUN apt-get update && apt-get install -y postgresql-13-cron

# Ensure the pg_cron shared library is preloaded
# RUN echo "shared_preload_libraries = 'pg_cron'" >> /var/lib/postgresql/data/postgresql.conf

# RUN echo "CREATE EXTENSION IF NOT EXISTS pg_cron;" > /docker-entrypoint-initdb.d/enable_pgcron.sql

