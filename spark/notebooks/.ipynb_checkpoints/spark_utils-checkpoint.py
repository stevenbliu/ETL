from pyspark.sql import SparkSession

def get_spark_session(app_name="SparkApplication", master="local[*]", config_options=None):
    """
    Creates and returns a SparkSession with specified configurations.
    :param app_name: Name of the Spark application
    :param master: Spark master URL
    :param config_options: Additional configurations as a dictionary
    :return: SparkSession instance
    """
    builder = SparkSession.builder.appName(app_name).master(master)
    
    if config_options:
        for key, value in config_options.items():
            builder = builder.config(key, value)
    
    return builder.getOrCreate()

def get_jdbc_connection_properties(user, password, driver="org.postgresql.Driver"):
    """
    Returns a dictionary of JDBC connection properties.
    :param user: Database username
    :param password: Database password
    :param driver: JDBC driver class
    :return: Dictionary of connection properties
    """
    return {
        "user": user,
        "password": password,
        "driver": driver
    }

def get_psql_data(jdbc_url, table_name, user, password, jdbc_jar_path="/opt/spark/jars/postgresql-42.7.4.jar"):
    """
    Loads data from a PostgreSQL table into a Spark DataFrame.
    :param jdbc_url: JDBC URL for the PostgreSQL database
    :param table_name: Table name to load
    :param user: Database username
    :param password: Database password
    :param jdbc_jar_path: Path to the PostgreSQL JDBC driver jar
    :return: Spark DataFrame
    """
    spark = get_spark_session(
        app_name="Spark with PostgreSQL",
        config_options={"spark.jars": jdbc_jar_path}
    )
    
    connection_properties = get_jdbc_connection_properties(user, password)
    
    df = spark.read.jdbc(url=jdbc_url, table=table_name, properties=connection_properties)
    return df

import utils  # Assuming this contains the verify_path function

def get_csv_data(file_path):
    """
    Loads data from a CSV file into a Spark DataFrame.
    :param file_path: Path to the CSV file
    :return: Spark DataFrame
    """
    spark = get_spark_session(app_name="CSVDataLoader")
    
    # Verify the file path exists
    utils.verify_path(file_path)
    
    # Read the CSV file into a Spark DataFrame
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    return df