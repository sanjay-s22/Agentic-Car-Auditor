from pydantic import BaseModel

class AuditRequest(BaseModel):
    user_input: str

class ResumeRequest(BaseModel):
    owner: str
    city: str