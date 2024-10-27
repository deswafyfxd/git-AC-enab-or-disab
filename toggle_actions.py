import requests
import os
import sys

# Replace with your token, owner, and repo
token = os.getenv('MY_GITHUB_TOKEN')
owner = os.getenv('OWNER')
repo = os.getenv('REPO')

# Headers for authentication
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
}

def set_actions_status(enabled):
    url = f'https://api.github.com/repos/{owner}/{repo}/actions/permissions'
    data = {
        'enabled': enabled
    }
    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f'Actions {"enabled" if enabled else "disabled"} successfully.')
    else:
        print(f'Failed to set actions status: {response.status_code}, {response.text}')

if len(sys.argv) != 2:
    print("Usage: python toggle_actions.py <enable|disable>")
    sys.exit(1)

action = sys.argv[1].lower()
if action == "enable":
    set_actions_status(True)
elif action == "disable":
    set_actions_status(False)
else:
    print("Invalid argument. Use 'enable' or 'disable'.")
    sys.exit(1)
