from config.constants import Negotiation_complete


def negotiation_node(state):
    market_data = state.get("market_data")

    if not market_data:
        raise ValueError("market_data missing from state")

    risk_data = state.get("risk_data")

    if not risk_data:
        raise ValueError("risk_data missing from state")

    avg_market_price = market_data.get("avg_market_price")
    risk_level = risk_data["risk_level"]

    # TEMPORARY GUARD
    if avg_market_price is None:

        state["negotiation_data"] = {
            "offer_price": None,
            "target_price": None,
            "walk_away_price": None,
        }

        state["status"] = Negotiation_complete
        return state

    if risk_level == "LOW":
        offer_price = round(avg_market_price * 0.95)
        target_price = round(avg_market_price * 0.98)
        walk_away_price = round(avg_market_price)

    elif risk_level == "MEDIUM":
        offer_price = round(avg_market_price * 0.90)
        target_price = round(avg_market_price * 0.95)
        walk_away_price = round(avg_market_price * 0.98)

    elif risk_level == "HIGH":
        offer_price = round(avg_market_price * 0.80)
        target_price = round(avg_market_price * 0.90)
        walk_away_price = round(avg_market_price * 0.95)

    else:
        raise ValueError(f"Invalid risk level: {risk_level}")

    state["negotiation_data"] = {
        "offer_price": offer_price,
        "target_price": target_price,
        "walk_away_price": walk_away_price,
    }

    state["status"] = Negotiation_complete
    return state