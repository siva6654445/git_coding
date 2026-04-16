df = spark.read.csv("location")
df.display()
from pyspark.sql.functions import *
from pyspark.sql.types import *
