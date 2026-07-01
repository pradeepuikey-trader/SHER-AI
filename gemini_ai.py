import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_image(image):

    prompt = """
    You are a professional Smart Money Concept trader.

    Analyze this TradingView chart.

    Return ONLY in this format:

    Trend:
    Entry:
    Stop Loss:
    Target 1:
    Target 2:
    Confidence:
    BOS:
    CHoCH:
    Liquidity Sweep:
    Order Block:
    Fair Value Gap:
    Reason:
    """

    response = model.generate_content(
        [prompt, image]
    )

    return response.text
