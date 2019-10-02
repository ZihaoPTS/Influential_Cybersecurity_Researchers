from bs4 import BeautifulSoup
import requests
import re

def GetLink(url,AllLink):
	tried = 0
	while tried < 3:
		try:
			r = requests.get(url)
			break
		except:
			print("Request " + url + " failed. Try again.")
			tried = tried + 1
	if tried >= 3:
		print("Request " + url + " failed. for three time, skiped")
		return
	soup = BeautifulSoup(r.content, 'html.parser')
	data = soup.findAll( "a", {"class": "toc-link"} )
	conference_list = ['sp','uss','ccs','ndss','acsac','raid','esorics']
	AllLink[url] = []
	cf = ""
	for c in conference_list:
		if c in url:
			cf = c
			break
	 
	for i in data:
		if re.findall(cf + '(\d{4})', i['href']) != []:
			AllLink[url].append( i['href'] )