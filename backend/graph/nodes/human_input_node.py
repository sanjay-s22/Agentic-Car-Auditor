from config.constants import Processing

def human_input_node(state):
    vehicle_data = state['vehicle_data']
    followup_data = state['followup_data']
    vehicle_data.update(followup_data)
    state['vehicle_data'] = vehicle_data
    state['followup_data'] = {}
    state['status'] = Processing
    return state 