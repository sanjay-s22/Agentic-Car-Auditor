from config.constants import Report_generated

def report_node(state):
    vehicle_data = state.get('vehicle_data')
    market_data = state.get('market_data')
    risk_data = state.get('risk_data')
    negotiation_data = state.get('negotiation_data')
    decision_data = state.get('decision_data')

    if vehicle_data is None:
        raise ValueError('vehicle_data missing from state')
 
    if market_data is None:
        raise ValueError('market_data missing from state')

    if risk_data is None:
        raise ValueError('risk_data missing from state')

    if negotiation_data is None:
        raise ValueError('negotiation_data missing from state')
    
    if decision_data is None:
        raise ValueError('decision_data missing from state')
    
    recommendation = decision_data['recommendation']
    state['report'] = {
    'summary': recommendation,
    'vehicle_details': {
        'brand': vehicle_data['brand'],
        'model': vehicle_data['model'],
        'year': vehicle_data['year']
    },

    'market_snapshot': {
        'average_price':
            market_data['avg_market_price'],
        'listing_count':
            market_data['listing_count']
    },

    'risk_assessment': {
        'risk_level':
            risk_data['risk_level'],
        'risk_score':
            risk_data['risk_score'],
        'key_risks':
            risk_data['reasons']
    },

    'pricing_strategy': {
        'offer_price':
            negotiation_data['offer_price'],
        'target_price':
            negotiation_data['target_price'],
        'walk_away_price':
            negotiation_data['walk_away_price']
    }
}
    state['status'] = Report_generated
    return state
