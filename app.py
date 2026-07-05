import streamlit as st
from PIL import Image
from ai_engine import analyze_chart
from trade_score import calculate_score

st.set_page_config(page_title="SHER AI PRO", page_icon="🦁", layout="wide")
st.title("🦁 SHER AI PRO")
st.caption("Professional Smart Money Concept AI")

uploaded_file = st.file_uploader("📷 Upload TradingView Screenshot", type=["png","jpg","jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_container_width=True)

    if st.button("🤖 Analyze with Gemini AI"):
        with st.spinner("Gemini AI is analyzing chart..."):
            result = analyze_chart(image)

        if result["success"]:
            analysis = result["analysis"]
            score, signal, confidence = calculate_score(analysis)
            st.success(signal)
            st.markdown("---")

if "BUY" in signal:
    st.success(f"## {signal}")

elif "SELL" in signal:
    st.error(f"## {signal}")

else:
    st.warning(f"## {signal}")

st.progress(confidence / 100)

st.metric(
    "⭐ AI Confidence",
    f"{confidence}%"
)

st.markdown("---")
            st.progress(score/100)
            st.metric("⭐ AI Trade Score", f"{score}/100")

            c1,c2=st.columns(2)
            with c1:
                st.metric("Trend", analysis["trend"])
                
                st.metric("Entry", analysis["entry"])
                st.metric("Target 1", analysis["target1"])
            with c2:
                st.metric("Stop Loss", analysis["stoploss"])
                st.metric("Target 2", analysis["target2"])

            st.subheader("🧠 Smart Money Concept")
            st.checkbox("BOS", value=analysis["bos"], disabled=True)
            st.checkbox("CHoCH", value=analysis["choch"], disabled=True)
            st.checkbox("Liquidity", value=analysis["liquidity"], disabled=True)
            st.checkbox("Order Block", value=analysis["orderblock"], disabled=True)
            st.checkbox("FVG", value=analysis["fvg"], disabled=True)

            st.info(analysis["reason"])
        else:
            st.error(result["analysis"])
