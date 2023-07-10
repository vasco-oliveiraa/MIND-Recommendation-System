import pandas as pd
import os
from sklearn.metrics.pairwise import cosine_similarity

def fetch_similar_users(read_articles, timestamp, k=5):
    
    current_path = os.getcwd()
    
    news_path = os.path.join(current_path, '..\\01.Dataset\\Small\\Clean\\Train\\news.pkl')
    behaviors_path = os.path.join(current_path, '..\\01.Dataset\\Small\\Clean\\Train\\behaviors.pkl')
    
    news = pd.read_pickle(news_path)
    behaviors = pd.read_pickle(behaviors_path)

    # Get average vector of user's history news IDs
    average_user_vector = news.loc[news['News ID'].isin(read_articles), 'Average Vector'].mean()

    # Create a copy of behaviours_df
    user_similarity_df = behaviors.copy()

    # Removes users without history & impressions
    user_similarity_df = user_similarity_df.dropna()

    # Drop duplicate users
    user_similarity_df = user_similarity_df.drop_duplicates(subset=['User ID', 'History & Impressions'])

    # Compute cosine similarity between average_news_vector and each unread news article
    user_similarity_df['Similarity'] = user_similarity_df['Average Vector'].apply(lambda x: cosine_similarity([average_user_vector], [x])[0][0])

    # Sort dataframe in descending order
    user_similarity_df = user_similarity_df.sort_values(by='Similarity', ascending=False).head(k)

    # Get similar users
    similar_users_timestamps = [(row['User ID'], row['Timestamp']) for _, row in user_similarity_df.iterrows()]

    return similar_users_timestamps