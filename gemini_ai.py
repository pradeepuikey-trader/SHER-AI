import streamlit as st
import google.generativeai as genai
import json

# Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_image(image):

    prompt = """
You are an expert Smart Money Concept (SMC) trader.

Analyze this TradingView chart carefully.

Return ONLY valid JSON.

{
    "trend":"Bullish/Bearish/Sideways",
    "confidence":"85%",
    "entry":"00000",
    "stoploss":"00000",
    "target1":"00000",
    "target2":"00000",
    "bos":true,
    "choch":false,
    "liquidity":true,
    "orderblock":true,
    "fvg":false,
    "reason":"Short professional explanation"
}

Rules:

- Confidence must always be percentage.
Example:
82%
91%
76%

Never return:
High
Medium
Low
4
4/5

Return Entry, Stoploss and Targets as price numbers only.

Return only JSON.

Do not write markdown.

Do not use ```json

Do not explain anything outside JSON.
"""

    response = model.generate_content([prompt, image])

    text = response.text.strip()

    # Remove markdown if Gemini adds it
    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    return json.loads(text)
