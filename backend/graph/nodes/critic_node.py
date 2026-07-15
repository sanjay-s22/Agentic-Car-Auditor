from config.constants import Critic_complete

def critic_node(state):
    risk_data = state.get('risk_data')
    negotiation_data = state.get('negotiation_data')
    decision_data = state.get('decision_data')

    if risk_data is None:
        raise ValueError('risk_data missing from state')

    if negotiation_data is None:
        raise ValueError('negotiation_data missing from state')

    if decision_data is None:
        raise ValueError('decision_data missing from state')

    issues = []

    risk_level = risk_data['risk_level']
    recommendation = decision_data['recommendation']
    offer_price = negotiation_data['offer_price']
    target_price = negotiation_data['target_price']
    walk_away_price = negotiation_data['walk_away_price']

    if (
        risk_level == 'HIGH'
        and recommendation == 'BUY'
    ):
        issues.append('High risk vehicle cannot be recommended as BUY')

    if (
        risk_level == 'LOW'
        and recommendation == 'AVOID'
    ):
        issues.append('Low risk vehicle cannot be recommended as AVOID')
    
    if (
    offer_price is None
    or target_price is None
    or walk_away_price is None):
        return state


    if offer_price > target_price:
        issues.append('Offer price exceeds target price')

    if target_price > walk_away_price:
        issues.append('Target price exceeds walk away price')

    if (
    offer_price is None
    or target_price is None
    or walk_away_price is None):

       state["critic_data"] = {
            "issues": [
            "Negotiation skipped due to missing market price"]
    }

    return state