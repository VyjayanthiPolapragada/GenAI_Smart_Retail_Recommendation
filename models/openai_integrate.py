import os
import openai
from openai import OpenAI

# Enter the Open AI API Key
api_key = {'Your API Key'}


# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def get_relevant_product_from_query(query: str) -> str:
    """Uses OpenAI API to convert a natural language query into a relevant product name or category."""

    prompt = f"Identify a relevant product category or product name for the query: '{query}'. Example: 'What are the best cereals?' → 'Cereal'."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that maps user queries to product names."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )

        result = response.choices[0].message.content.strip()
        return result

    except Exception as e:
        print(f"Error in OpenAI API: {e}")
        return "Error"

