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
from module.web_table_jq_wo_5 import web_generation_wo_5
import json


def is_accessible(path, mode='r'):
    try:
        f = open(path, mode)
        f.close()
    except IOError:
        return False
    return True


def main():
	authors = {}
	publications = []
	website = {}
	if is_accessible("data_collected/website.json"):
		with open('data_collected/website.json',encoding='utf-8') as filehandle:
			website = json.load(filehandle)
	if is_accessible("data_collected/authors.json"):
		with open('data_collected/publications.json',encoding='utf-8') as filehandle:  
			publications = json.load(filehandle)
		with open('data_collected/authors.json',encoding='utf-8') as filehandle:  
			authors = json.load(filehandle)
			
	print("Crawling dplb for data collection")
	top4 = ["https://dblp.org/db/conf/sp/",
			"https://dblp.org/db/conf/uss/", 
			"https://dblp.org/db/conf/ccs/",
			"https://dblp.org/db/conf/ndss/"]
	tier2 = ["https://dblp.org/db/conf/acsac/",
			"https://dblp.org/db/conf/raid/",
			"https://dblp.org/db/conf/esorics/"]

	AllLink = {}
	for i in top4:
		GetLink(i,AllLink)
	for i in tier2:
		GetLink(i,AllLink)

	updated = False
	for k,v in AllLink.items():
		if updated:
			break
		for w in v:
			if w not in website:
				updated = True
				print("New entry found. Updating db")
				break

	if updated:
		for k,v in AllLink.items():
			for link in AllLink[k]:
				update_db(link,authors,publications,k,website)
		print("loading information from top notch support by dear friend")
		finding_citation_count(publications)
		with open('data_collected/authors.json', 'w+', encoding='utf8') as filehandle:  
			json.dump(authors, filehandle)
		with open('data_collected/publications.json', 'w+', encoding='utf8') as filehandle:  
			json.dump(publications, filehandle)
		with open('data_collected/website.json', 'w+', encoding='utf-8') as filehandle:
			json.dump(website, filehandle)
	else:
		print("No new conference entry found. Useing previous crawled data to proceed")

	if updated:
		print("striping latin/no Engl Alph from name for consodition")
		authors = strip_latin(authors)
		print("consolidating author automically")
		consolidating_author(authors)
		with open('data_collected/authors_temp.json', 'w+', encoding='utf8') as filehandle:
			json.dump(authors, filehandle)
	else:
		print("Using previous consolidation record since no new entry found")
		with open('data_collected/authors_temp.json',encoding='utf-8') as filehandle:  
			authors = json.load(filehandle)

	print("consolidating the rest author(menually)")
	specific_consolidation(authors)
	print("Truncate all entry w/ <5 publication")
	truncate(authors)
	print("Consolidate info into web json")
	web_json = prepare_web_json(authors,publications)
	print("Input affiliation information and google scholar information")
	use_aff(web_json)
	use_gs(web_json)
	print("Set up completed, creating website")
	web_generation(web_json,publications)
	web_generation_wo_5(web_json,publications)

if __name__ == "__main__" :
	main()