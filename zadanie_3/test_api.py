"""
API ktore wybrałem:
    https://github.com/cyberboysumanjay/Inshorts-News-API
Live endpoint: https://inshortsapi.vercel.app/news?category=science
"""

import requests
import json

country_cases = 'poland'
url = f"https://inshortsapi.vercel.app/news?category={country_cases}"
head = {'content-type': 'application/json'}
response = requests.request("GET", url)
a = json.loads(response.text)
country = None
success = None

# -----------------------------------
# sprawdzanie kluczy
expected = ['category', 'data', 'success']
current = []

for key in a.keys():
    if key in expected:
        current.append(key)
assert expected == current

# -----------------------------------
# sprawdzanie wartosci w kluczu category i success
for k, v in a.items():
    if k == 'category':
        country = v
    if k == 'success':
        success = v

assert country_cases == country
assert success is True

# -----------------------------------
# sprawdzanie odpowiedzi
assert response.status_code == 200

# -----------------------------------
# sprawdzanie niepoprawnego zapytania
url = f"https://inshortsapi.vercel.app/1?category1={country_cases}"  # zmiana endpointu z `news` na `1`
response = requests.request("GET", url)
assert response.status_code == 404
