import re
import time
from datetime import datetime, timedelta
from pytz import timezone
import pytz
from enviar import enviarEmail
from bs4 import BeautifulSoup
from urllib2 import urlopen

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

brazilTime= timezone('Brazil/East')
usTimeZone = timezone('US/Eastern')
usTime = usTimeZone.localize(datetime(currentDates[2], dates[0], dates[1], dates[2], dates[3]))

printFormat = '%d/%m/%Y %H:%M'

if(currentDates[1] + 1 == dates[1]):
	enviarEmail('', 'TopCoder SRM Amanha!  ' + usTime.astimezone(brazilTime).strftime(printFormat) )
elif(currentDates[1] == dates[1]):
	enviarEmail('', 'TopCoder SRM Hoje!' + usTime.astimezone(brazilTime).strftime(printFormat) )
