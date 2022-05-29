import  requests
import json
response = requests.get("https://api.github.com/users/avielb/repos")
# print(response.json())
repo_list = response.json()
print(repo_list[0].keys)
for repo in repo_list:
    print(repo["name"])
