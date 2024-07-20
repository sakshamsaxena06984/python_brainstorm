from tut_pyspark.DataValidationYaml.Python.pipline.craete_spark_object import create_spark
from tut_pyspark.DataValidationYaml.Python.pipline.ingest import *


def main_run():
    try:
        spark_obj = create_spark()
        output = spark_obj.sql("select current_date()")
        print(str(output.collect()[0]))
        ingest_files = read_csv_source(spark=spark_obj)
        # print(ingest_files.show())

        # ingest_tables = read_data_from_sqlserver(spark=spark_obj, tableName='city_df')
        df_csv=read_data_from_source(spark=spark_obj, src_type='csv')
        # print("table records .......")
        # print(ingest_tables.show())
        df_csv.show()

        df_sql = read_data_from_source(spark=spark_obj, src_type='SqlServer', table='city_df')
        print("--------------------")
        df_sql.show()




    except Exception as e:
        print(f"An error occurred in main_run {str(e)}")


main_run()
