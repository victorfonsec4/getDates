import re
import time
from enviar import enviarEmail
from bs4 import BeautifulSoup
from urllib2 import urlopen
soup = BeautifulSoup(urlopen('http://community.topcoder.com/tc'))
prizes = soup.find_all(attrs = {'class':'prizes'})

unformDate = prizes[-1]
unformDate.string = unformDate.string.replace(',', '')
dates = unformDate.string.split()

stringCurrentDates = time.strftime('%b %d')
currentDates = stringCurrentDates.split()

if(int(currentDates[1]) + 1 == int(dates[1])):
	enviarEmail('', True)
elif(int(currentDates[1]) == int(dates[1])):
	enviarEmail('', False)
