import uuid 
from graph.nodes.input_node import input_node
from graph.nodes.validation_node import validation_node
from graph.workflow import graph 
from config.constants import Processing

initial_state = {
    'session_id' : str(uuid.uuid4()),
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
    'followup_data' : {
        'owner' : 'second owner'
    },
    "status": Processing
}

result = graph.invoke(
    initial_state
)

print(result)