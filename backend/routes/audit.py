from uuid import uuid4 
from fastapi import APIRouter 
from schemas.request import AuditRequest 
from graph.workflow import graph
from services.session_store import save_session 
from schemas.request import ContinueAuditRequest
from services.session_store import get_session

router = APIRouter()

@router.post('/audit')
def audit_vehicle(request : AuditRequest):
    state = {
        'session_id' : str(uuid4()),
        'raw_input' : request.raw_input,
        'vehicle_data' : request.vehicle_data,
        'missing_field' : [],
        'validation_passed' : False,
        'status' : 'Processing',
    }

    result = graph.invoke(state) 

    save_session(
        result['session_id'],
        result 
    )

    return result

@router.post("/audit/continue")
def continue_audit(request: ContinueAuditRequest):

    state = get_session(request.session_id)

    if not state:
        return {
            "error": "Session not found"
        }

    state["vehicle_data"].update(
        request.updates
    )

    result = graph.invoke(state)

    save_session(
        result["session_id"],
        result
    )

    return result