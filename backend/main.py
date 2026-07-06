
'''
from graph.nodes.input_node import input_node

state = {
    "user_input": """
    2020 Hyundai i20 Petrol
    55000 km
    Second Owner
    Chennai
    """,
    "vehicle_data": {},
    "missing_fields": [],
    "market_data": {},
    "risk_data": {},
    "negotiation_data": {},
    "decision_data": {},
    "critic_data": {},
    "report": {},
    "confidence": 0,
    "status": "PROCESSING"
}
result = input_node(state)
print(result["vehicle_data"])'''


from graph.nodes.input_node import input_node
from graph.nodes.validation_node import validation_node
from graph.workflow import graph 
from config.constants import Processing

initial_state = {
    "user_input": """
    2020 Hyundai i20 Petrol
    55000 km
    Chennai
    """,

    "vehicle_data": {},
    "missing_fields": [],
    "market_data": {},
    "risk_data": {},
    "negotiation_data": {},
    "decision_data": {},
    "critic_data": {},
    "report": {},
    "confidence": 0,
    "status": Processing
}

result = graph.invoke(
    initial_state
)

print(result)