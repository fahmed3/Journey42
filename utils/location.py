import requests

response = requests.get("http://api.tripadvisor.com/api/partner/2.0/map/42.33141,-71.099396?key=4C0D0AC5DE094004AFE1F10B5927498E").json()
print(response['data'][0].keys())
