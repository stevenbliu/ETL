ETL Practice Repository 
- General Practice with ETL tools in an attempt to replicate real-world projects.

**Orechestration/Automation**
1. Airflow (Workflow Orchestrator - scheduling and monitoring execution of tasks)
   - Completed:
     - Set up Airflow with docker-compose yaml. (There exist other set-up methods)
     - Executed DAGs via Airflow UI.
     - Extract weather data via API.
     - 
   - TODO:
     - Include weather API fetcher in DAGs to execute.
     - Set up scheduling/triggers for tasks.
     - Requires more ingestion, transformation


Data Source - Process data from diverse formats, and combining them
1. API
    - Completed:
      - Extract weather data via API
3. Streaming Data - Kafka (PubSub service for data transfer)
  - Completed:
     - Set up Kafka with docker-compose yaml.
     - Tested sending synthetic transaction data with Producer and retrieval with Consumer 
 - TODO:
     - Implement Kafka Streams, or Flink for real-time processing
4. Batch Data - RedShift
5. File-Based - CSV, JSON
Example: Combining real-time streaming data (Kafka) with batch data (Redshift) and delivering to dashboards and ML models.

Data Transformation - Complex transformation operations
1. Joins
2. Aggregrations
3. Window Functions
4. Feature Engineering
Example: Enriching customer data with geolocation information and calculating churn probability.

Scalability - Design to handle massive datasets with distributed processing frameworks
1. Spark
2. Flink
Example: Scales horizontally to manage increased workloads.

Real-time Proccesing
1. Kafka Streams
Example: A pipeline for fraud detection using real-time transaction data.

Error Handling + Monitoring
1. Prometheus
2. Grafana
Example: Automatically retries failed steps and sends alerts on pipeline failures.

Data Storage
1. PostgreSQL
2. Snowflake


