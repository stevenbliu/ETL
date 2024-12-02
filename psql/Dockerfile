FROM postgres:13

# Install required dependencies and pg_cron
RUN apt-get update && apt-get install -y \
    postgresql-13-cron \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update
RUN apt-get install nano


# Enable pg_cron in PostgreSQL config
RUN echo "shared_preload_libraries = 'pg_cron'" >> /usr/share/postgresql/postgresql.conf.sample
