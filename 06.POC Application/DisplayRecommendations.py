import pandas as pd
import os
import streamlit as st

def display_recommendations(article_ids):
    
    current_path = os.getcwd()
    
    news_path = os.path.join(current_path, '..\\01.Dataset\\Small\\Clean\\Train\\news.pkl')
    
    news = pd.read_pickle(news_path)
    
    result = news.loc[news['News ID'].isin(article_ids), ['News ID', 'Category', 'SubCategory', 'Title', 'Abstract']]
    result_dict = result.set_index('News ID').to_dict(orient='index')

    modified_dict = {}
    for article_id, article_data in result_dict.items():
        modified_article_data = {}
        for key, value in article_data.items():
            if key == 'Abstract':
                modified_article_data[key] = value.capitalize()
            else:
                modified_article_data[key] = value.title()
        modified_dict[article_id] = modified_article_data

    # Define the article IDs
    article_id_1 = article_ids[0]
    article_id_2 = article_ids[1]
    article_id_3 = article_ids[2]

    # Fetch the article data
    article_1_data = modified_dict[article_id_1]
    article_2_data = modified_dict[article_id_2]
    article_3_data = modified_dict[article_id_3]

    # Extract the article information
    category_1 = article_1_data['Category']
    subcategory_1 = article_1_data['SubCategory']
    title_1 = article_1_data['Title']
    abstract_1 = article_1_data['Abstract']

    category_2 = article_2_data['Category']
    subcategory_2 = article_2_data['SubCategory']
    title_2 = article_2_data['Title']
    abstract_2 = article_2_data['Abstract']

    category_3 = article_3_data['Category']
    subcategory_3 = article_3_data['SubCategory']
    title_3 = article_3_data['Title']
    abstract_3 = article_3_data['Abstract']
    
    def truncate_text(text, limit):
        if len(text) <= limit:
            return text
        else:
            return text[:limit-3] + '...' 
    
    col1, col2, col3 = st.columns(3)
    
    title_limit = 60
    abstract_limit = 75
    
    with col1:
        st.subheader(truncate_text(title_1, title_limit))
        st.caption(category_1 + ' - ' + subcategory_1)
        st.caption(truncate_text(abstract_1, abstract_limit))
        if st.button('Read Article', key='read_article_1'):
            st.session_state['read_articles'].append(article_id_1)
            st.experimental_rerun()
    with col2:
        st.subheader(truncate_text(title_2, title_limit))
        st.caption(category_2 + ' - ' + subcategory_2)
        st.caption(truncate_text(abstract_2, abstract_limit))
        if st.button('Read Article', key='read_article_2'):
            st.session_state['read_articles'].append(article_id_2)
            st.experimental_rerun()
        
    with col3:
        st.subheader(truncate_text(title_3, title_limit))
        st.caption(category_3 + ' - ' + subcategory_3)
        st.caption(truncate_text(abstract_3, abstract_limit))
        if st.button('Read Article', key='read_article_3'):
            st.session_state['read_articles'].append(article_id_3)
            st.experimental_rerun()
            
