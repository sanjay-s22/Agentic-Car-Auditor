from services.market_service import get_market_data
from config.constants import Market_analyzed

def market_node(state):
    vehicle_data = state.get('vehicle_data')
    if not vehicle_data:
       raise ValueError('vehicle_data missing from state')
    
    vehicle_data = state['vehicle_data']
    market_data = get_market_data(
        brand = vehicle_data['brand'],
        model = vehicle_data['model'],
        year = vehicle_data['year'],
        city = vehicle_data['city']
    )

    state['market_data'] = market_data
    state['status'] = Market_analyzed
    return state 