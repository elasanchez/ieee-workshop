import requests
BASE = 'https://api.twilio.com/'
VERSION = '2010-04-01/'
ACCOUNT_SID  = 'AC4cda62b27eb2fcc8ea1ec84b809aedb5'
TOKEN = '289832b1d5f4efbd65bd09be354d93d7'
NUMBER = '+19097643562]'


def sendMessage(to_number, body):
	ENDPOINT = API +'/Accounts/' + ACCOUNT_SID + '/Messages.json'
	payload = (
		'From' : NUMBER,
		'To' : to_number,
		'Body' : body
	)
	
	r = requests.post(ENDPOINT, data = payload, auth = (ACCOUNT_SID, TOKEN))
	print(r)
	
sendMessage('insert my number here', 'Hello from workshop')