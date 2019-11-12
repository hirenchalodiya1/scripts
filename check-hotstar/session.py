import requests

response = requests.get("https://api.hotstar.com/in/antares/v2/chromecast/in/entitlement/content/1260013004/?timeStamp=1572441438096", cookies={})
print(response.json())