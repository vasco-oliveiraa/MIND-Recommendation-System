# Sokovia News Recommender System - MIND

Welcome to the Sokovia News Recommender System project! This project aims to deliver personalized news article recommendations to users, enhancing their engagement and satisfaction while exploring the Sokovia News platform. By implementing recommender models, we can provide accurate and diverse recommendations based on user preferences and article characteristics.

## Table of Contents
1. [Introduction](#introduction)
2. [Data Analysis](#data-analysis)
3. [Data Preparation and Feature Engineering](#data-preparation-and-feature-engineering)
4. [Recommender Models](#recommender-models)
5. [Model Evaluation](#model-evaluation)
6. [Business Application and ROI](#business-application-and-roi)
7. [Production and Deployment](#production-and-deployment)
8. [Future Improvements](#future-improvements)

## Introduction
This project explores the development of a news recommender system for Sokovia News, aiming to deliver tailored news articles to users. The importance of personalized news recommendations in today's information-rich world is emphasized, and two main approaches in recommender systems are discussed: content-based filtering and collaborative filtering. To provide accurate and diverse recommendations, a hybrid model that combines both approaches is proposed.

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

## Production and Deployment
To efficiently deploy the models in production, Microsoft Azure Cloud has been chosen as the preferred architecture. It provides dynamic resource allocation, scalability, and cost efficiency through a pay-as-you-go model. Legal and regulatory requirements, such as data privacy regulations, encryption measures, and intellectual property protection, have been addressed to ensure compliance and user trust.

## Future Improvements
Looking ahead, the focus is on creating an in-house dataset that incorporates user demographics, article ratings, and real-time external events. This dataset enhancement will further improve the accuracy and relevance of the recommendations, providing a more customized news experience for users. Continuous improvement and optimization of the recommender system are essential to stay competitive in the news industry.

Thank you for your interest in the Sokovia News Recommender System project. We hope that this system will enhance your news reading experience and contribute to your engagement with our platform.
