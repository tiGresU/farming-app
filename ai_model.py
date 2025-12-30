import os
import requests
from dotenv import load_dotenv

load_dotenv("myapi.env")
OPENAI_API_KEY = os.getenv("OPEN_AI_API_KEY")

# -----------------------------------------
# LOW-LEVEL OPENAI CALL
# -----------------------------------------
def call_openai(prompt):
    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are an expert agriculture farm assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    if "choices" in data:
        return data["choices"][0]["message"]["content"]

    return "AI response not available."


# -----------------------------------------
# AI FOR ML-BASED RECOMMENDATION
# -----------------------------------------
def generate_farm_ai_response(predicted_value, area, year):
    prompt = f"""
You are an agriculture farm management assistant.

ML Prediction:
- Area code: {area}
- Year: {year}
- Predicted pesticide usage: {predicted_value}

Give clear, simple, farmer-friendly advice.
Use bullet points.
Avoid technical words.
"""

    return call_openai(prompt)


# -----------------------------------------
# AI CHATBOT (QUESTION-BASED)
# -----------------------------------------
def farm_chatbot_response(question):
    prompt = f"""
You are an AI Farm Assistant.

IMPORTANT RULES:
- Use very simple words
- Use short bullet points
- EACH FIELD MUST BE ON A NEW LINE
- DO NOT write in paragraph form

STRICT OUTPUT FORMAT (EXACT):

Crop:
Problem (Pest/Disease):
Recommended Pesticide:
Dosage:
Waiting Period:
Safety Notes:
Alternative Options:

Farmer Question:
{question}
"""
    return call_openai(prompt)
