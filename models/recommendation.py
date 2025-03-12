#Import Libraries

import os
import math
import scipy
import numpy as np
import pandas as pd

#Import the libraries (for recomm)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, "data")

#Import all the datasets 
df1 = pd.read_csv(os.path.join(DATA_DIR, 'products.csv'))
df2 = pd.read_csv(os.path.join(DATA_DIR, 'aisles.csv'))
df3 = pd.read_csv(os.path.join(DATA_DIR, 'departments.csv'))
df4 = pd.read_csv(os.path.join(DATA_DIR, 'order_products__train.csv'))
df5 = pd.read_csv(os.path.join(DATA_DIR, 'orders.csv'))


#Merge all these datasets into a single df for further recommendation
df1_2 = pd.merge(df2, df1, how='inner', on='aisle_id')
df12_3 = pd.merge(df1_2, df3, how='inner', on='department_id')
df123_4 = pd.merge(df4, df12_3, how='inner', on='product_id')
df1234_5 = pd.merge(df5, df123_4, how='inner', on='order_id')

#Drop irrelevant columns
data_cleaned = df1234_5.drop(['aisle_id','department_id','eval_set'],axis=1)

# Select relevant columns for recommendation
df_cleaned = data_cleaned[['product_id', 'product_name', 'aisle', 'department']]

# Drop duplicates (if any)
df_cleaned = df_cleaned.drop_duplicates(subset=['product_id'])

# Combine product-related features into a single text field
df_cleaned['combined_features'] = df_cleaned['product_name'] + " " + df_cleaned['aisle'] + " " + df_cleaned['department']

df_cleaned = df_cleaned.reset_index(drop=True)

# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

# Convert text data into TF-IDF matrix
tfidf_matrix = vectorizer.fit_transform(df_cleaned['combined_features'])

# Compute cosine similarity between products
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

df_cleaned['product_name_lower'] = df_cleaned['product_name'].str.lower()

def recommend_products(product_name, top_n=5):
    # Check if product exists in the 'product_name_lower' column
    product_name = product_name.lower()  # Make input lowercase for case-insensitive matching
    
    if product_name not in df_cleaned['product_name_lower'].values:
        return {"error": "Product not found!"}

    # Find the index of the product in the dataframe
    idx = df_cleaned[df_cleaned['product_name_lower'] == product_name].index[0]
    
    # Get similarity scores for the selected product
    sim_scores = sorted(list(enumerate(cosine_sim[idx])), key=lambda x: x[1], reverse=True)

    # Get top N recommendations (excluding the input product itself)
    top_products = sim_scores[1:top_n + 1]
    
    # Retrieve the product indices for the top recommendations
    product_indices = [i[0] for i in top_products]
    
    # Return top N recommended products as a dictionary
    return df_cleaned.iloc[product_indices][['product_id', 'product_name', 'aisle', 'department']].to_dict(orient='records')















