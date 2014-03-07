import re
import socket
import time
from datetime import datetime, timedelta, date
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

	dates[0] = time.strptime(dates[0], "%b").tm_mon
	dates[1] = int(dates[1])
	dates[2] = int(dates[2])
	dates[3] = int(dates[3])
	dates.insert(0, date.today().year)

	usTimeZone = timezone('US/Eastern')

	MontarEnviar('TopCoder', usTimeZone, dates)

def CodeForces():
	soup = BeautifulSoup(urlopen('http://codeforces.com/contests'))
	stringDate = soup.find_all(href=re.compile('worldclock'))[0].string
	pm = stringDate.find('PM')
	stringDate = stringDate.replace('/', ' ')
	stringDate = stringDate.replace(':', ' ')
	stringDate = stringDate.replace('AM', '')
	stringDate = stringDate.replace('PM', '')
	date = stringDate.split()
	date = [int(x) for x in date]

	date[0], date[2] = date[2], date[0]
	date[1], date[2] = date[2], date[1]
	if(pm != -1):
		date[3] = date[3] + 12
	russianTimeZone = timezone('Europe/Moscow')

	MontarEnviar('CodeForces', russianTimeZone, date)

def CodeChef():
	soup = BeautifulSoup(urlopen('http://www.codechef.com/contests?sort_by=START&sorting_order=asc'))
	timeList = soup.find_all(text=re.compile('\d{4}\-\d{2}\-\d{2}'))[0]
	timeList = timeList.replace('-', ' ')
	timeList = timeList.replace(':', ' ')
	timeList = timeList.split()
	timeList = [int(x) for x in timeList]

	indianTimeZone = timezone('Asia/Calcutta')

	MontarEnviar('CodeChef', indianTimeZone, timeList)

def MontarEnviar(competition, zone, dateList):
	currentDate = date.today().strftime('%Y %m %d')
	currentDate = currentDate.split()
	currentDate = [int(x) for x in currentDate]

	brazilTimeZone = timezone('Brazil/East')
	time = zone.localize(datetime(dateList[0], dateList[1], dateList[2], dateList[3], dateList[4]))

	printFormat = '%d/%m/%Y %H:%M'
	brazilTimeStr = time.astimezone(brazilTimeZone).strftime(printFormat)

	delta = date(dateList[0], dateList[1],dateList[2]) - date(currentDate[0], currentDate[1],currentDate[2])

	if(delta.days == 0):
		enviarEmail('', competition + ' Match Hoje! ' + brazilTimeStr)
	elif(delta.days == 1):
		enviarEmail('', competition + ' Match Amanha! ' + brazilTimeStr)
	else:
		print('Ainda faltam ' + str(delta.days) + ' dias para o ' + competition)

socket.setdefaulttimeout(12)
TopCoder()
CodeForces()
CodeChef()
