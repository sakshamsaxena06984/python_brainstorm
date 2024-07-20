import yaml
from pyspark.sql.types import *
from pyspark.sql.functions import *
from ..pipline.craete_spark_object import *


def read_csv_source(spark):
    try:
        with open('../config/properties.yaml', 'r') as f:
            properties = yaml.safe_load(f)
            file_path = properties['CsvSource']['filepath']
            header = properties['CsvSource']['header']
            inferSchema = properties['CsvSource']['inferSchema']
            delimiter = properties['CsvSource']['delimiter']

            if not file_path:
                raise ValueError("csv file_path not provided in yaml file")

            df = spark.read.format('csv').option('header',header).option('inferSchema',inferSchema).load(file_path)

            return df
    except Exception as e:
        print(f"An error occurred while processing raed_csv_sources : {str(e)}")


def read_data_from_sqlserver(spark, tableName):
    try:
        with open('../config/properties.yaml', 'r') as f:
            properties = yaml.safe_load(f)
            dbname = properties['SqlServer']['dbname']
            tables = properties['SqlServer']['tables']
            hostname = properties['SqlServer']['hostname']
            portnumber = properties['SqlServer']['port number']
            username = properties['SqlServer']['username']
            pwd = properties['SqlServer']['password']

            defined_tables = properties.get('SqlServer').get('tables')
            print(defined_tables)

            if tableName not in defined_tables:
                raise ValueError(f"table : {tableName} not defined in the yaml file")


            print("defining connection to the databases")
            url = f"jdbc:mysql://{hostname}:{portnumber}/{dbname}"
            properties = {
                "user": username,
                "password": pwd,
                "driver": "com.mysql.cj.jdbc.Driver"
                # "driver": "com.mysql.jdbc.Driver"
            }
            df = spark.read.jdbc(url=url, table=tableName, properties=properties)

            return df

    except Exception as e:
        print(f"An error occurred while processing read_data_from_sql_server : {str(e)}")


def read_data_from_source(spark, src_type, table=None):
    if src_type == 'SqlServer':
        return read_data_from_sqlserver(spark, tableName=table)
    elif src_type == 'csv':
        return read_csv_source(spark)
    else:
        raise ValueError("Invalid src_type _ supported src-types values are csv and sqlServer")

