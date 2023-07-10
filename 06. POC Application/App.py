import streamlit as st

from NoArticlesRead.ChosenCategories import choose_categories
from NoArticlesRead.PopularityCategoryRecommender import popularity_category_recommender
from FewArticlesRead.PureContentEmbeddingsRecommender import pure_content_embeddings_recommender
from EnoughArticlesRead.FetchSimilarUsers import fetch_similar_users
from EnoughArticlesRead.CollaborativeRecommender import collaborative_recommender
from EnoughArticlesRead.CombinedEmbeddingsRecommender import combined_embeddings_recommender
from DisplayRecommendations import display_recommendations

def app():
    # Set the page configuration
    st.set_page_config(
    page_title="MIND - News Recommender",
    page_icon="newspaper",
    #layout="wide",
    #initial_sidebar_state="expanded",
    menu_items={
    #     'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "mailto:vasco.oliveira260@gmail.com?subject=MIND Recommender - Bug Report",
    #     'About': "# This is a header. This is an *extremely* cool app!"
    }
    )
    
    if 'chosen_categories' not in st.session_state:
        st.session_state['chosen_categories'] = None
        
    if 'read_articles' not in st.session_state:
        st.session_state['read_articles'] = []
        
    rec_article_ids = None
        
    if len(st.session_state['read_articles'])<=4:
        
        choose_categories()

        if st.session_state['chosen_categories']:

            rec_article_ids = popularity_category_recommender(timestamp='2019-11-14', categories=st.session_state['chosen_categories'], read_articles=st.session_state['read_articles'],k=3)

    if (len(st.session_state['read_articles'])>=5) & (len(st.session_state['read_articles'])<=7):
        
        rec_article_ids = pure_content_embeddings_recommender(st.session_state['read_articles'], timestamp='2019-11-14', articles_k=3)
        
    if len(st.session_state['read_articles'])>7:
        
        similar_users_timestamps = fetch_similar_users(st.session_state['read_articles'], timestamp='2019-11-14', k=5)
        
        recommended_article_ids = collaborative_recommender(st.session_state['read_articles'], timestamp='2019-11-14', similar_users_timestamps=similar_users_timestamps)
        
        rec_article_ids = combined_embeddings_recommender(st.session_state['read_articles'], timestamp='2019-11-14', recommended_article_ids=recommended_article_ids, k=3)  
    
    if rec_article_ids:

        display_recommendations(rec_article_ids)

if __name__ == "__main__":
    app()
    
    
