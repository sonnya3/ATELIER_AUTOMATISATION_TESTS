# API Choice

- Étudiant : sonnya
- API choisie : Agify.io
- URL base : https://api.agify.io
- Documentation officielle / README :agify.io
- Auth : None / API Key / OAuth
- Endpoints testés : 
  - GET ... name=michael
  - GET ...
- Hypothèses de contrat (champs attendus, types, codes) : Code HTTP 200 attendu pour chaque requête valide.
Le JSON doit obligatoirement contenir les clés name (String), age (Number/Null) et count (Number).
- Limites / rate limiting connu :Limité à 1000 requêtes par jour pour les utilisateurs gratuits (basé sur l'IP).
- Risques (instabilité, downtime, CORS, etc.) :Le champ age peut être null si l'API n'a pas assez de données pour un prénom, ce qui peut casser une application qui attend strictement un chiffre.
