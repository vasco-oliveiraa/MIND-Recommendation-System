import pandas as pd
from datetime import timedelta
import os
import streamlit as st

def popularity_category_recommender(timestamp, categories, read_articles, k=5):
    
    current_path = os.getcwd()
    
    news_path = os.path.join(current_path, '..\\01.Dataset\\Small\\Clean\\Train\\news.pkl')
    behaviors_path = os.path.join(current_path, '..\\01.Dataset\\Small\\Clean\\Train\\behaviors.pkl')

    news = pd.read_pickle(news_path)
    behaviors = pd.read_pickle(behaviors_path)
    
    timestamp_threshold = pd.to_datetime(timestamp)
    max_old_date = timestamp_threshold - timedelta(weeks=2)

    filtered_behaviors = behaviors.loc[
        (behaviors["Timestamp"] < timestamp_threshold) &
        (behaviors["Timestamp"] > max_old_date)
    ].copy()

    filtered_behaviors.drop("Timestamp", axis=1, inplace=True)

    articles_df = (
        filtered_behaviors["History"].str.split(" ")
        .explode("History")
        .to_frame()
    )
    
    articles_df["ArticleCount"] = 1

    articles_most_read = articles_df["History"].value_counts().to_frame(name="ArticleCount")
    
    articles_most_read["Category"] = articles_most_read.index.map(news.set_index("News ID")["Category"])

    filtered_articles = articles_most_read[articles_most_read["Category"].isin(categories)]
    
    filtered_articles = filtered_articles[~filtered_articles.index.isin(read_articles)]
    
    article_ids = filtered_articles.index[:k].tolist()

    return article_ids