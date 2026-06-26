from graph.state import AuditState 

def human_loop_node(state : AuditState):
    state['status'] = 'Waiting For Input'
    return state 
    