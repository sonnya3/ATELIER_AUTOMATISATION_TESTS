from tester.client import call_agify
from tester.tests import validate_contract, check_status_code

def run_all_tests():
    response, latency = call_agify()
    
    report = {
        "status": "ÉCHEC ❌",
        "latency": latency,
        "contract": "INVALIDE ❌",
        "code": "N/A",
        "age_found": "N/A"
    }

    if response:
        report["code"] = response.status_code
        if check_status_code(response):
            data = response.json()
            report["age_found"] = data.get("age")
            if validate_contract(data):
                report["contract"] = "VALIDE ✅"
                report["status"] = "OPÉRATIONNEL ✅"
    
    return report
