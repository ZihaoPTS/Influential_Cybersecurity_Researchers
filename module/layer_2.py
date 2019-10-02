from bs4 import BeautifulSoup
import json
import requests
import re

'''
in main loop, a data base for "publication" will be created and we will 
record index instead of the full name index will be used to keep tab
'''

def update_db_core(t,publications,authors,year,conference):
    temp_author = []
    pub = t.find("span",{"class":"title"})
    name = pub.text
    data_parsed = t.findAll("span",{"itemprop":"author"})
    index = len(publications)
    for author_token in data_parsed:
        author = author_token.text
        temp_author.append(author)
        if author in authors:
            authors[author].append(index)
        else:
            authors[author] = [index]
    publications.append({"name":name,"citation":-1,'conference':conference,"author":temp_author,"year":year})

def update_db(URL,authors,publications,cf,website):
    conference = ''
    conference_list = ['sp','uss','ccs','ndss','acsac','raid','esorics']
    ignore_list = ["poster","tutorial","demo","workshop","keynote","panel","demonstration","forum"]
    for c in conference_list:
        if c in cf:
            conference = c
            break
    year = re.findall('(\d{4})', URL)[0]

    if URL in website:
        return
    else:
        tried = 0
        while tried < 3:
            try:
                r = requests.get(URL)
                break
            except:
                print("Request " + URL + " failed. Try again.")
                tried = tried + 1
        if tried >= 3:
            print("Request " + URL + " failed. for three time, skiped")
            return
        website[URL] = str(r.content)
    
    soup = BeautifulSoup(r.content, 'html.parser')
    tokens = soup.findAll('h2')
    if tokens == []:
        datas = soup.findAll("article", {"class": "data"})[1:]
        for i in datas:
            update_db_core(i,publications,authors,year,conference)
        return
    headers = []
    is_pub = True
    for token in tokens:
        temp = token.findNext("article", {"class": "data"})
        headers.append([token,temp])
    for k,header in enumerate(headers[:-1]):
        is_pub = True
        for ig in ignore_list:
            if ig in header[0].text.lower():
                is_pub = False
                break
        if not is_pub:
            continue
        token = header[1]
        while token != headers[k+1][1]:
            update_db_core(token,publications,authors,year,conference)
            token = token.findNext("article", {"class": "data"})
    for ig in ignore_list:
        if ig in headers[-1][0].text.lower():
            is_pub = False
            break
    if is_pub:
        token = headers[-1][0].findAllNext("article", {"class": "data"})
        for t in token:
            update_db_core(t,publications,authors,year,conference)