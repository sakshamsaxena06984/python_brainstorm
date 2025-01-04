# li=[1,2,2,3,3,1,4]
# d={}
# li.append()
# for ele in li:
#     print(ele)
#     d[ele]=d.get(ele,0)+1
#
# print(li)
# print(d)
# for k,v in d.items():
#     print(f"key is {k} and value is {v}")

"""
1
4
6 9 8 5
5
9 2 4 1 8


"""
import sys

def intersections(arr1, n, arr2, m) :
    #Your code goes here
    d={}
    for ele in arr1:
        d[ele]=d.get(ele,0)+1

    for ele in arr2:
        d[ele]=d.get(ele,0)+1

    ans=[]
    for k,v in d.items():
        if v==2:
            ans.append(k)
    return ans

from pyspark.sql import SparkSession
spark = (
    SparkSession
    .builder
    .master("local[*]")
    .appName("processing json file with streaming")
    .config("spark.streaming.stopGracefullyonshutdown",True)
    .getOrCreate()
)
# allow automatic schemaInference while reading
spark.conf.set("spark.sql.streaming.schemaInference",True)
streaming_df= (
    spark
    .readStream
    .option("cleanSource","archive")
    .option("sourceArchiveDir","archive_dir")
    .option("maxFilesPerTrigger",1)
    .format("json")
    .load("inputs/device-file/")
)

streaming_df.printSchema()
from pyspark.sql.functions import explode
df=streaming_df.withColumn("data_devices",explode("data.devices"))
from pyspark.sql.functions import col
flatten_df=(
    df.drop("data")
    .withColumn("deviceId",col("data_devices.deviceId"))
    .withColumn("measure",col("data_devices.measure"))
    .withColumn("status",col("data_devices.status"))
    .withColumn("temperature",col("data_devices.temperature"))


)

flatten_df.printSchema()
flatten_df.drop("data_devices")


spark.conf.set('spark.sql.legacy.pathOptionBehavior.enabled',True)


(
    flatten_df
    .writeStream
    .format('csv')
    .outputMode("append")
    .option("path","output/device.csv")
    .option("checkpointLocation","checkpoint_dir")
    .start()
    .awaitTermination())

if __name__=='__main__':
    # arr1=[6 ,9 ,8, 5]
    # arr2=[9 ,2 ,4 ,1, 8]
    # print(intersections(arr1,4,arr2,5))
    #
    # print(f"max size is {sys.maxsize}")
    # li=[0,1,0,1]
    # li.sort()
    # print(li)
    #
    n=123
    print(n/10)
    print(n//10)


