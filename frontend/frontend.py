import streamlit as st
import requests

# URL for your FastAPI backend (adjust the port if needed)
API_URL = "http://127.0.0.1:8000/recommendations/"

# Streamlit interface
st.title("GenAI-powered Smart Retail Experience")

# Input from the user: product name or a natural language query
product_name = st.text_input("Enter a product name or ask a question:", "")

# Option to specify number of recommendations
top_n = st.number_input("Number of recommendations:", min_value=1, max_value=10, value=5)

# Button to trigger the recommendation process
if st.button("Get Recommendations"):
    if product_name:
        # Send the request to FastAPI backend
        params = {"product_name": product_name, "top_n": top_n}
        response = requests.get(API_URL, params=params)
        
        if response.status_code == 200:
            recommendations = response.json()
            if recommendations:
                st.subheader(f"Top {top_n} recommendations for '{product_name}':")
                for idx, recommendation in enumerate(recommendations, 1):
                    st.write(f"{idx}. {recommendation['product_name']} (Aisle: {recommendation['aisle']}, Department: {recommendation['department']})")
            else:
                st.write("No recommendations found.")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    else:
        st.warning("Please enter a product name or query.")

