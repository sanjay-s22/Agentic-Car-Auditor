from graph.state import AuditState


def feature_enrichment_node(state: AuditState):

    vehicle = state["vehicle_data"]
    state['model_input'] = {
        'km_driven' : vehicle['kms_driven'],
        'car_age' : 2026 - vehicle['year'],
        'fuel' : vehicle['fuel'],
        'owner' : vehicle['owner'],
        'brand' : vehicle['brand'],
        'model_family' : vehicle['model']
    }

    vehicle['car_age'] = state['model_input'] ['car_age']
    return state 