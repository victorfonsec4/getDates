from bs4 import BeautifulSoup
from urllib2 import urlopen
soup = BeautifulSoup(urlopen('http://community.topcoder.com/tc?module=MatchDetails&rd=15839'))

print(soup.prettify())
