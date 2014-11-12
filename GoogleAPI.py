##Google Developer Console API
    ##Only Authorized for IP: 69.178.171.20
##     AIzaSyCSi_Hw8fGUO974rR-hgGleyPcK2SzCrYc


#$ pip install -U google-api-python-client

from urllib2 import Request, urlopen, URLError

request = Request('http://placekitten.com/')

try:
	response = urlopen(request)
	kittens = response.read()
	print kittens[559:1000]
except URLError, e:
    print 'No kittez. Got an error code:', e