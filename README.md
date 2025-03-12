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

Installation and Setup

Prerequisites
1. Python 3.8 or higher
2. Git (for cloning the repository)
3. Access to the OpenAI API (if you want to use the OpenAI integration)

Running the project 
1. Clone the repo
2. Create and activate virtual environment
3. Install pacakges from requirements.txt
4. Apply recommendation functions on data
5. Run the backend (FastAPI)
   Use following command:
   cd backend;
   uvicorn main:app --reload
6. Run the frontend (Streamlit)
   Use following command:
   cd frontend;
   streamlit run frontend.py
7. Access the Recommendation API:Use the API endpoint /recommendations/ to get product recommendations based on the input product name. If you are using OpenAI, it will provide more personalized recommendations based on user queries.

