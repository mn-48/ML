from  datetime import datetime, timedelta

def get_user_interaction_counts(search_interaction_df):
    latest_date_string = search_interaction_df.agg({"date": "max"}).collect()[0][0]
    latest_date = datetime.strptime(latest_date_string, "%Y-%m-%d")

    user_month_counts = get_df_counts_from_date_by_user_id(search_interaction_df, latest_date, 30)

def get_df_counts_from_date_by_user_id(df, end_date, days_delta):
    start_date = end_date - days_delta
    return df.where(df["date"].between(start_date, end_date)).groupBy("user_id").count()

