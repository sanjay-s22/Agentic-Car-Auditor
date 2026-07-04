from graph.state import AuditState 
ExtractionPrompt ='''
you are a vehicle information extraction system.
Extract vehicle details from the user input.
Return only valid JSON.

Do not include explanations.
Do not include markdown.
Do not include code blocks.

Extract the following fields:

{{
    'brand' : null,
    'model' : null,
    'year' : null,
    'fuel_type' : null,
    'km_driven' : null,
    'owner' : null,
    'city' : null,
}}

Rules:
Year must be an integer 
km_driven must be integer
missing values should be null 
return only JSON

User Input :
{user_input}

'''