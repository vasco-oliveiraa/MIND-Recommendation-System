import os
import pandas as pd

def collaborative_recommender(read_articles, timestamp, similar_users_timestamps):
    
    current_path = os.getcwd()
    behaviors_path = os.path.join(current_path, '..\\01.Dataset\\Small\\Clean\\Train\\behaviors.pkl')
    behaviors = pd.read_pickle(behaviors_path)

    # Filter behaviors df for similar users & timestamps
    similar_users_df = behaviors[behaviors[['User ID', 'Timestamp']].apply(tuple, axis=1).isin(similar_users_timestamps)]

    # Initialize list to store relevant article IDs
    recommended_article_ids = []

    # Iterate over the rows of the DataFrame
    for index, row in similar_users_df.iterrows():
    # Split the text into words and add them to the word_list
        recommended_article_ids.extend(row['History & Impressions'].split())

    # Remove any already read articles from the recommended articles
    recommended_article_ids = list(set([id for id in recommended_article_ids if id not in read_articles]))

    return recommended_article_ids