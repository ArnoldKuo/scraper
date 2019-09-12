import sys
import requests
lan = sys.argv[1]
text = sys.argv[2]
url = 'https://'+lan+'.wikipedia.org/w/api.php'

response = requests.get(
	url,
	params = {
		'action': 'query',
		'format': 'json',
		'titles': text,
		'prop': 'extracts',
		'exintro': True,
		'explaintext': True,
	}
).json()

page = next(iter(response['query']['pages'].values()))
extract = page['extract']
abstract = extract.split('. ')
print(abstract[0])
