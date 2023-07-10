# Sokovia News Recommender System - MIND

Welcome to the Sokovia News Recommender System project! This project aims to deliver personalized news article recommendations to users, enhancing their engagement and satisfaction while exploring the Sokovia News platform. By implementing recommender models, we can provide accurate and diverse recommendations based on user preferences and article characteristics.

## Table of Contents
1. [Introduction](#introduction)
2. [Exploratory Data Analysis](#data-analysis)
3. [Data Preparation and Feature Engineering](#data-preparation-and-feature-engineering)
4. [Recommender Models](#recommender-models)
5. [Model Evaluation](#model-evaluation)
6. [Business Application and ROI](#business-application-and-roi)
7. [Production and Deployment](#production-and-deployment)
8. [Future Improvements](#future-improvements)

## Introduction
This project explores the development of a news recommender system for Sokovia News, aiming to deliver tailored news articles to users. The importance of personalized news recommendations in today's information-rich world is emphasized, and two main approaches in recommender systems are discussed: content-based filtering and collaborative filtering. To provide accurate and diverse recommendations, a hybrid model that combines both methods is proposed.

### Data for Reproducibility

This repository does not contain the folder *01.Dataset*, where the necessary data to perform the analysis is located, due to Github's limitations on handling large data files. While in the future, we want to include a DVC version of this folder, here is the folder structure and the sources of the files you need before running the project:
<details>
<ul>
  <li>01.Dataset
    <ul>
      <li>Small
        <ul>
          <li>Original
            <ul>
              <li>Train
                <ul>
                  <li><a href="https://msnews.github.io/behaviors.tsv">behaviors.tsv</a></li>
                  <li><a href="https://msnews.github.io/news.tsv">news.tsv</a></li>
                  <li><a href="https://msnews.github.io/entity_embeddings.vec">entity_embeddings.vec</a></li>
                </ul>
              </li>
            </ul>
          </li>
          <li>Clean
            <ul>
              <li>Train</li>
                <ul>
                  <li>(Empty Folder)</li>
                </ul>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Predictions
    <ul>
      <li>(Empty Folder)</li>
    </ul>
  </li>
  <li><a href="https://nlp.stanford.edu/projects/glove/glove.6B.300d">glove.6B.300d</a></li>
  <li><a href="https://huggingface.co/fse/word2vec-google-news-300">GoogleNews-vectors-negative300-002.bin</a></li>
</ul>
</details>

## Data Analysis
The project utilized the Microsoft News Dataset (MIND), consisting of "news" and "behaviors" datasets. Preliminary data analysis provided valuable insights into the dataset's structure, data quality, user interactions, and article characteristics. These insights formed the basis for feature engineering, model selection, and system optimization.

## Data Preparation and Feature Engineering
During data preparation, missing values were handled, duplicate records were removed, and variables were transformed into appropriate formats. Textual data underwent tokenization, removal of stop words, and techniques like stemming or lemmatization. Feature engineering involved creating new variables, calculating popularity metrics, and incorporating temporal information. Collaborative filtering techniques were used to compute user similarities, enabling accurate and personalized recommendations.

## Recommender Models
Multiple recommender models were developed to provide relevant news article recommendations. For new users, a Frequency & Category-Based Recommender (Model 1) suggests popular articles within specific categories or recent articles. As users engage with the platform and accumulate a browsing history, more advanced models are employed. One of these models is the Content-Based Filtering Model (Model 2), which recommends articles based on the similarity to previously read articles. Additionally, a Collaborative Filtering & Content-Based Recommender (Model 3) combines user-to-user collaborative filtering with content-based recommendations, delivering personalized suggestions tailored to the user's preferences.

## Model Evaluation
The models were evaluated using various metrics, including Hit Ratio, Precision@5, Precision@10, Recall@5, Recall@10, MRR, nDCG@5, and nDCG@10. Model 3, the collaborative filtering model, outperformed Model 2, demonstrating its effectiveness in recommending articles aligned with user preferences. Although the models' performance falls short of state-of-the-art models, they show significant improvement over a random baseline and hold promise for business applications.

## Business Application and ROI
The recommender system offers significant business application potential for Sokovia News. By delivering personalized news article recommendations, user engagement and satisfaction can be enhanced, leading to increased ad revenues and potential conversions into premium subscriptions. The estimated ROI of the recommender system is approximately 220%, demonstrating its cost-effectiveness and value.

### Proof of Concept Streamlit App
To showcase the proof of concept of the recommender system, a simple Streamlit app has been developed. The app demonstrates the functionality of the three models at different points of the customer journey. The app provides a user interface where users can input their preferences and interact with the system to receive personalized news article recommendations.

To run the app, execute the following command:
`streamlit run App.py`

## Production and Deployment
To efficiently deploy the models in production, Microsoft Azure Cloud has been chosen as the preferred architecture. It provides dynamic resource allocation, scalability, and cost efficiency through a pay-as-you-go model. Legal and regulatory requirements, such as data privacy regulations, encryption measures, and intellectual property protection, have been addressed to ensure compliance and user trust.

## Future Improvements
Looking ahead, the focus is on creating an in-house dataset that incorporates user demographics, article ratings, and real-time external events. This dataset enhancement will further improve the accuracy and relevance of the recommendations, providing a more customized news experience for users. Continuous improvement and optimization of the recommender system are essential to stay competitive in the news industry.

Thank you for your interest in the Sokovia News Recommender System project. We hope that this system will enhance your news reading experience and contribute to your engagement with our platform.

## Acknowledgments

This project is part of the Master in Business Analytics and Big Data program as the capstone project. We would like to express our gratitude to the program faculty and staff for their guidance and support throughout this project.

The project was developed by:

- Beatriz Leitão
- Louis Ritz
- Sachin Nair
- Vasco Oliveira
- Y Chi Cindy Lange

We would also like to thank Microsoft for providing the necessary resources and data for this project.
