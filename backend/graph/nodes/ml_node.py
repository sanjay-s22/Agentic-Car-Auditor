import pandas as pd
from graph.state import AuditState 
from services.model_service import model


def ml_node(state : AuditState):
    model_input = state['model_input']
    print(model_input)
    return state 
