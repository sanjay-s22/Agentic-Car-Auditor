from pydantic import BaseModel
from typing import Any

class AuditResponse(BaseModel):
    session_id: str
    status: str
    data: Any