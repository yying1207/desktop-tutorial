import requests
import os
import json
from github import Github

# Method 1: Using requests library to interact with GitHub API
token = os.environ.get("GITHUB_TOKEN") # 'export GITHUB_TOKEN=abc123' in terminal before running the script

repo_name = input("Please enter the repo name you want to chreate: ")
GITHUB_API_URL = "https://api.github.com"
headers = { "Authorization": f"token {token}" }
data = {"name": f"{repo_name}"}

# Create a repo
r = requests.post(f"{GITHUB_API_URL}/user/repos", headers=headers, data=json.dumps(data))   
print(r)



# Delete a repo
username = input("Please enter your GitHub username: ")
r = requests.delete(f"{GITHUB_API_URL}/repos/{username}/{repo_name}", headers=headers)
print(r)



# List repo
data = {"type": "all", "sort": "full_name", "direction": "asc"}
username = input("Please enter your GitHub username: ")
output = requests.get(f"{GITHUB_API_URL}/users/{username}/repos", data=json.dumps(data))
output = json.loads(output.text)

for repo_name in output:
    print(repo_name["name"])



# Method 2: Using PyGithub library
access_token = os.environ.get("GITHUB_TOKEN") # 'export GITHUB_TOKEN=abc123' in terminal before running the script
#using an access token
g = Github(access_token)
for repo in g.get_user().get_repos():
    print(repo.name)
    