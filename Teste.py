############################################ SPARK
# Cria uma SparkSession
spark = SparkSession.builder.appName("ExemplParquet").getOrCreate()

logs_spark_df = spark.createDataFrame(logs_df)


# PYSPARK Exibição do DataFrame PySpark
logs_spark_df.show()

# PYSPARK Salvando o DataFrame em um arquivo Parquet
logs_spark_df.write.parquet('caminho/para/arquivo.parquet')

# PYSPARK Leitura do arquivo Parquet

leitura_arquivo = spark.read.parquet('caminho/para/arquivo.parquet')