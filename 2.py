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
df1 = df.withColumn("Salary",col("salary"*96))
--df1.display()
data = [1,3,4,5,6,7,9]

for i in data:
    if i > 9:
        print(i)
    else:
        "mone"
