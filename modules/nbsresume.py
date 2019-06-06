#useless file to delete
import re
import statistics

# template du nécessaire pour mots clés

def claims_total():
# nb de claims total
    cw = 0
    fc = open("/home/dadou/PycharmProjects/FactCheckStat+back/modules/claim_id_cw.txt", "r")
    if fc:
        for ligne in fc.readlines() :
            cw += 1
    else :
        print("Fichier inaccessible")
    # print(cw)
    return cw
claims_total()

def keywords():
    cw_with_kw = {}
    #nb de claims avec mots clés
    #remplir un dico clé = id de claim, item  = mots clés
    #un dico de liste.. chq clé est associée a une liste de mots clés
    fk2 = open("/home/dadou/projects/ter_ips/claim_stat/keywords.txt", "r")
    if fk2 :
        mc = []
        patternk2 ="\'(.+)\'.+\(\'(.+)\'[,]"
        regexk2 = re.compile(patternk2, flags=re.IGNORECASE)
        for ligne in fk2.readlines() :
            resultatk2 = regexk2.search(ligne)
            if resultatk2 :
                ckw = resultatk2.group(1)
                keyw = resultatk2.group(2)
                keyw2 = keyw.lower()
                nl2 = keyw2.split(',')
                cw_with_kw[ckw] = nl2
                for mot in nl2:
                    mot = mot.lstrip()
                    mc.append(mot)
    else :
        print("Fichier inaccessible")

    kw = {}
    for mot in mc:
        if mot in kw:
            kw[mot] += 1
        else:
            kw[mot] = 1
    nbkw = len(kw.keys())
    # print(nbkw)#161 mots clés
    #rajouter au dico la longeur de la liste,
    #doit être une variable

    # print(cw_with_kw)
    cwkw= len(cw_with_kw.keys())
    # print(cwkw)#451 claims avc mots clés
    return nbkw, cwkw, cw_with_kw, kw
keywords()

def percentkw():
    #% nb de claims avec mots clés /nb de claims total
    # percent_kw = round((cwkw / cw * 100), 2)
    cwkw = keywords()[1]
    cw = claims_total()
    percent_kw = round((cwkw / cw * 100), 2)
    # print(percent_kw)
    return percent_kw
percentkw()


def moykw():
    # moyenne de nb de mots clés par assertion

    #Sur ceux qui ont des mots clés
    #récupération liste de kw pour chq claim, puis .len()
    cw_with_kw = keywords()[2]
    cwkw = keywords()[1]
    #façon lazy en premier
    nb_kw_pc = {}
    # for list_val in cw_with_kw.values():
    #     for i in list_val:
    #         i.lstrip()
    #         list_val.replace()
    # for key,list_val in cw_with_kw.items():
    #     # nb_kw_pc += key, list_val, len(list_val)
    #     # nb_kw_pc += key[list_val][len(list_val)]
    #     key[list_val] = [len(list_val)]
    nbpc = []
    # for key in cw_with_kw:
    #     for list_val in key:
    #     # nb_kw_pc += key, list_val, len(list_val)
    #     # nb_kw_pc += key[list_val][len(list_val)]
    #     #     list_val.append(len(list_val))
    #         list_val = list_val.lstrip()
    #         nb_kw_pc[key] = list_val
    for key,val in cw_with_kw.items():
        # nb_kw_pc += key, list_val, len(list_val)
        # nb_kw_pc += key[list_val][len(list_val)]
        #     list_val.append(len(list_val))
        # for i in val:
        #     list_val = i.lstrip()
        # nb_kw_pc[key][val] = len(val)
        nb_kw_pc[key]= len(val)
    # print(nb_kw_pc)
    # print(cw_with_kw)

    m = round(statistics.mean(nb_kw_pc.values()),2)
    print(m)
#    return m
    cw = claims_total()
    m2 = round(sum(nb_kw_pc.values())/cw,2)
    print(m2)
    return m, m2, nb_kw_pc

    # mwky = numpy.array(nb_kw_pc.values())
    # # mwky = numpy.asarray(nb_kw_pc.values())
    # print(mwky)
    # print(type(mwky))
    # # numpy.mean(mwky)
    # mwky.mean()
    # # mkw = numpy.array(mwky)
    # # mkw2 = numpy.mean(mkw)
    # # # mkw = mwky.mean()
    # # # mkw = numpy.mean(mwky)
    # # print(mkw2)
    # # mwky.mean()
    # print( mwky.mean())
    # # print(numpy.mean(mwky))
    # return mwky
moykw() #3.29490022172949 #m2=0.0924704418170504

#sur la totalité




#nb de mots clés pour chq claim
#mcpc = 0
#algo dico soit avec virgule soit je reprends le txt je fais un dico avec liste mc
#je for dico 1 si dico[clé]1 = dico2 alors +=1


# /nb de claims total
#mcpc / cw