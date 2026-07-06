def validation_router(state):
    if state['missing_fields'] :
        return 'missing_information'
    return 'validated'