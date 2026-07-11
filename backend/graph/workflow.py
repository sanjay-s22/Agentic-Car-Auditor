from langgraph.graph import StateGraph
from langgraph.graph import END
from graph.state import AuditState
from graph.nodes.input_node import input_node
from graph.nodes.validation_node import validation_node
from graph.routers import validation_router 
from graph.nodes.human_input_node import human_input_node
from graph.nodes.market_node import market_node 
from graph.nodes.risk_node import risk_node

builder = StateGraph(AuditState)
builder.add_node('input_node', input_node)
builder.add_node('validation_node', validation_node)
#builder.add_node('human_input_node', human_input_node)
builder.add_node('market_node', market_node)
builder.add_node('risk_node', risk_node)

builder.set_entry_point('input_node')


builder.add_edge('input_node', 'validation_node')
builder.add_edge('market_node', 'risk_node')
builder.add_edge('risk_node', END)
builder.add_conditional_edges('validation_node', validation_router, 
{
    'validated' : 'market_node',
    'missing_information' : END
})
#builder.add_edge('human_input_node', 'validation_node')

graph = builder.compile()
