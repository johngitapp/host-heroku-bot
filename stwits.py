from apscheduler.scheduler import Scheduler
import requests
import os

clientID = os.environ["clientID"]
clientSecret = os.environ["clientSecret"]
redirectURI = os.environ["defaultURI"]

def getAtoken(cID,cSec,rURI):
	# Get Access Token
	auth = request.args.get('code', None)
	tokenUrl = 'https://api.stocktwits.com/api/2/oauth/token?client_id='+cID+'&client_secret='+cSec+'&code='+str(auth)+'&grant_type=authorization_code&redirect_uri='+rURI
	resp = requests.post(url=tokenUrl)
	data = resp.text
	translate = json.loads(data)
	access = translate["access_token"]
	return access


def createPost(aTok,bMessage,cMessage):
	# Create Post To Stocktwits
	url = 'https://api.stocktwits.com/api/2/messages/create.json?access_token='+aTok
	send_json = {'body': str(bMessage),'chart':str(cMessage)}
	resp = requests.post(url=url,json=send_json)
	return resp


def controls(messageKey,imageKey):
	# Relevant Function Location For Scheduler
	messageDiction = {}
	imageDiction = {}

	aToken = getAtoken(clientID,clientSecret,redirectURI)

	response = createPost(aToken,messageDiction[str(messageKey)],imageDiction[str(imageKey)])

	if response.status_code == 200:
		print ("Post Sent")
	else:
		print ("Post Halted",response.status_code)


sched = Scheduler(standalone=True)

sched.add_cron_job(controls, day_of_week='mon-fri', hour= 0, minute=1, args=("Company Reports 2022 Earnings","earnings.jpg",))

sched.start()