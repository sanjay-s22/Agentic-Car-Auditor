from graph.state import AuditState

required_fields = [
    'brand',
    'model',
    'year',
    'fuel',
    'kms_driven',
    'owner',
]

def validation_node(state : AuditState):
    vehicle = state['vehicle_data']
    missing_fields = []

    for field in required_fields:
        if field not in vehicle:
            missing_fields.append(field)

    state['missing_fields'] = missing_fields 
    state['validation_passed'] = (len(missing_fields) ==0
    )
    return state  
    