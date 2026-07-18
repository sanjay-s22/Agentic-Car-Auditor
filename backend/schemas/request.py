from pydantic import BaseModel

class AuditRequest(BaseModel):
    user_input: str

class ResumeRequest(BaseModel):
    brand: str | None = None
    model: str | None = None
    year: int | None = None
    fuel_type: str | None = None
    km_driven: int | None = None
    owner: str | None = None
    city: str | None = None