import json
import statistics
import pandas as pd
from modules import entites_resume2
from pathlib import Path


# def list_numbers_resume():
##########################load df
# df_complete = pd.read_csv('df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
base_path = Path(__file__).parent
file_path = (base_path / "df_complete.csv").resolve()
df_complete = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)
# df_complete = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
#à reflechir à appeler sur une df, à rajouter comme paramètre aux fonctions

########################récup nb de claims total
nb_cw = entites_resume2.claims_total()[0]
nb_cr = entites_resume2.claims_total()[1]


def total_claim_review():
    nb_cr_total = len(df_complete['id1'].unique())
    # print(nb_cr_total)#28354
    return nb_cr_total
# total_claim_review()

def get_dates():
    min1 = df_complete['date1'].dropna().min()
    # min1 = pd.to_datetime(min1.dt.strftime('%B %d, %Y'))
    min1 = pd.to_datetime(min1)
    min1 = min1.strftime('%B %d, %Y')
    # print(min1)
    max1 = df_complete['date1'].dropna().max()
    max1 = pd.to_datetime(max1)
    max1 = max1.strftime('%B %d, %Y')
    min2 = df_complete['date2'].dropna().min()
    min2 = pd.to_datetime(min2)
    min2 = min2.strftime('%B %d, %Y')
    # min2 = min2.strftime('%B %d, %Y')
    max2 = df_complete['date2'].dropna().max()
    max2 = pd.to_datetime(max2)
    max2 = max2.strftime('%B %d, %Y')
    # max2 = max2.strftime('%B %d, %Y')
    # print(min2)
    # print(max2)
    return min1, max1, min2, max2
# get_dates()


# def percent_date_published():

# dates_cw = len(df_complete['date2'].dropna().unique())
# print(dates_cw)
# dates_cr = len(df_complete['date1'].dropna().unique())
# print(dates_cr)

def claim_with_dates():
    filtre_cw = df_complete['date2'].notna()
    df_filter_cw = df_complete[filtre_cw]
    nb_cw_with_dates = len(df_filter_cw['id2'].unique())

    filtre_cr = df_complete['date1'].notna()
    df_filter_cr = df_complete[filtre_cr]
    nb_cr_with_dates = len(df_filter_cr['id1'].unique())
    # print(nb_cw_with_dates)#18066
    # print(nb_cr_with_dates)#18089
    return nb_cw_with_dates, nb_cr_with_dates
# claim_with_dates()

def percent_claim_with_dates():
    # cw = claims_total()
    nb_cw_w_dates = claim_with_dates()[0]
    nb_cr_w_dates = claim_with_dates()[1]
    percent_dates_cw = round((nb_cw_w_dates/ nb_cw * 100), 2)
    percent_dates_cr = round((nb_cr_w_dates/ nb_cr * 100), 2)
    # print(percent_dates_cw)
    # print(percent_dates_cr)
    return percent_dates_cw, percent_dates_cr
# percent_claim_with_dates()


def numbers_of_author():
    nb_author = len(df_complete['author'].dropna().unique())
    # print(nb_author)
    return nb_author

def numbers_of_entities():
    nb_entities = len(df_complete['entity'].dropna().unique())
    # print(nb_entities)
    return nb_entities

def numbers_keywords():
    nb_keywords = len(df_complete['keywords'].dropna().unique())
    # print(nb_keywords)
    return nb_keywords
# numbers_keywords()

def list_numbers_resume():
    list_numbers_res = []
    claims = "Numbers of claims : " + str(nb_cw)
    claims_review = "Numbers of claims review : " + str(total_claim_review())
    dates = "Since " + str(get_dates()[2])+ " to " + str(get_dates()[1])
    author = "Numbers of authors : "+ str(numbers_of_author())
    entities = "Numbers of entities : "+ str(numbers_of_entities())
    keywords = "Numbers of keywords : "+ str(numbers_keywords())

    list_numbers_res.append(str(claims))
    list_numbers_res.append(str(claims_review))
    list_numbers_res.append(str(dates))
    list_numbers_res.append(str(author))
    list_numbers_res.append(str(entities))
    list_numbers_res.append(str(keywords))
    # print(list_numbers_res)
    list_numbers_resume_JSON = json.dumps(list_numbers_res)
    # print(list_numbers_resume_JSON)
    return list_numbers_res, list_numbers_resume_JSON
# list_numbers_resume()

def dico_numbers_resume():
    list = [
        {"Numbers of claims " : str(nb_cw),
         "Numbers of claims review " : str(total_claim_review()),
         "Since " : str(get_dates()[2]) , "to " : str(get_dates()[1]),
        "Numbers of authors " : str(numbers_of_author()),
        "Numbers of entities " : str(numbers_of_entities()),
        "Numbers of keywords " : str(numbers_keywords())}]
    # print(list)
    list_json = json.dumps(list)
    # print(list_json)
    return list_json