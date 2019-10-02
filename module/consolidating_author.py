import json

def consolidating_author(authors):
    names = []
    merge = []

    for k,v in authors.items():
        names.append(k)

    for index,name in enumerate(names):
        for index_2,name_2 in enumerate(names[(index+1):],start=1):
            n = name.split()
            n_2 = name_2.split()
            l_n = len(n)
            l_n2 = len(n_2)
            count = 0
            for x in n:
                for y in n_2:
                    if x == y:
                        count = count + 1
                        n_2.remove(y)
                        break
            if count >= min(l_n,l_n2):
                merge.append([name,name_2,index,index+index_2])


    for x in merge:
        if x[0] in authors and x[1] in authors:
            if len(x[0]) >= len(x[1]):
                authors[x[0]].extend(authors[x[1]])
                del authors[x[1]]
            else:
                authors[x[1]].extend(authors[x[0]])
                del authors[x[0]]