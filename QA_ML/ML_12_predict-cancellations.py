from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import VectorAssembler


def predict_cancellations(user_interaction_df):
    assembler = VectorAssembler(
        inputCols=["month_interaction_count", "week_interaction_count", "day_interaction_count"], outputCol="features"
    )
    user_interaction_df.show()
    features_df = assembler.transform(user_interaction_df)
    features_df = features_df.withColumn(
        "label", features_df["cancelled_within_week"])

    lr_model = LogisticRegression(
        maxIter=10, threshold=0.6, elasticNetParam=1, regParam=0.1)

    trained_lr_model = lr_model.fit(features_df)

    predicts_df = trained_lr_model.transform(features_df)
    predicts_df = predicts_df.select(
        ["user_id", "rawPrediction", "probability", "prediction"])

    predicts_df.show()
    return predicts_df
