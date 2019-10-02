import json

def prepare_web_json(authors,publications):
    web_json = []
    for p in publications:
        p["conference"] = p["conference"].upper()

    for author,pub in authors.items():
        tier_1 = []
        tier_1_a = []
        tier_1_c = 0
        tier_1_n = 0
        all = []
        all_a = []
        all_c = 0
        all_n = 0
        for p in pub:
            all.append({"index":p,"citation":max(0,publications[p]["citation"])})
            all_c += max(0,publications[p]["citation"])
            if publications[p]["citation"] >= 0:
                all_n += 1
            if (publications[p]["conference"] == 'SP') | (publications[p]["conference"] == 'USS') | (publications[p]["conference"] == 'CCS') | (publications[p]["conference"] == 'NDSS'): 
                tier_1.append({"index":p,"citation":max(0,publications[p]["citation"])})
                tier_1_c += max(0,publications[p]["citation"])
                if publications[p]["citation"] >= 0:
                    tier_1_n += 1
        tier_1 = sorted(tier_1, key = lambda i: i['citation'],reverse=True)
        for a in tier_1:
            tier_1_a.append(a["index"])
        all = sorted(all, key = lambda i: i['citation'],reverse=True)
        for a in all:
            all_a.append(a["index"])  
        
        top_5 = 0
        top_10 = 0
        
        for i in range(min(len(all_a),5)):
            top_5 += max(0,publications[all_a[i]]["citation"])
        for i in range(min(len(all_a),10)):
            top_10 += max(0,publications[all_a[i]]["citation"])
        if tier_1_n == 0:
            tier_1_n += 1
        if all_n == 0:
            all_n += 1
        web_json.append({"name":author,
            "tier_1_citation":tier_1_c,"tier_1_avg":tier_1_c/tier_1_n,"tier_1":tier_1_a,
            "total_citation":all_c,"total_avg":all_c/all_n,"all":all_a,
            "top_5":top_5,"top_10":top_10,"top_5_avg":top_5/min(all_n,5),"top_10_avg":top_10/min(all_n,10)})

    web_json = sorted(web_json, key = lambda i: i['total_citation'],reverse=True) 
    return web_json
    
