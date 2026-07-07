def get_decision(score, rr):

    try:
        rr_value = float(rr.replace("1 :", "").strip())

        if score >= 80 and rr_value >= 2:
            return "🟢 BUY"

        elif score >= 60 and rr_value >= 1.5:
            return "🟡 WAIT"

        else:
            return "🔴 SELL"

    except:
        return "⚪ UNKNOWN"
