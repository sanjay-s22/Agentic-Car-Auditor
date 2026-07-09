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


paused_state = graph.invoke(initial_state)

print("\nPAUSED STATE")
print(paused_state)


saved_state = session_service.get_state(
    paused_state['session_id']
)

print("\nSAVED STATE")
print(saved_state)


resumed_state = resume_session(
    paused_state['session_id'],
    {
        'owner': 'Second Owner'
    }
)

print("\nRESUMED STATE")
print(resumed_state)




'''
from services.session_service import session_service

session_service.save_state(
    "test123",
    {"name": "brodie"}
)

print(
    session_service.get_state(
        "test123"
    )
)'''