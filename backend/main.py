
import uuid
from graph.workflow import graph
from config.constants import Processing
from services.resume_service import resume_session
from services.session_service import session_service

initial_state = {
    "session_id": str(uuid.uuid4()),

    "user_input": """
    2020 Hyundai i20 Petrol
    55000 km
    second owner
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

    "followup_data": {},

    "status": Processing
}

result = graph.invoke(initial_state)

print(result)

