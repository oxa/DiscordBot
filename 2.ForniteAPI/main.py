import requests
import os
from dotenv import load_dotenv

load_dotenv()

FORTNITE_TOKEN = os.getenv('FORTNITE_TOKEN')

username = "MrKaime"

url = "https://fortnite-api.com/v2/stats/br/v2?name={}".format(username)

payload={}
headers = {
    'Authorization': FORTNITE_TOKEN
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.json()

print(data)
