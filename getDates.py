import re
import time
from bs4 import BeautifulSoup
from urllib2 import urlopen
soup = BeautifulSoup(urlopen('http://community.topcoder.com/tc'))
prizes = soup.find_all(attrs = {'class':'prizes'})

unformDate = prizes[-1]
dates = unformDate.string.split()

stringCurrentDates = time.strftime('%b %d')
currentDates = stringCurrentDates.split()

print(currentDates)
