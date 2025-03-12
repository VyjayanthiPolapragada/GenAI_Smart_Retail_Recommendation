from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

import sys
import os

# Add the root directory (GenAI_Smart_Retail) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the recommendation function from models/recommendation.py
from models.recommendation import recommend_products
# Import the function for OpenAI interaction
from models.openai_integrate import get_relevant_product_from_query

app = FastAPI()

# Define a Pydantic model for the input (product_name and top_n)
class RecommendationRequest(BaseModel):
    product_name: str
    top_n: int = 5  # Default to 5 recommendations

@app.get("/")
def read_root():
    return {"message": "Welcome to GenAI-powered Smart Retail API!"}

# Recommendation endpoint
@app.get("/recommendations/")
def get_recommendations(product_name: str, top_n: int = 5):
    # Check if the product name is in question form (natural language query)
    if "?" in product_name:
        try:
            # Call the OpenAI integration to retrieve relevant product
            product_name = get_relevant_product_from_query(product_name)
        except Exception as e:
            # If OpenAI fails, return a fallback message
            return JSONResponse(
                content={"error": "OpenAI API failed: " + str(e)},
                status_code=500
            )

    # Call the recommendation function and get the result
    recommendations = recommend_products(product_name, top_n)

    if "error" in recommendations:
        return JSONResponse(content=recommendations, status_code=404)

    return recommendations





