from pyspark.sql import  SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder.appName("StructuredStreamingKafka").getOrCreate()

spark.sql("set spark.sql.streaming.schemaInference=true")

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "json-data-topic") \
    .option("startingOffsets", "earliest") \
    .load()

df.printSchema()

personStringDF = df.selectExpr("CAST(value AS STRING)")

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("firstname", StringType(), True),
    StructField("middlename", StringType(), True),
    StructField("lastname", StringType(), True),
    StructField("dob_year", IntegerType(), True),
    StructField("dob_month", IntegerType(), True),
    StructField("gender", StringType(), True),
    StructField("salary", IntegerType(), True),
    ])

personDF = personStringDF.select(from_json(col("value"), schema).alias("data"))

personDF = personDF.select("data.*")

personDF.writeStream \
      .format("console") \
      .outputMode("append") \
      .start() \
      .awaitTermination()
'''
If you want your spark streaming write in kafka topic.
Please comment the codes from line 36 to line 40 and
uncomment all the code lines below
Note: Or you want to your spark streaming write in the console,
you should do it the opposite way
'''    
# personDF.selectExpr("CAST(id AS STRING) AS key", "to_json(struct(*)) AS value") \
#    .writeStream \
#    .format("kafka") \
#    .outputMode("append") \
#    .option("kafka.bootstrap.servers", "localhost:9092") \
#    .option("checkpointLocation", "change-to-your-checkpoint-path") \
#    .option("topic", "read-json-data-topic") \
#    .start() \
#    .awaitTermination()