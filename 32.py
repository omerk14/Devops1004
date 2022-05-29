import requests

response = requests.post("http://localhost:5001/name")
expected = "save new car"
assert expected == "save new car1"