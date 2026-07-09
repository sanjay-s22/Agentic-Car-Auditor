from services.session_service import session_service
from graph.nodes.human_input_node import human_input_node 
from graph.nodes.validation_node import validation_node 


def resume_session(session_id: str, followup_data: dict):
    state=session_service.get_state(session_id)

    if not state:
        raise ValueError('session not found')

    state['followup_data'] = followup_data
    state = human_input_node(state)
    state = validation_node(state)
    return state 