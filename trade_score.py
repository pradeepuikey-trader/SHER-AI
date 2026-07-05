def calculate_score(data):

    score = 0

    if data["bos"]:
        score += 20

    if data["choch"]:
        score += 20

    if data["liquidity"]:
        score += 20

    if data["orderblock"]:
        score += 20

    if data["fvg"]:
        score += 20

    confidence = int(score)

    if score >= 80:
        signal = "🟢 STRONG BUY"

    elif score >= 60:
        signal = "🟢 BUY"

    elif score >= 40:
        signal = "🟡 WAIT"

    else:
        signal = "🔴 SELL"

    return score, signal, confidence
