import json
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model=genai.GenerativeModel("gemini-2.5-flash")

def analyze_image(image):
    prompt="""
Return ONLY valid JSON:
{
"trend":"",
"confidence":"",
"entry":"",
"stoploss":"",
"target1":"",
"target2":"",
"bos":true,
"choch":false,
"liquidity":true,
"orderblock":true,
"fvg":false,
"reason":""
}
"""
    response=model.generate_content([prompt,image])
    text=response.text.replace("```json","").replace("```","").strip()
    return json.loads(text)
