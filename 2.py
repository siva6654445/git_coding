df1 = df.select("salaty").count()
df1.display()
from pyspark.sql.functions import *
from pyspark.sql.types import *