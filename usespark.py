from pyspark.sql import SparkSession
from pyspark.ml.regression import GBTRegressor

spark = SparkSession.builder.appName('learn_regression').master('local[1]').getOrCreate()
df_train = spark.read.csv(r"C:\Users\28634\Desktop\train.csv", header=True, inferSchema=True, encoding='utf8')
df_test = spark.read.csv(r"C:\Users\28634\Desktop\test.csv", header=True, inferSchema=True, encoding='utf8')
gbt = GBTRegressor(maxIter=10, labelCol='Closing price', maxDepth=3)
gbt_model = gbt.fit(df_train)
result = gbt_model.transform(df_test)
result.show()