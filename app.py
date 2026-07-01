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

    st.write(f"Market : **{symbol}**")
    st.write(f"Timeframe : **{timeframe}**")

    if st.button("🤖 Analyze with Gemini AI"):

        with st.spinner("Gemini AI is analyzing chart..."):

            result = analyze_chart(image)

        if result["success"]:

            st.success("Analysis Completed")

            st.subheader("🦁 SHER AI Report")

            st.markdown(result["analysis"])

        else:

            st.error(result["analysis"])
