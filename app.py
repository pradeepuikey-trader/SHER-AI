from position_size import calculate_position_size
from risk_manager import calculate_rr
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

        with st.spinner("Gemini AI is analyzing chart..."):

            result = analyze_chart(image)

        if result["success"]:

            analysis = result["analysis"]
           capital = 10000
           risk_percent = 2

           position = calculate_position_size(
           capital,
               risk_percent,
               analysis["entry"],
               analysis["stoploss"]
)
            rr = calculate_rr(
               analysis["entry"],
               analysis["stoploss"],
               analysis["target1"]
            )
            score, signal, confidence = calculate_score(analysis)

            if "BUY" in signal:
                st.success(signal)
            elif "SELL" in signal:
                st.error(signal)
            else:
                st.warning(signal)

            st.progress(confidence / 100)

            st.metric(
                "⭐ AI Confidence",
                f"{confidence}%"
            )

            st.progress(score / 100)

            st.metric(
                "⭐ AI Trade Score",
                f"{score}/100"
            )

            st.divider()

            c1, c2 = st.columns(2)

            with c1:

                st.metric("Trend", analysis["trend"])
                st.metric("Entry", analysis["entry"])
                st.metric("Target 1", analysis["target1"])

            with c2:

                st.metric("Stop Loss", analysis["stoploss"])
                st.metric("Target 2", analysis["target2"])

                st.metric("Risk", rr["risk"])
                st.metric("Reward", rr["reward"])
                st.metric("Risk : Reward", rr["rr"])

                st.metric("💰 Capital", f"₹{capital}")
                st.metric("⚠ Risk %", f"{risk_percent}%")
                st.metric("💸 Max Risk", f"₹{position['risk_amount']}")
                st.metric("📦 Position Size", position["position_size"])


            st.divider()

            st.subheader("🧠 Smart Money Concept")

            st.checkbox(
                "BOS",
                value=analysis["bos"],
                disabled=True
            )

            st.checkbox(
                "CHoCH",
                value=analysis["choch"],
                disabled=True
            )

            st.checkbox(
                "Liquidity Sweep",
                value=analysis["liquidity"],
                disabled=True
            )

            st.checkbox(
                "Order Block",
                value=analysis["orderblock"],
                disabled=True
            )

            st.checkbox(
                "Fair Value Gap",
                value=analysis["fvg"],
                disabled=True
            )

            st.subheader("💡 AI Reason")

            st.info(analysis["reason"])

        else:

            st.error(result["analysis"])
