from pydantic import BaseModel 

class AuditRequest(BaseModel):
    raw_input : str
    vehicle_data : dict 

class ContinueAuditRequest(BaseModel):
    session_id: str
    updates: dict