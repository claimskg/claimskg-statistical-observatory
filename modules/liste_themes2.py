import re


def dico_themes():
    themes = {}
    list_themes = []
    nomlist = []
    # ct = 0
    somme_claim_themes = []

    # fk2 = open("/home/dadou/projects/ter_ips/claim_stat/cle_classes_true.txt", "r")
    fk2 = open("/home/dadou/projects/ter_ips/claim_stat/cle_classes_add1_newdata.txt", "r")
    # fk2 = open("/home/dadou/projects/ter_ips/claim_stat/cle_classes_add1.txt", "r")
    if fk2:
        # patternk2 ="(\w+[-]?\w*\s?\w*\s?\w*),\d+:*"
        # regexk2 = re.compile(patternk2, flags=re.IGNORECASE)
        for ligne in fk2.readlines():
            # resultatk2 = regexk2.search(ligne)
            res = re.search("(\w+[-]?\w*\s?\w*\s?\w*),\d+:", ligne)
            # res = re.findall("(\w+[-]?\w*\s?\w*\s?\w*),\d+[:]", ligne)
            res2 = re.findall("\'(\w+[-]?\w*\s?\w*\s?\w*)\'", ligne)
            res3 = re.findall(",(\d+)", ligne)
            # if res and res2 and res3 :
            if res:
                # nl = resultatk2.group(1)
                nomlist.append(res.group(1))
                # nomlist.append(res)
                # list_themes.append(res2)
                # res3 = [int(i) for i in res3]
                # somme_claim_themes.append(res3)
                if res2:
                    list_themes.append(res2)
                else:
                    list_themes.append('')
                if res3:
                    res3 = [int(i) for i in res3]
                    somme_claim_themes.append(res3)
                # ss_list = str(res.group(1))
                # ss_list = []
                # ct += 1
                # n_ss_list = 'ss_list'+str(ct)
                # print(res)
                # print(res2)
                # print(res3)
                # print(nl)
                # print(type(nl))

    # print(nomlist)
    # print(len(nomlist))
    # print(list_themes)
    # print(len(list_themes))
    # # print(somme_claim_themes)
    # print(len(somme_claim_themes))
    # ranger liste dans ss liste voir remplir dico

    for i in range(0, len(list_themes)):
        # print(i)
        themes[nomlist[i]] = list_themes[i]
    #
    # # for j in nomlist:
    # #     for i in list_themes:
    # #         themes[j] = i
    #
    print(themes)
    return themes
dico_themes()