from config.constants import Risk_analyzed

def risk_node(state):
    vehicle_data = state.get('vehicle_data')
    if not vehicle_data:
        raise ValueError('vehicle_data missing from state')
    vehicle_data = state['vehicle_data']

    risk_score = 0
    reasons = []
    owner = vehicle_data['owner'].lower()
    
    if 'second' in owner:
        risk_score += 10
        reasons.append('Multiple ownership history')
    elif 'third' in owner:
        risk_score += 20
        reasons.append('Multiple ownership history')
    elif 'fourth' in owner:
        risk_score += 30
        reasons.append('Multiple ownership history')
    if vehicle_data['km_driven'] > 100000:
        risk_score += 30
        reasons.append('High mileage vehicle')
    if vehicle_data['year'] < 2015:
        risk_score += 25
        reasons.append('Older vehicle')
    if risk_score >= 60:
        risk_level = 'HIGH'
    elif risk_score >= 30:
        risk_level = 'MEDIUM'
    else:
        risk_level = 'LOW'

    state['risk_data'] = {
        'risk_score': risk_score,
        'risk_level': risk_level,
        'reasons': reasons
    }

    state['status'] = Risk_analyzed
    return state