'''
from fastapi import APIRouter
from uuid import uuid4

from langchain_core.runnables import router
from schemas.request import AuditRequest, ResumeRequest
from graph.workflow import graph
from services.resume_service import resume_session

router = APIRouter(tags=["Car Auditor"])

@router.post("/audit")
def audit_car(request: AuditRequest):

    initial_state = {
        "session_id": str(uuid4()),
        "user_input": request.user_input,
        "vehicle_data": {},
        "missing_fields": [],
        "market_data": {},
        "risk_data": {},
        "negotiation_data": {},
        "decision_data": {},
        "report": {},
        "critic_data": {},
        "status": "STARTED",
        "followup_data": {}
    }

    result = graph.invoke(initial_state)
    return result

@router.post("/resume/{session_id}")
def resume_workflow(
    session_id: str,
    request: ResumeRequest):

    result = resume_session(
        session_id=session_id,
        followup_data={
            "owner": request.owner,
            "city": request.city
        }
    )

    return result
    '''


from fastapi import APIRouter
from uuid import uuid4

from schemas.request import AuditRequest, ResumeRequest
from graph.workflow import graph
from services.resume_service import resume_session

router = APIRouter(tags=["Car Auditor"])


@router.post("/audit")
def audit_car(request: AuditRequest):

    initial_state = {
        "session_id": str(uuid4()),
        "user_input": request.user_input,
        "vehicle_data": {},
        "missing_fields": [],
        "market_data": {},
        "risk_data": {},
        "negotiation_data": {},
        "decision_data": {},
        "report": {},
        "critic_data": {},
        "status": "STARTED",
        "followup_data": {}
    }

    result = graph.invoke(initial_state)
    return result


@router.post("/resume/{session_id}")
def resume_workflow(
    session_id: str,
    request: ResumeRequest
):

    result = resume_session(
        session_id=session_id,
        followup_data=request.model_dump(exclude_none=True)
    )

    return result