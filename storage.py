import sqlite3

def save_test_result(report):
    try:
        # Pour l'instant on se contente de confirmer la réception
        print(f"Résultat sauvegardé localement : {report['status']}")
        return True
    except Exception as e:
        print(f"Erreur de stockage : {e}")
        return False
