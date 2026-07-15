from config.constants import Decision_complete

def decision_node(state):
    risk_data = state.get('risk_data')

    if not risk_data:
        raise ValueError('risk_data missing from state')

    risk_level = risk_data.get('risk_level')

    if not risk_level:
        raise ValueError('risk_level missing from risk_data')

    if risk_level == 'LOW':
        recommendation = 'BUY'

    elif risk_level == 'MEDIUM':
        recommendation = 'NEGOTIATE'

    elif risk_level == 'HIGH':
        recommendation = 'AVOID'

    else:
        raise ValueError(f'Invalid risk level: {risk_level}')

    state['decision_data'] = {
        'recommendation': recommendation}

    state['status'] = Decision_complete

    return state