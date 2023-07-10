import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import os

def combined_embeddings_recommender(read_articles, timestamp, recommended_article_ids, k=3):
    
    current_path = os.getcwd()
    news_path = os.path.join(current_path, '..\\01.Dataset\\Small\\Clean\\Train\\news.pkl')
    news = pd.read_pickle(news_path)

    # create filtered_news based on recommended articles from collaborative based filtering
    filtered_news = news.loc[news['News ID'].isin(recommended_article_ids)]

    # Get average vector of user's history news IDs
    average_news_vector = news.loc[news['News ID'].isin(read_articles), 'Average Vector'].mean()

    # Filter news to exlcude articles in user history
    filtered_news = filtered_news.loc[~filtered_news['News ID'].isin(read_articles)]

    # Compute cosine similarity between average_news_vector and each unread news article
    filtered_news['Similarity'] = filtered_news['Average Vector'].apply(lambda x: cosine_similarity([average_news_vector], [x])[0][0])

    # Sort dataframe in descending order
    filtered_news = filtered_news.sort_values(by='Similarity', ascending=False)

    #select top k articles
    top_k_recommended_article_ids = filtered_news.head(k)['News ID'].tolist()

    return top_k_recommended_article_ids