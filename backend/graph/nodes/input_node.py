import json 
from config.llm import llm
from prompts.extraction_prompt import ExtractionPrompt
from config.constants import(Processing, Extraction_failed)

def input_node(state):
    try:    
        prompt = ExtractionPrompt.format(user_input = state['user_input'])
        response = llm.invoke(prompt)
        print(response.content)
        vehicle_data = json.loads(response.content)
        state['vehicle_data'] = vehicle_data
        state['status'] = Processing 

    except Exception as e:
        print(f'Input Node Error: {e}')
        state['vehicle_data'] = {}
        state['status'] = Extraction_failed
    
    return state 