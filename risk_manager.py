def calculate_rr(entry, stoploss, target):

    try:
        entry = float(entry)
        stoploss = float(stoploss)
        target = float(target)

        risk = abs(entry - stoploss)
        reward = abs(target - entry)

        if risk == 0:
            return {
                "risk": 0,
                "reward": 0,
                "rr": "0 : 0"
            }

        rr = round(reward / risk, 2)

        return {
            "risk": risk,
            "reward": reward,
            "rr": f"1 : {rr}"
        }

    except:
        return {
            "risk": "-",
            "reward": "-",
            "rr": "-"
        }
