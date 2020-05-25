def normalize_data(data):
    return {k: v for k, v in data.items() if v is not None}
