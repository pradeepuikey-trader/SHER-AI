import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="🦁 SHER AI",
    page_icon="🦁",
    layout="wide"
)

st.title("🦁 SHER AI")
st.write("Welcome Pradeep Uikey 👋")

uploaded_file = st.file_uploader(
    "📷 Upload TradingView Screenshot",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded TradingView Chart", use_container_width=True)

    symbol = st.selectbox(
        "📈 Select Market",
        ["BTCUSDT", "NIFTY", "BANKNIFTY", "GOLD", "ETHUSDT"]
    )

    timeframe = st.selectbox(
        "⏰ Timeframe",
        ["1m", "5m", "15m", "1H", "4H", "1D"]
    )

    if st.button("🤖 Analyze Chart"):
        st.success("Analysis Started 🚀")

        st.subheader("AI Result")

        st.info(f"""
Trend : Waiting...

Symbol : {symbol}

Timeframe : {timeframe}

Entry : --

Stop Loss : --

Target : --
""")
