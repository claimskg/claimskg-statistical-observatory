import json

import plotly
import plotly.graph_objs as go

from modules import author_resume
from modules import entites_resume2
from modules import keywords_resume
from modules import numbers_claimskg_resume


##Get percent coverage of metadata
def create_barchart_percent_global():
    #avec auteur
    percent_with_author = author_resume.percent_claim_with_author()
    #avec entites
    # percent_with_entities = entites_resume2.percent_claim_with_entities()[1]
    percent_with_entities_cw = entites_resume2.percent_claim_with_entities()[0]
    percent_with_entities_cr = entites_resume2.percent_claim_with_entities()[1]
    #avec keywords
    percent_with_keywords = keywords_resume.percent_claim_with_keywords()[0]
    #avec keywords et entites
    percent_with_ent_keywords = keywords_resume.percent_ent_keywords()
    #avec les 3
    percent_with_3 = author_resume.get_3()
    #with dates published
    #claims creative work
    percent_dates_cw = numbers_claimskg_resume.percent_claim_with_dates()[0]
    percent_dates_cr = numbers_claimskg_resume.percent_claim_with_dates()[1]
    # with all
    percent_with_4 = author_resume.get_4()

    # m_ent_pc_we = entites_resume2.moy_ent_per_claims()[0]
    # m_ent_pc = entites_resume2.moy_ent_per_claims()[1]
    #
    # m_kw_pc_wk = keywords_resume.moy_keywords_per_claims()[0]
    # m_kw_pc = keywords_resume.moy_keywords_per_claims()[1]

    # labels = ['With author', 'With entities', 'With keywords', 'With keywords and entities', 'With all']
    labels = ['With author', 'With entities', 'With keywords', 'With dates', 'With keywords and entities', 'With entities, keywords, author', 'With all']

    values = []
    values.append(percent_with_author)
    values.append(percent_with_entities_cw)
    values.append(percent_with_entities_cr)
    values.append(percent_with_keywords)
    values.append(percent_with_ent_keywords)
    values.append(percent_with_3)
    values.append(percent_dates_cw)
    values.append(percent_dates_cr)
    values.append(percent_with_4)

    colors = ['blue', 'gold']

    trace0 = go.Bar(
        x=labels,
        y=[values[0],values[1],values[3],values[6],values[4],values[5],values[8]],
        name='Percent of claims',
        marker=dict(color=colors[0]))

    trace1 = go.Bar(
            x=[labels[1],labels[3]],
            y=[values[2],values[7]],
            name='Percent of claims reviews',
            marker=dict(color=colors[1]))

    data = [trace0, trace1]

    barchart_percent_global_JSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)


    # print(piechart_labels_JSON)
    return barchart_percent_global_JSON