import requests
import json
BASE_URL = 'https://api.github.com'
Link_URL = 'https://gist.github.com'
username = 'inc0gn1to'
api_token = 'e9bef6b907d5c1ca7cb78057d05fae65e66a26b7'
#gist_id = '25f423e80f0ff85b9a82b07296540652'
header = { 'X-Github-Username': '%s' % username,
'Content-Type': 'application/json',
'Authorization': 'token %s' % api_token,
}
url = '/users/%s/gists' % username #"/gists/%s" % gist_id
r = requests.get('%s%s' % (BASE_URL, url), headers=header,)
#print r.json()

gists = r.json()
for gist in gists:
    data = gist['files'].values()[0]
    print data['filename'], data['raw_url'], data['language']
