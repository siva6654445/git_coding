from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("My First PySpark App") \
    .getOrCreate()

data = [
    ("Siva", 25, 5000),
    ("Ravi", 30, 6000),
    ("Kumar", 35, None)
]

columns = ["Name", "Age", "Salary"]

df = spark.createDataFrame(data, columns)

# Count example
df1 = df.select("Salary").count()

print("Count:", df1)

# Show DataFrame
df.show()

spark.stop()
from pyspark.sql.functions import *
from pyspark.sql.types import *