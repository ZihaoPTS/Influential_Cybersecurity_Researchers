import json

def specific_consolidation(authors):
    indexs = [1,10,18,35,51,65,70]

    with open('data/merge.json',encoding='utf-8') as filehandle:  
        merge = json.load(filehandle)
    for index in indexs:
        if len(merge[index][0]) > len(merge[index][1]):
            authors[merge[index][0]].extend(authors[merge[index][1]])
            del authors[merge[index][1]]
        else:
            authors[merge[index][1]].extend(authors[merge[index][0]])
            del authors[merge[index][0]]
