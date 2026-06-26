from langgraph.graph import StateGraph
from langgraph.graph import END
from graph.state import AuditState 
from graph.nodes.input_node import input_node 
from graph.nodes.validation_node import validation_node 
from graph.nodes.human_loop_node import human_loop_node 
from graph.nodes.feature_enrichment_node import feature_enrichment_node
from graph.nodes.ml_node import ml_node 
from graph.nodes.model_validation_node import model_validation_node


def validation_router(state: AuditState):
    if state['validation_passed']:
        return 'feature_enrichment'
        
    return 'human_loop'

def model_validation_router(state):
    if state['model_validation_passed']:
        return 'ml'
    return 'human_loop'


builder = StateGraph(AuditState)
builder.add_node('input', input_node)
builder.add_node('validation', validation_node )
builder.add_node('human_loop', human_loop_node )
builder.add_node('feature_enrichment', feature_enrichment_node)
builder.add_node('ml', ml_node) 
builder.add_node('model_validation', model_validation_node)
builder.set_entry_point ('input')
builder.add_edge('input', 'validation')
builder.add_conditional_edges(
    'validation', validation_router,
    {
        'human_loop': 'human_loop',
        'feature_enrichment': 'feature_enrichment'
    },
)
builder.add_conditional_edges('model_validation', model_validation_router,
    {
    'ml' : 'ml',
    'human_loop' : 'human_loop'
    }
)

builder.add_edge('feature_enrichment', 'model_validation')
builder.add_edge('ml', END)

graph = builder.compile()

