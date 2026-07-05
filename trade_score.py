def calculate_score(data):
    score=0
    for k in ["bos","choch","liquidity","orderblock","fvg"]:
        if data.get(k):
            score+=20
    if score>=80:
        signal="🟢 STRONG BUY"
    elif score>=60:
        signal="🟡 BUY"
    elif score>=40:
        signal="🟠 WAIT"
    else:
        signal="🔴 NO TRADE"
    return score,signal
