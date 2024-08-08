import pandas as pd
import pandasql as ps
import numpy as np
from datetime import datetime, timedelta
from pyspark.sql import SparkSession


# Gerar dados de log fictícios
np.random.seed(42)

# Configurar parâmetros
num_logs = 10000
start_date = datetime(2023, 1, 1)

# Gerar datas
dates = [start_date + timedelta(minutes=30 * i) for i in range(num_logs)]

# Gerar níveis de log
log_levels = ['INFO', 'WARNING', 'ERROR']
log_level_probs = [0.7, 0.2, 0.1]
log_levels = np.random.choice(log_levels, num_logs, p=log_level_probs)

# Gerar mensagens de log
messages = ['User login', 'File uploaded', 'Error processing request', 'User logout']
messages = np.random.choice(messages, num_logs)

# Criar DataFrame
logs_df = pd.DataFrame({
    'timestamp': dates,
    'log_level': log_levels,
    'message': messages
})

# logs_df.head() #'Usado para visualizar as primeiras linhas de um data frame'

# # Salvar em arquivo Parquet
# logs_df.to_parquet(path="C:\\PROJECTS\\teste_analytics\\server_logs.parquet", engine='fastparquet', compression='gzip')

# # Carregar o arquivo Parquet em um DataFrame
# leitura_arquivo = pd.read_parquet("C:\\PROJECTS\\teste_analytics\\server_logs.parquet", engine='fastparquet')


spark = SparkSession.builder.appName("ExemplParquet").getOrCreate()

logs_spark_df = spark.createDataFrame(logs_df)


# PYSPARK Exibição do DataFrame PySpark
logs_spark_df.show()

# PYSPARK Salvando o DataFrame em um arquivo Parquet
logs_spark_df.write.parquet('C:\\PROJECTS\\teste_analytics\\server_logs.parquet')

# PYSPARK Leitura do arquivo Parquet
leitura_arquivo = spark.read.parquet('C:\\PROJECTS\\teste_analytics\\server_logs.parquet')








# Definir consultas SQL
query_1 = """
SELECT timestamp, log_level, message
FROM leitura_arquivo
WHERE log_level = 'ERROR'
LIMIT 10;
"""

query_2 = """
SELECT log_level, COUNT(*) as count
FROM leitura_arquivo
GROUP BY log_level;
"""

query_3 = """
SELECT DATE(timestamp) as date, COUNT(*) as error_count
FROM leitura_arquivo
WHERE log_level = 'ERROR'
GROUP BY date
ORDER BY date;
"""

# Executar consultas usando pandasql
result_1 = ps.sqldf(query_1, locals())
result_2 = ps.sqldf(query_2, locals())
result_3 = ps.sqldf(query_3, locals())

# Exibir os resultados
print("Resultado da Consulta 1:")
print(result_1)

print("\nResultado da Consulta 2:")
print(result_2)

print("\nResultado da Consulta 3:")
print(result_3)
