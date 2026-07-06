def calculate_position_size(capital, risk_percent, entry, stoploss):

    try:
        capital = float(capital)
        risk_percent = float(risk_percent)
        entry = float(entry)
        stoploss = float(stoploss)

        risk_amount = capital * (risk_percent / 100)

        sl_distance = abs(entry - stoploss)

        if sl_distance == 0:
            return {
                "risk_amount": 0,
                "position_size": 0
            }

        position_size = round(risk_amount / sl_distance, 4)

        return {
            "risk_amount": round(risk_amount, 2),
            "position_size": position_size
        }

    except:
        return {
            "risk_amount": "-",
            "position_size": "-"
        }
