def validate_contract(data):
    """Vérifie si les clés JSON attendues sont présentes"""
    required_keys = ["name", "age", "count"]
    return all(key in data for key in required_keys)

def check_status_code(response):
    return response.status_code == 200
