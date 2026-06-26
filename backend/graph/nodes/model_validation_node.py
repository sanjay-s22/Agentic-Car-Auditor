from graph.state import AuditState


required_model_features = [
    "km_driven",
    "mileage",
    "engine",
    "max_power",
    "seats",
    "car_age",
    "fuel",
    "seller_type",
    "transmission",
    "owner",
    "brand",
    "model_family"
]


def model_validation_node(state: AuditState):

    model_input = state["model_input"]

    missing = [
        field
        for field in required_model_features
        if field not in model_input
    ]

    state["missing_model_features"] = missing

    state['model_validation_passed'] = (len(missing) == 0)

    return state