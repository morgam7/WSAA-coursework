
from config import config
import requests
import base64

# apikey is in config.py
apikey = config["githubkey"]

url = "https://api.github.com/repos/morgam7/WSAA-coursework/contents/Andrew.txt"

# Get the file data from GitHub
response = requests.get(url, auth=("token", apikey))
data = response.json()

# The file content is returned in base64, so decode it to normal text
content = base64.b64decode(data["content"]).decode("utf-8")

# Replace multiple words in the file text
replacements = {"Andrew": "Marcella", "teach": "learn"}
for old, new in replacements.items():
    content = content.replace(old, new)

# Prepare the updated file data for GitHub
# The new content must be encoded back into base64
update_data = {
    "message": "Replace Andrew with my name",
    "content": base64.b64encode(content.encode("utf-8")).decode("utf-8"),
    "sha": data["sha"]
}

# Send the updated file back to GitHub and create the commit
response = requests.put(url, auth=("token", apikey), json=update_data)


print(response.status_code)



# https://www.geeksforgeeks.org/python/python-replace-multiple-characters-at-once/
# https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
# https://docs.python.org/3/library/base64.html
# https://docs.github.com/en/rest/repos/contents?apiVersion=2026-03-10