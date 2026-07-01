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
            result = analyze_chart(symbol, timeframe)

    st.success("Analysis Complete")

    st.subheader("📊 SHER AI Result")

    st.metric("Trend", result["trend"])
    st.metric("Confidence", result["confidence"])

    st.write("### Trade Setup")

    st.write("📍 Entry :", result["entry"])
    st.write("🛑 Stop Loss :", result["stoploss"])
    st.write("🎯 Target 1 :", result["target1"])
    st.write("🎯 Target 2 :", result["target2"])
    st.write("💰 Risk Reward :", result["rr"])

    st.write("### Smart Money Concept")

    st.checkbox("BOS", value=result["bos"], disabled=True)
    st.checkbox("CHoCH", value=result["choch"], disabled=True)
    st.checkbox("Liquidity Sweep", value=result["liquidity"], disabled=True)
    st.checkbox("Order Block", value=result["orderblock"], disabled=True)
    st.checkbox("Fair Value Gap", value=result["fvg"], disabled=True)

    st.info(result["reason"])
