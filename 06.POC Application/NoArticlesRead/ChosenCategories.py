import streamlit as st
import pandas as pd
import os

def choose_categories():
    
    current_path = os.getcwd()
    
    news_path = os.path.join(current_path, '..\\01.Dataset\\Small\\Clean\\Train\\news.pkl')
    
    news = pd.read_pickle(news_path)

    categories = {category.title() for category in news.Category.unique()}
    
    chosen_categories = st.multiselect('Choose Your Categories of Interest', categories)
    
    chosen_categories = [word.lower() for word in chosen_categories]
    
    st.session_state['chosen_categories'] = chosen_categories