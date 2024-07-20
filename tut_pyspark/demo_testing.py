from pyspark.sql import SparkSession
import findspark

findspark.init()

spark = SparkSession.builder.master('local').appName("testing").getOrCreate()
spark_version = spark.version
print(f"Spark Version: {spark_version}")
config = spark.sparkContext.getConf().getAll()
for conf in config:
    print(conf)

data = [
    (1, 2, 3, 4),
    (11, 21, 31, 41),
    (12, 22, 32, 42)
]

df = spark.createDataFrame(data=data, schema=['c1', 'c2', 'c3', 'c4'])
df.printSchema()
df.show()

print("printing the summary ......")
print(type(df.summary()))
print(df.summary())
