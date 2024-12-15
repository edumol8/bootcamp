import requests

urls = "https://dragonball-api.com/api/characters/1"
headers = {
    "Accept": "application/json",
    "content-type": "application/json"
}

#Realizar una peticion tipo get con los encabezados
response = requests.get(urls, headers=headers)

if response.status_code == 200:
    data= response.json()
    print(f"Nombre: {data["name"]}")
    print(f"Ki: {data["ki"]}")

else:
    print(f"Error en la app: {response.status_code}")