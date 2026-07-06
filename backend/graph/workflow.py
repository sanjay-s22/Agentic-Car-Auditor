from langgraph import graph
from langgraph.graph import StateGraph
from langgraph.graph import END
from graph.state import AuditState
from graph.nodes.input_node import input_node
from graph.nodes.validation_node import validation_node
from graph.routers import validation_router 

builder = StateGraph(AuditState)
builder.add_node('input_node', input_node)
builder.add_node('validation_node', validation_node)
builder.set_entry_point('input_node')

builder.add_edge('input_node', 'validation_node')
builder.add_conditional_edges('validation_node', validation_router, 
{
    'validated' : END,
    'missing_information' : END
})

graph = builder.compile()
