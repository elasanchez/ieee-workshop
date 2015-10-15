import requests
BASE = 'https://api.twilio.com/'
VERSION = '2010-04-01/'
ACCOUNT_SID  = '[INSERT ACCOUNT SIDE HERE]'
TOKEN = '[AUTH TOKEN HERE]'
NUMBER = '[+1 ..INSERT NUMBER HERE]'


def sendMessage(to_number, body):
	ENDPOINT = API +'/Accounts/' + ACCOUNT_SID + '/Messages.json'
	payload = (
		'From' : NUMBER,
		'To' : to_number,
		'Body' : body
	)
	
	r = requests.post(ENDPOINT, data = payload, auth = (ACCOUNT_SID, TOKEN))
	print(r)
	
sendMessage('insert my number here', 'Hello from worksho')