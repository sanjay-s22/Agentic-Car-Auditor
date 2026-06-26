from uuid import uuid4
from graph.workflow import graph
'''
initial_state = {
    'session_id' : str(uuid4()),
    'raw_input' : '2020 Hyundai i20 Petrol 55k km',
    'vehicle_data' : {
        'brand' : 'Hyundai',
        'model' : 'i20',
        'year' : 2020,
        'fuel' : 'petrol',
        'kms_driven' : 55000
    },

    'missing_fields' : [],
    'validation_passed' : False,
    'status' : 'Processing',
}

result = graph.invoke(initial_state)
print(result)'''

from fastapi import FastAPI
from routes.audit import router as audit_router

app = FastAPI(title = 'Agentic Car Auditor')

app.include_router(audit_router)
