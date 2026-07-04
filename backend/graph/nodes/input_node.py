import json 
from config.llm import llm
from prompts.extraction_prompt import ExtractionPrompt

def input_node(state):
    try:    
        print('before prompt')
        prompt = ExtractionPrompt.format(user_input = state['user_input'])
        print('after')
        response = llm.invoke(prompt)
        print("\nLLM OUTPUT:")
        print(response.content)
        vehicle_data = json.loads(response.content)
        state['vehicle_data'] = vehicle_data
        state['status'] = 'Processing'

    except Exception as e:
        print('Error:', e)
        state['vehicle_data'] = {}
        state['status'] = 'Extraction_Failed'
    
    return state 