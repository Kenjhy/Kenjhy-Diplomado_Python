import requests

#url = "https://api.thingspeak.com/update?api_key=RXKYA9KE91OV2POU"
url = "https://api.thingspeak.com/update?api_key=A0TMNR155FXX6TC5"

#response = requests.request("GET", url, headers=None, params="&field1= 40" + "&field1= 25" )
response = requests.request("GET", url, headers=None, params= "&field1= 6" + "&field2= 200" )

print(response.status_code)