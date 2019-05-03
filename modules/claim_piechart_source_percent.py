#!/usr/bin/env python
# import matplotlib.pyplot as plt
import json
import plotly
import plotly.graph_objs as go

######################################figure
def create_piechart_source():
    # load json
    with open("/home/dadou/PycharmProjects/FactCheckStat+back/modules/pourcentage_source_nb_claim", "r") as p2j:
        res2_parse = json.load(p2j)

    listauteur = []

    # valeur=ligne["name"]["value"].split("/")[-1]


    # for ligne in q2.bindings:
    for ligne in res2_parse["results"]["bindings"]:
        # val=str(ligne.get(rdflib.term.Variable('name')).split("/")[-1])
        val = str(ligne["name"]["value"].split("/")[-1])
        listauteur.append(val)

    # print(listauteur)
    listsansdoubln = list(set(listauteur))
    # print(listsansdoubln)


    dicauteur = {}
    for auteur in listsansdoubln:
        nbr = listauteur.count(auteur)
        dicauteur[auteur] = nbr
    # print("le nombre de claims pour l'auteur",auteur,"est=",str(nbr))
    #

    # labels = dicauteur.keys()
    labels = list(dicauteur.keys())
    # print(labels)

    sizes = []
    for cle in dicauteur.keys():
        sizes.append(dicauteur[cle])
    # print(sizes)

    colors = ['yellowgreen', 'lightskyblue', 'gold', 'lightcoral', 'blue']

    trace = [go.Pie(labels=labels, values=sizes,
                    hoverinfo='label+percent', textinfo='percent',
                    textfont=dict(size=20),
                    marker=dict(colors=colors))]

    # explode = (0, 0, 0, 0, 0.1)
    # plt.pie(sizes,explode=explode,labels=labels, colors=colors,
    #         autopct='%1.1f%%', shadow=False, startangle=90)
    # plt.axis('equal')
    # plt.savefig('PieChart01source.png')
    # plt.show()
    #

    piechart_sources_JSON = json.dumps(trace, cls=plotly.utils.PlotlyJSONEncoder)

    # print(piechart_sources_JSON)
    return piechart_sources_JSON
# create_piechart_source()