# Data Engineering Project 

This checklist represents a comprehensive approach to building a senior-level data engineering project, with tasks divided into specific, manageable phases. 
- **Comprehensive Coverage**: It includes foundational tasks, real-time processing, scaling, error handling, and automation.
- **Progressive Complexity**: Tasks are ordered from simple setup to advanced integrations, ensuring a logical flow.
- **Real-World Focus**: The project mimics what senior-level data engineers work on in production systems (orchestration, streaming, scalability).
---

## Phase 1: Setup and Foundational Components

### 1. Orchestration with Apache Airflow
- [x] Set up **Apache Airflow** with `docker-compose` and verify the environment is running.
- [x] Run example **DAGs** to ensure the environment is working correctly.
- [x] Integrate a basic script to fetch weather data from an external **API** (OpenWeaher).
- [x] Include **Airflow's scheduling system** to automate events.
- [x] Set up logging of DAGS. Viewable in UI.
- [ ] Set up DAGs on Trigger.

### 2. Data Ingestion Basics
- [x] **Ingest data** from an external **API** 
- [x] Set up **Kafka** using `docker-compose` to manage data streams.
- [x] Create and test **Kafka Producer** to send synthetic data.
- [x] Create and test **Kafka Consumer** to receive synthetic data.


### 3. Data Storage
- [x] Set up a SQL or **Snowflake** database to store ingested synthetic and API data.
  - [x] Set up + connect with PostgreSQL in Local 
  - [x] Set up + connect with PostgreSQL in Docker Container
- [x] Write a pipeline to ingest weather data into **PostgreSQL/Snowflake** 
  - [x] Ensure successful data storage.
- [~] Optimize database schema and tables for time-series or batch data (weather data, in this case).
- [x] Set up a NoSQL database
  - [x] Set up + connect with MongoDB in Docker
  ## Database Selection
  - #### Batch: PostgreSQL, MySQL, SQL Server
    - When to use: 
      - Require complex SQL queries, joins, relational data integrity
      - Well-defined schema and ACID transactions
        - Atomicity:  Ensures that all operations within a transaction are treated as a single unit. This means that either all operations succeed or none of them are applied.

        - Consistency: Ensures that a transaction brings the database from one valid state to another. It enforces rules such as constraints (e.g., primary keys, foreign keys, and check constraints) so that the data remains correct and valid according to the database schema.

        - Isolation:  Ensures that transactions are executed in such a way that they do not interfere with each other. Even if multiple transactions are occurring simultaneously, they should not affect each other's results.

        - Durability: Guarantees that once a transaction has been committed, it will remain so, even in the event of a power failure, crash, or other types of system failure.

      - Enforce foreign key constraints, data integrity, and support for complex relational models
    - Can be optimized by:
      - [x] Partitioning based on time-intervals (daily, monthly, yearly)
      - [x] Create indexes frequently queried fields (IDs, etc.)
        - [x] Created index for transaction_types
        - [x] Verified index is created
      - [x] Retention Policy. Delete or archive old data to prevent table from growing too large
        - [x] Automatically install pg_cron to PostgreSQL
        - [x] Schedule simple tasks to query data, analyze data, or remove with cron based on a fixed-interval. (Airflow is more overhead)
        - [x] Implement a retention policy with cron to delete/archive data every 30 days
      - [ ] Compression (pg_compress in PostgreSQL) to reduce size of historical data
  - 
  - ##### MongoDB, NoSQL, Redis, Cassandra
    - When to use:
      - Require schema flexibility or expect frequent changes to data structure
      - Working with large-scale applications that require high throughput and horizontal scalability.
      - Data has a document-based structure with nested data (e.g., JSON-like documents).
      - Need a NoSQL solution for key-value stores or document-based storage.
      - You need faster performance for simple read/write operations.
  - ##### Others:
    - Time-Series: Use TimescaleDB, InfluxDB
      - Specialized time-series databases

---
---

## Phase 2: Batch and Real-Time Data Integration

### 4. Batch Processing with Apache Spark
- [x] Install **Apache Spark** on your local environment or cloud.
  - [x] Set up dockerized Spark 
  - [x] Set up driver/master  + workers
  - [x] Tested connection and data retrieval from PSQL datbase on Jupyter with PySpark
- [ ] Write a **Spark batch job** to process data 
  - [] Data from PostgreSQL/Snowflake.
  - [] Data from file-base
- [ ] Perform aggregations, joins, and other batch transformations on the data.
- [ ] Store the processed data back into the database for downstream analysis.

### 5. Real-Time Processing with Kafka Streams
- [ ] Set up **Kafka Streams** for processing real-time data (transaction data, etc.).
- [ ] Build a **Kafka Streams topology** for real-time processing of incoming data.
- [ ] Integrate **stream-to-batch data pipeline** to feed Kafka data into the PostgreSQL/Snowflake database.
- [ ] Handle time-based operations (e.g., windowing) in your Kafka Streams pipeline.

---

## Phase 3: Data Transformation and Advanced Processing

### 6. Data Transformation

- [ ] Perform **data transformations** using batch processing tools (Spark).
  - Example: Join weather data with external datasets like geolocation information.
  - Example: Create features such as churn probability or customer profiling.
