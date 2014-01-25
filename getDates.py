import re
import socket
import time
from datetime import datetime, timedelta
from pytz import timezone
import pytz
from enviar import enviarEmail
from bs4 import BeautifulSoup
from urllib2 import urlopen

def TopCoder():
	soup = BeautifulSoup(urlopen('http://community.topcoder.com/tc'))
	prizes = soup.find_all(attrs = {'class':'prizes'})

	unformDate = prizes[-1]
	unformDate.string = unformDate.string.replace(',', '')
	unformDate.string = unformDate.string.replace(':', ' ')
	dates = unformDate.string.split()

	stringCurrentDates = time.strftime('%b %d %Y')
	currentDates = stringCurrentDates.split()

	dates[0] = time.strptime(dates[0], "%b").tm_mon
	dates[1] = int(dates[1])
	dates[2] = int(dates[2])
	dates[3] = int(dates[3])

	currentDates[0] = time.strptime(currentDates[0], "%b").tm_mon
	currentDates[1] = int(currentDates[1])
	currentDates[2] = int(currentDates[2])

	brazilTimeZone= timezone('Brazil/East')
	usTimeZone = timezone('US/Eastern')
	usTime = usTimeZone.localize(datetime(currentDates[2], dates[0], dates[1], dates[2], dates[3]))

	printFormat = '%d/%m/%Y %H:%M'
	brazilTimeStr = usTime.astimezone(brazilTimeZone).strftime(printFormat)


	if(currentDates[1] + 1 == dates[1]):
		enviarEmail('', 'TopCoder SRM Amanha!  ' +  brazilTimeStr)
	elif(currentDates[1] == dates[1]):
		enviarEmail('', 'TopCoder SRM Hoje!' + brazilTimeStr)
	else:
		print('ainda faltam ' + str((dates[1] - currentDates[1])) + ' dias para o TopCoder')
def CodeForces():
	socket.setdefaulttimeout(3)
	soup = BeautifulSoup(urlopen('http://codeforces.com/contests'))
	stringDate = soup.find_all(href=re.compile('worldclock'))[0].string

	stringDate = stringDate.replace('/', ' ')
	stringDate = stringDate.replace(':', ' ')
	stringDate = stringDate.replace('AM', '')
	stringDate = stringDate.replace('PM', '')
	date = stringDate.split()
	
	date[0] = int(date[0]);
	date[1] = int(date[1]);
	date[2] = int(date[2]);
	date[3] = int(date[3]);
	date[4] = int(date[4]);
	
	stringCurrentDates = time.strftime('%b %d %Y')
	currentDates = stringCurrentDates.split()
	currentDates[0] = time.strptime(currentDates[0], "%b").tm_mon
	currentDates[1] = int(currentDates[1])
	currentDates[2] = int(currentDates[2])

	brazilTimeZone = timezone('Brazil/East')
	russianTimeZone = timezone('Europe/Moscow')
	russianTime = russianTimeZone.localize(datetime(date[2], date[0], date[1], date[3], date[4]))

	printFormat = '%d/%m/%Y %H:%M'
	brazilTimeStr = russianTime.astimezone(brazilTimeZone).strftime(printFormat)
	

	if(currentDates[1] + 1 == date[1]):
		enviarEmail('', 'CodeForces Match Amanha!  ' +  brazilTimeStr)
	elif(currentDates[1] == date[1]):
		enviarEmail('', 'CodeForces Mattch Hoje!' + brazilTimeStr)
	else:
		print('ainda faltam ' + str((date[1] - currentDates[1])) + ' dias para o CodeForces')

TopCoder()
CodeForces()
