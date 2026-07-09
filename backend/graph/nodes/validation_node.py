from config.constants import (Waiting_for_input, Validated)
from services.session_service import session_service

def validation_node(state):
    vehicle_data = state['vehicle_data']
    missing_fields = []
    required_fields = [
        'brand',
        'model',
        'year',
        'fuel_type',
        'km_driven',
        'owner',
        'city'
    ]

    for field in required_fields:
        value = vehicle_data.get(field)
        if value is None: 
            missing_fields.append(field)
    
    state['missing_fields'] = missing_fields

    if missing_fields:
        state['status'] = Waiting_for_input
        session_service.save_state(state['session_id'], state)
    else:
        state['status'] = Validated 
    return state 
