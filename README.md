GenAI Smart Retail Recommendation System

Overview
GenAI Smart Retail Recommendation System is a machine learning-based project that leverages product data and customer information to provide personalized product recommendations. 
The system integrates with FastAPI to create an API for retrieving recommendations and utilizes modern recommendation techniques like cosine similarity for product similarity analysis. 
It also includes integration with the OpenAI API for natural language processing (though the OpenAI integration is not active in the current version due to API quota limitations).

Features

1. Product Recommendations: Get personalized product recommendations based on the input product name.
2. API Integration: Built using FastAPI for fast and efficient interaction with the backend.
3. Data Analysis: Uses product data, including details like product name, aisle, and department, to generate recommendations.
4. Frontend: A simple Streamlit frontend to interact with the backend API for recommendations.

Technologies Used

1. Python: Core programming language for backend and logic.
2. FastAPI: Used for building the RESTful API to fetch recommendations.
3. Streamlit: Simple frontend to visualize product recommendations.
4. Cosine Similarity: Used for measuring product similarity based on textual data.
5. OpenAI API: Integrated for enhancing recommendations via natural language processing (though not currently active due to API quota).
6. Pandas: Data manipulation and handling for product datasets.
7. Scikit-learn: For calculating similarity scores and handling machine learning models.

Data Used: Instacart Retail User Data 
