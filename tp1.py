import requests

search = input("Recherche: ")


url = f"https://data.economie.gouv.fr/api/records/1.0/search/?dataset=rappelconso0&q={search}"


response = requests.get(url)

responseJson = response.json()


for data in responseJson["records"]:
    print("Conduites a tenir par le consommateur :", data.get("fields").get("conduites_a_tenir_par_le_consommateur"))
    print("Motif du rappel :", data.get("fields").get("motif_du_rappel"))
    print("Numero de contact :", data.get("fields").get("numero_de_contact"))
    print("Nom de la marque du produit :", data.get("fields").get("nom_de_la_marque_du_produit"))
    print("Risques encourus par le consommateur :", data.get("fields").get("risques_encourus_par_le_consommateur"), "\n")
    print("----------------------------------------------------")
    