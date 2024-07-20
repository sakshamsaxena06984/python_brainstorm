import yaml
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *


def create_spark():
    try:
        spark = SparkSession.builder \
            .master('local[*]') \
            .appName('DataValidation') \
            .enableHiveSupport() \
            .config('spark.driver.extraClassPath', '/Users/sakshamsaxena/PycharmProjects/python_tut/tut_pyspark/DataValidationYaml/Python/'
                                                   'resources/mysql-connector-java-8.0.29.jar') \
            .getOrCreate()
        return spark
    except Exception as e:
        print(f" An error occurred in create_spark method : {str(e)}")
