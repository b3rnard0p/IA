import requests

url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
resp = requests.get(url)
resp.raise_for_status()

with open("brazil-states.geojson", "wb") as f:
    f.write(resp.content)

print("Arquivo salvo como brazil-states.geojson")