- [ ] Write **complex SQL queries** involving joins, window functions, and aggregations for real-time and batch data.
- [ ] Ensure **data quality** through transformations, handling null values, and ensuring data consistency.

### 7. Real-Time Fraud Detection Pipeline
- [ ] Set up **Flink** or **Kafka Streams** for fraud detection with real-time transaction data.
- [ ] Implement **stateful stream processing** in Kafka Streams or Flink (e.g., sessionization).
- [ ] Integrate **machine learning models** for real-time prediction (e.g., detecting fraudulent transactions).
- [ ] Implement a **real-time alerting system** when fraud is detected.

---

## Phase 4: Monitoring, Scalability, and Error Handling

### 8. Monitoring and Alerting
- [ ] Set up **Prometheus** to monitor the health and performance of your data pipeline.
- [ ] Integrate **Grafana** with Prometheus for visualizing pipeline metrics (e.g., processing time, throughput).
- [ ] Set up **alerting** for failed tasks, delays, and performance degradation in the pipeline.
- [ ] Monitor **Kafka consumer lag** and **Spark job performance**.

### 9. Error Handling
- [ ] Implement **error handling** in your DAGs to catch task failures.
- [ ] Implement **automatic retries** for failed tasks in both Airflow and Kafka.
- [ ] Set up **alerting** for failed pipeline steps, especially in real-time data processing.

### 10. Scaling the System
- [ ] Benchmark **Spark** performance on large datasets (e.g., scaling to 1TB of weather data).
- [ ] Optimize **Kafka producer and consumer** performance by adjusting partitioning and replication factors.
- [ ] Test **horizontal scaling** for Apache Spark jobs to distribute workload.
- [ ] Load test the system and identify bottlenecks.

### API Interaction
  - [] Implement graceful error handling. Ex. PlaidApiException catches any specific errors from the Plaid API, while the generic Exception catches other unexpected errors.
  - [] Manage pagination for requests with large number of transactions by using count and offset. The count is set to the maximum number of transactions per request (250 in this case), and offset helps you retrieve subsequent pages of transactions if needed.
  - [] Response Handling. In the original code, you're accessing the transactions directly from the response object as response['transactions']. However, depending on the SDK version and response structure, this may need to be adjusted.
  - [x] Ensure that your ETL process is designed to handle rate-limiting and retries.
---

## Phase 5: Automation and CI/CD

### 11. Automation
- [ ] Automate the **deployment** of the entire pipeline using **GitHub Actions** or another CI/CD tool.
- [ ] Write **Dockerfiles** for each component (Airflow, Kafka, Spark, Flink) and containerize them.
- [ ] Set up **automated tests** for each component of the data pipeline (using PyTest, Unittest, etc.).

### 12. Data Quality
- [ ] Integrate **Great Expectations** or another data quality tool to validate data at each pipeline stage.
- [ ] Write data validation checks for all datasets (schema validation, completeness, correctness).
- [ ] Automate **data quality tests** in the CI/CD pipeline.

---

## Phase 6: Advanced Enhancements

### 13. Machine Learning Integration
- [ ] Create a **feature engineering pipeline** to prepare data for machine learning models.
- [ ] Train and deploy **ML models** for prediction tasks such as churn or fraud detection.
- [ ] Integrate ML models into the streaming pipeline for real-time inference.
- [ ] Write batch jobs to retrain models periodically with new data.

### 14. Cloud Integration
- [ ] Migrate parts of your pipeline to **cloud services** like AWS, GCP, or Azure (e.g., S3 for storage, BigQuery for processing).
- [ ] Set up **cloud storage** for large-scale datasets and model outputs.
- [ ] Integrate **cloud data lakes** for scalable storage and processing.


### 15. Documentation
- [ ] Document the **architecture** of your pipeline (diagramming tools like Lucidchart or draw.io).
- [ ] Create detailed **README files** for each project component (Airflow DAGs, Kafka topics, Spark jobs, etc.).
- [ ] Write **technical documentation** for the pipeline, including setup instructions and dependencies.

---

## Phase 7: Final Testing and Deployment

### 16. Integration Testing
- [ ] Perform **end-to-end testing** of the entire pipeline to ensure all components work together.
- [ ] Validate data flow from ingestion to processing, transformation, and storage.
- [ ] Test **edge cases** (e.g., missing data, API failures, etc.).

### 17. Performance Tuning
- [ ] Fine-tune **Kafka settings** for higher throughput and lower latency.
- [ ] Optimize **Spark jobs** for faster processing with large datasets.
- [ ] Perform **load testing** to evaluate the system's performance under heavy usage.

### 18. Final Deployment
- [ ] Deploy the project to **production** (on-premises or cloud).
- [ ] Ensure that all components are configured for **production use**, including scalability, monitoring, and alerting.
- [ ] Set up a **maintenance plan** for periodic updates and model retraining.

---

## Additional Enhancements

### 19. Real-time Dashboard
- [ ] Build a **real-time dashboard** using tools like **Tableau** or **PowerBI** to visualize incoming data and ML model predictions.
- [ ] Ensure that the dashboard pulls data from the real-time Kafka streams or batch jobs.

---


