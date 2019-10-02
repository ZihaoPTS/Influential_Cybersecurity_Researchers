import json

def use_gs(web_json):
    with open('data/gs_search_results.json',encoding='utf-8') as filehandle:  
        gs_s = json.load(filehandle)

    for k,author in enumerate(web_json):
        v = gs_s[k]
        found = False
        for site in v["webPages"]["value"]:
            if author["name"] in site['name']:
                found = True
                author["gs_link"] = site['url']
                break
            if "Google Scholar Citations" in site['name']:
                found = True
                author["gs_link"] = site['url']
                break
        if not found:
                author["gs_link"] = ""