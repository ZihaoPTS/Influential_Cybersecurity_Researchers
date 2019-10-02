from module.layer_1 import GetLink
from module.layer_2 import update_db
from module.finding_citation_count import finding_citation_count
from module.strip_latin import strip_latin
from module.consolidating_author import consolidating_author
from module.specific_consolidation import specific_consolidation
from module.truncate import truncate
from module.prepare_web_json import prepare_web_json
from module.use_aff import use_aff
from module.use_gs import use_gs
from module.web_table_jq import web_generation
import json

from bs4 import BeautifulSoup
import requests
import re

def main():
    t4 = ['SP','USS','CCS','NDSS']
    t2 = ['ACSAC','RAID','ESORICS']
    pub = 0
    p_a = {'SP':0,'USS':0,'CCS':0,'NDSS':0}
    p_a_2 = {'SP':0,'USS':0,'CCS':0,'NDSS':0}
    p_2 = 0
    with open('data/topnotch.json',encoding='utf-8') as filehandle:
        topnotch = json.load(filehandle)
    with open('data_collected/publications.json',encoding='utf-8') as filehandle:
        publications = json.load(filehandle)
    """
    for i in topnotch:
        if "Giovanni Vigna" in i["authors"]:
            found = False
            for j in publications:
                if (i['title'] in j['name']) or (j['name'] in i['title']):
                    found = True
                    break
            if not found:
                print(i["conference"] + str(i["year"]) + " : " + i["title"])
    """
    for i in publications:
        if "Giovanni Vigna" in i["author"]:
            for j in t4:     
                if j.lower() in i["conference"]:
                    pub = pub + 1
                    p_a[j] = p_a[j] + 1
                    break
    for i in topnotch:
        if "Giovanni Vigna" in i["authors"]:
            for j in t4:     
                if j in i["conference"]:
                    p_2 = p_2 + 1
                    p_a_2[j] = p_a_2[j] + 1
                    break
    print(pub)
    print(p_a)
    print(p_2)
    print(p_a_2)
if __name__ == "__main__" :
	main()