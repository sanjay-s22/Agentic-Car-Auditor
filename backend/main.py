
'''
from graph.state import AuditState

state: AuditState = {
    "user_input": "2020 Hyundai i20",
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

print(state)
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
print(result["vehicle_data"])