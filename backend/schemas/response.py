from pydantic import BaseModel 

class AuditResponse(BaseModel):
    session_id : str
    status : str
    missing_fields : list[str]
    
