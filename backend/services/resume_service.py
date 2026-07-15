from services.session_service import session_service
from graph.nodes.human_input_node import human_input_node 
from graph.nodes.validation_node import validation_node 
from graph.nodes.market_node import market_node
from graph.nodes.risk_node import risk_node
from graph.nodes.negotiation_node import negotiation_node
from graph.nodes.decision_node import decision_node
from graph.nodes.critic_node import critic_node
from graph.nodes.report_node import report_node

def resume_session(
    session_id: str,
    followup_data: dict):
    state = session_service.get_state(session_id)

    if not state:
        raise ValueError('session not found')

    state['followup_data'] = followup_data
    state = human_input_node(state)
    state = validation_node(state)

    if state['missing_fields']:
        return state

    state = market_node(state)
    state = risk_node(state)
    state = negotiation_node(state)
    state = decision_node(state)
    state = critic_node(state)
    state = report_node(state)
    return state