def truncate(authors):
    temp = []

    for author,pub in authors.items():
        if len(pub) < 5:
            temp.append(author)

    for t in temp:
        del authors[t]
