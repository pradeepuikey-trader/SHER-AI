import streamlit as st
import google.generativeai as genai
import json

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_image(image):

    prompt = """
You are an expert Smart Money Concept trader.

Analyze this TradingView screenshot.

Return ONLY valid JSON.

No markdown.
No explanation.
No ```json.

JSON format:

{
    "trend":"",
    "entry":"",
    "stoploss":"",
    "target1":"",
    "target2":"",
    "confidence":"",
    "bos":true,
    "choch":true,
    "liquidity":true,
    "orderblock":true,
    "fvg":true,
    "reason":""
}
"""

    response = model.generate_content(
        contents=[prompt, image]
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return json.loads(text)
