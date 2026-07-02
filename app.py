import streamlit as st
from PIL import Image
from ai_engine import analyze_chart
from trade_score import calculate_score

st.set_page_config(
    page_title="🦁 SHER AI PRO",
    page_icon="🦁",
    layout="wide"
)

st.title("🦁 SHER AI PRO")
st.caption("Professional Smart Money Concept AI")

uploaded_file = st.file_uploader(
    "📷 Upload TradingView Screenshot",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="TradingView Screenshot",
        use_container_width=True
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        symbol = st.selectbox(
            "📈 Market",
            [
                "BTCUSDT",
                "ETHUSDT",
                "NIFTY",
                "BANKNIFTY",
                "GOLD"
            ]
        )

    with col2:
        timeframe = st.selectbox(
            "⏰ Timeframe",
            [
                "1m",
                "5m",
                "15m",
                "1H",
                "4H",
                "1D"
            ]
        )

    st.write(f"### 📈 Market : {symbol}")
    st.write(f"### ⏰ Timeframe : {timeframe}")

    if st.button("🤖 Analyze with Gemini AI"):

        with st.spinner("Gemini AI is analyzing
