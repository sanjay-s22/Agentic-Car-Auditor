from typing import TypedDict 

class AuditState(TypedDict):
    session_id : str 
    user_input : str
    vehicle_data : dict[str, any]
    missing_fields : list[str]
    market_data : dict[str, any]
    risk_data : dict[str, any]
    negotiation_data : dict[str, any]
    decision_data : dict[str, any]
    report : dict[str, any]
    critic_data : dict 
    cofidence : int 
    status : str 
    followup_data : dict 

    
