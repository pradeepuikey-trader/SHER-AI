def calculate_score(data):
    score = 0
    for key in ["bos","choch","liquidity","orderblock","fvg"]:
        if data.get(key):
            score += 20

    confidence = score

    if score >= 80:
        signal = "🟢 STRONG BUY"
    elif score >= 60:
        signal = "🟢 BUY"
    elif score >= 40:
        signal = "🟡 WAIT"
    else:
        signal = "🔴 SELL"

    return score, signal, confidence
