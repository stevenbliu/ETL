#!/usr/bin/env python
# coding: utf-8

# In[17]:


from pyspark.sql import SparkSession
#.master("spark://spark-master:7077") \

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Spark with PostgreSQL") \
    .master("local[*]") \
    .config("spark.jars", "file:/opt/spark/jars/postgresql-42.7.4.jar") \
    .getOrCreate()

# JDBC connection properties
jdbc_url = "jdbc:postgresql://psql-postgres-1:5432/mydatabase"
connection_properties = {
    "user": "myuser",
    "password": "mysecretpassword",
    "driver": "org.postgresql.Driver"
}

# Load a table into Spark
df = spark.read.jdbc(url=jdbc_url, table="transactions", properties=connection_properties)
df.show(1)


# # In[16]:


# import os

# # Specify the path you want to check
# path = "/opt/spark/jars/postgresql-42.7.4.jar"

# # Check if the path exists
# if os.path.exists(path):
#     print("Path exists!")
# else:
#     print("Path does not exist.")


# # In[15]:


# import psycopg2
# conn = psycopg2.connect(
#     host="psql-postgres-1",
#     port=5432,
#     user="myuser",
#     password="mysecretpassword",
#     dbname="mydatabase"
# )
# print("Connection successful!")

# cur = conn.cursor()

# cur.execute("""
#     SELECT * FROM transactions;
# """)

# rows = cur.fetchall()

# # Print each row
# for i, row in enumerate(rows):
#     if i == 10:
#         break
#     print(row)
    

# # Commit the changes and close the connection
# conn.commit()
# conn.close()


# # In[8]:


# from pyspark.sql import SparkSession

# spark.catalog.clearCache()

# if 'spark' in globals():
#     spark.stop()
    
# # Initialize Spark session
# spark = SparkSession.builder \
#     .appName("Spark Test") \
#     .master("local[*]") \
#     .getOrCreate()

# # Create a simple DataFrame
# data = [("Alice", 29), ("Bob", 35), ("Cathy", 45)]
# columns = ["Name", "Age"]

# df = spark.createDataFrame(data, columns)

# # Show the DataFrame
# df.show()

# # Perform a simple transformation: filter by age > 30
# df_filtered = df.filter(df["Age"] > 30)

# # Show the filtered DataFrame
# df_filtered.show()

# # Stop the Spark session when done
# spark.stop()


# # In[5]:


# if 'spark' in globals():
#     spark.stop()


# # In[4]:


# spark.version


# # In[6]:


# from pyspark.sql import SparkSession

# spark = SparkSession.builder.master("local[*]").appName("SimpleApp").getOrCreate()

# data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
# columns = ["Name", "Age"]

# df = spark.createDataFrame(data, columns)
# df.show()


# # In[11]:


# # pip install psycopg2-binary


# # In[ ]:




