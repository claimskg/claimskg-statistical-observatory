import json
import statistics

########################récup nb de claims total
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

########################nb de claims avec entités
def nb_cw_w_ent():
    #load
    with open('/home/dadou/PycharmProjects/FactCheckStat+back/modules/dic_entities_JSON','r') as fjson :
        dic_ent_l = json.load(fjson)

    # #= nb de clés du dico
    nb_cw_w_ent = len(dic_ent_l.keys())
    # print(nb_cw_w_ent)
    #
    # #
    return dic_ent_l, nb_cw_w_ent
nb_cw_w_ent()

def percent_cw_w_ent():
    cw = claims_total()
    nb_w_ent = nb_cw_w_ent()[1]
    percent_ent = round((nb_w_ent / cw * 100), 2)
    print(percent_ent)
    return percent_ent
percent_cw_w_ent()

#################################moyenne entités par claims

def moy_ent():
    dic_ent_l = nb_cw_w_ent()[0]
    nb_ent_pc = {}
    for key,val in dic_ent_l.items():
        nb_ent_pc[key]= len(val)

    m_ent_pc_wc = round(statistics.mean(nb_ent_pc.values()),2)
    print(m_ent_pc_wc)
        #    return m
    cw = claims_total()
    m_ent_pc = round(sum(nb_ent_pc.values())/cw,2)
    print(m_ent_pc)
    return m_ent_pc_wc, m_ent_pc, nb_ent_pc
moy_ent()