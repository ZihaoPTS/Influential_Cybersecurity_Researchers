import json

def finding_citation_count(publications):
    count = 0	
    with open('data/topnotch.json',encoding='utf-8') as filehandle:
        topnotch = json.load(filehandle)
    for i in publications:
        for j in topnotch:
            if (i['name'] in j['title']) or (j['title'] in i['name']):
                if(j['max_cites'] > 0):
                    i['citation'] = j['max_cites']
                break