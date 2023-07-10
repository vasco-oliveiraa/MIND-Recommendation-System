import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import os

def pure_content_embeddings_recommender(read_articles, timestamp, articles_k=3):
    
    current_path = os.getcwd()
    news_path = os.path.join(current_path, '..\\01.Dataset\\Small\\Clean\\Train\\news.pkl')
    news = pd.read_pickle(news_path)

    # Get average vector of user's history news IDs
    average_news_vector = news.loc[news['News ID'].isin(read_articles), 'Average Vector'].mean()

    # Filter news to exlcude articles in user history
    filtered_news = news.loc[~news['News ID'].isin(read_articles)]

    # Convert input timestamp to date time
    timestamp = pd.to_datetime(timestamp)

    # # Filter news to exlcude any articles released after date of interaction
    filtered_news = filtered_news[filtered_news['Release Date'] <= timestamp]

    # Compute cosine similarity between average_news_vector and each unread news article
    filtered_news['Similarity'] = filtered_news['Average Vector'].apply(lambda x: cosine_similarity([average_news_vector], [x])[0][0])

    # Sort dataframe in descending order
    filtered_news = filtered_news.sort_values(by='Similarity', ascending=False)

    #select top k articles
    article_ids = filtered_news.head(articles_k)['News ID'].tolist()
    
    return article_ids