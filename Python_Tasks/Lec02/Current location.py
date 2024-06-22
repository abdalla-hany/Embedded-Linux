# print your current location

import requests
from pprint import pprint

url = requests.get("https://api.ipify.org/?format=json")
json = dict(url.json())
ip = str(json.get("ip"))

url = requests.get(f"https://ipinfo.io/{ip}/geo")
pprint(url.json())
