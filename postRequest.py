import requests

r = requests.post("https://89tuws2rg3.execute-api.eu-west-2.amazonaws.com/Test/search",auth=("user","pass"), data={"searchQuery" : "black dress"})
r = r.json()

print(r)
