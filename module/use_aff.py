import json

def use_aff(web_json):
    with open('data/affiliation.json',encoding='utf-8') as filehandle:  
        affiliation = json.load(filehandle)
    N_A = 0 
    for author in web_json:
        found = False
        if author['name'] in affiliation:
            author['affiliation'] = affiliation[author['name']]
            continue
        else:
            for k,v in affiliation.items():
                n = author['name'].split()
                n_2 = k.split()
                l_n = len(n)
                l_n2 = len(n_2)
                count = 0
                for x in n:
                    for y in n_2:
                        if x == y:
                            count = count + 1
                            n.remove(x)
                            n_2.remove(y)
                            break
                if count >= min(l_n,l_n2):
                    author['affiliation'] = v
                    found = True
                    break
        if not found:
            author['affiliation'] = "N/A"
            N_A = N_A + 1
    print("There are a total of " + str(len(web_json)) + " entry, " + str(N_A) + " entry does not have affiliation information. If the number is too high please change affiliation.json at data folder")
