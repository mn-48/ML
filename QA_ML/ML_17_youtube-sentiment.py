import pandas as pd
def get_youtube_sentiment(video_stats_df):
    # print(video_stats_df.info())
    video_stats_df['sentiment'] = (video_stats_df['likes'] / (video_stats_df['likes'] + video_stats_df['dislikes']))
    mean_sentiment_df = video_stats_df.groupby('category_id').mean()
    mean_sentiment_df = mean_sentiment_df.sort_values("sentiment", ascending=False)
    mean_sentiment_df['mean_sentiment'] = mean_sentiment_df['sentiment']
    mean_sentiment_df = mean_sentiment_df.filter(['mean_sentiment'])
    return mean_sentiment_df
