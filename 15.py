# def get_age()
#     age = int(input("ënter first number: "))
#     if age < 0:
#         raise ValueError("age cannot be negative")

# try:
#     get_age()
# except ValueError as e:
#     print(e.args)

import requests
try:
    requests.get("https://gghhff")
except requests.exceptions.MissingSchema:
    print("nissing schema in  url")
except requests.exceptions.InvalidURL:
    print("invalid url")
except requests.exceptions.ConnectionError:
    print("connection error")