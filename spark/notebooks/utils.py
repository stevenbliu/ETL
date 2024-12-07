import os

def verify_path(path):
    # Specify the path you want to check
    # path = "/opt/spark/jars/postgresql-42.7.4.jar"
    # path = "problematic_transactions.csv"
    # Check if the path exists
    if os.path.exists(path):
        print("Path exists!")
        return True
    else:
        print("Path does not exist.")
        return False



