import requests
import json
BASE_URL = 'https://api.github.com'
Link_URL = 'https://gist.github.com'
username = 'inc0gn1to'
api_token = ''
#gist_id = ''
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
