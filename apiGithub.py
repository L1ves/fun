import requests
import json
BASE_URL = 'https://api.github.com'
Link_URL = 'https://gist.github.com'
username = 'inc0gn1to' ## Fill in your github username
api_token = 'e9bef6b907d5c1ca7cb78057d05fae65e66a26b7' ## Fill in your token
header = { 'X-Github-Username': '%s' % username,
'Content-Type': 'application/json',
'Authorization': 'token %s' % api_token,
}
url = "/gists"
data ={ "description": "the description for this gist",
"public": True,
"files": {
"file1.txt": {
"content": "String file contents"
  }
 }
}
r = requests.post('%s%s' % (BASE_URL, url),headers=header,data=json.dumps(data))
print r.json()['url']
