import streamlit as st
from PIL import Image
from ai_engine import analyze_chart

st.set_page_config(
    page_title="🦁 SHER AI",
    page_icon="🦁",
    layout="wide"
)

st.title("🦁 SHER AI")
st.caption("Smart Hybrid Engine for Risk Analysis")

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

    if st.button("🤖 Analyze with Gemini AI"):

        with st.spinner("Analyzing Chart..."):

            result = analyze_chart(image)

        if result["success"]:

            analysis = result["analysis"]

            st.success("Analysis Complete ✅")

            st.subheader("📊 SHER AI Result")

            c1, c2 = st.columns(2)

            with c1:
                st.metric("Trend", analysis["trend"])
                st.metric("Confidence", analysis["confidence"])
                st.metric("Entry", analysis["entry"])
                st.metric("Target 1", analysis["target1"])

            with c2:
                st.metric("Stop Loss", analysis["stoploss"])
                st.metric("Target 2", analysis["target2"])

            st.divider()

            st.subheader("🧠 Smart Money Concept")

            a, b = st.columns(2)

            with a:
                st.checkbox("BOS", value=analysis["bos"], disabled=True)
                st.checkbox("Liquidity Sweep", value=analysis["liquidity"], disabled=True)
                st.checkbox("Fair Value Gap", value=analysis["fvg"], disabled=True)

            with b:
                st.checkbox("CHoCH", value=analysis["choch"], disabled=True)
                st.checkbox("Order Block", value=analysis["orderblock"], disabled=True)

            st.divider()

            st.subheader("💡 AI Reason")

            st.info(analysis["reason"])

        else:

            st.error(result["analysis"])
