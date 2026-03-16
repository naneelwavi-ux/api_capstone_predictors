# test_corrige.py
import requests
import json

url = "http://127.0.0.1:5000/api/predict"

test_data = {
   "surface_m2": 120,
    "nb_chambres": 3,
    "nb_salons": 1,
    "nb_sdb": 2,
    "quartier_encoded": 3612504.347826087,
    "latitude": 18.10,
    "longitude": -15.96,
    "dist_centre_ville_km": 0.0035805905757335,
    "dist_aeroport_km": 1.7708127278455823,
    "dist_plage_km": 6.797640291921312,
    "nb_ecoles_1km": 6,
    "nb_mosquees_1km": 3,
    "nb_commerce_1km": 60,
    "nb_hopitaux_1km": 5,
    "nb_total_pois_1km": 74,
    "nb_pieces_total": 4,
    "has_garage": 0,
    "has_jardin": 0,
    "has_piscine": 0,
    "has_balcon": 1,
    "has_meuble": 1,
    "has_titre_foncier": 1,
    "est_neuf": 0,
    "age_annonce": 3
   }

response = requests.post(url, json=test_data)
result = response.json()

print(json.dumps(result, indent=2))