from typing import TypedDict 



class AuditState(TypedDict):
    session_id : str
    raw_input : str 
    vehicle_data : dict  
    missing_fields : list[str]
    validation_passed : bool 
    status : str 
    enriched_features: dict
    ml_price : float | None 
    model_input : dict 
    missing_model_features: list[str]
    model_validation_passed : bool 
