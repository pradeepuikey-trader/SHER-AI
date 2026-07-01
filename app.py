import streamlit as st

st.set_page_config(page_title="SHER AI", page_icon="🦁")

st.title("🦁 SHER AI")
st.write("Welcome Pradeep Uikey 👋")

st.file_uploader("📷 Upload TradingView Screenshot")

if st.button("📊 Analyze"):
    st.success("AI Engine Coming Soon...")
