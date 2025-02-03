from pyspark.sql import SparkSession, Row
from pyspark.ml.linalg import Vectors
from pyspark.ml.classification import LogisticRegression, LogisticRegressionModel

# Initialize Spark Session
spark = SparkSession.builder.appName("LogisticRegressionExample").getOrCreate()

# Create DataFrame using spark.createDataFrame()
bdf = spark.createDataFrame([
    Row(label=1.0, weight=1.0, features=Vectors.dense([0.0, 5.0])),
    Row(label=0.0, weight=2.0, features=Vectors.dense([1.0, 2.0])),
    Row(label=1.0, weight=3.0, features=Vectors.dense([2.0, 1.0])),
    Row(label=0.0, weight=4.0, features=Vectors.dense([3.0, 3.0]))
])

# Initialize Logistic Regression Model
blor = LogisticRegression(weightCol="weight")

# Get and Set Parameters
print("Regularization Parameter (before):", blor.getRegParam())
blor.setRegParam(0.01)
print("Regularization Parameter (after):", blor.getRegParam())

blor.setMaxIter(10)
print("Max Iterations:", blor.getMaxIter())

# Clear maxIter Parameter
blor.clear(blor.maxIter)

# Fit Model
blorModel = blor.fit(bdf)

# Set Model Parameters
blorModel.setFeaturesCol("features")
blorModel.setProbabilityCol("newProbability")

print("Probability Column:", blorModel.getProbabilityCol())
print("Max Block Size:", blorModel.getMaxBlockSizeInMB())

blorModel.setThreshold(0.1)
print("Threshold:", blorModel.getThreshold())

print("Coefficients:", blorModel.coefficients)
print("Intercept:", blorModel.intercept)

# Evaluate Model
accuracy_check = blorModel.evaluate(bdf).accuracy == blorModel.summary.accuracy
print("Model Accuracy Check:", accuracy_check)

# Load Multiclass Classification Data
data_path = "data/mllib/sample_multiclass_classification_data.txt"
mdf = spark.read.format("libsvm").load(data_path)

# Multinomial Logistic Regression
mlor = LogisticRegression(regParam=0.1, elasticNetParam=1.0, family="multinomial")
mlorModel = mlor.fit(mdf)

print("Coefficient Matrix:", mlorModel.coefficientMatrix)
print("Intercept Vector:", mlorModel.interceptVector)

# Create Test Data
test0 = spark.createDataFrame([Row(features=Vectors.dense([-1.0, 1.0]))])

print("Prediction:", blorModel.predict(test0.head().features))
print("Raw Prediction:", blorModel.predictRaw(test0.head().features))
print("Probability:", blorModel.predictProbability(test0.head().features))

# Transform and Inspect Result
result = blorModel.transform(test0).head()
print("Prediction:", result.prediction)
print("New Probability:", result.newProbability)
print("Raw Prediction:", result.rawPrediction)

# Sparse Test Data
test1 = spark.createDataFrame([Row(features=Vectors.sparse(2, [0], [1.0]))])
print("Sparse Prediction:", blorModel.transform(test1).head().prediction)

# Fixing setParams Error
try:
    blor.setParams("vector")
except TypeError as e:
    print("Error:", e)  # Fix: setParams requires keyword arguments

# Save and Load Model
temp_path = "/tmp"  # Set a valid path
lr_path = temp_path + "/lr"
blor.save(lr_path)
lr2 = LogisticRegression.load(lr_path)
print("Loaded Model Regularization Parameter:", lr2.getRegParam())

model_path = temp_path + "/lr_model"
blorModel.save(model_path)
model2 = LogisticRegressionModel.load(model_path)

print("Coefficient Comparison:", blorModel.coefficients[0] == model2.coefficients[0])
print("Intercept Comparison:", blorModel.intercept == model2.intercept)

print("Model 2:", model2)
print("Transform Equality Check:", blorModel.transform(test0).take(1) == model2.transform(test0).take(1))
