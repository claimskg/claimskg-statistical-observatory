from pathlib import Path

import pandas as pd

from modules import liste_themes2


def get_newdata_dico_themes():
    dico_themes = liste_themes2.dico_themes()

    #load df
    # df_complete = pd.read_csv('df_complete.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)
    base_path = Path(__file__).parent
    file_path = (base_path / "df_complete.csv").resolve()
    df_complete = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)

    #prepare list of distinct themes
    df_complete['keywords'] = df_complete['keywords'].str.split(',')

    df_list_themes = df_complete['keywords'].dropna().values.tolist()
    # print(df_list_themes)

    flat_list = [item for sublist in df_list_themes for item in sublist]
    # print(flat_list)

    distinctThemeRefList = list(set(flat_list))
    distinctThemeRefList.sort()
    # print(distinctThemeRefList)

    distinctThemeRefList_strip = []
    for i in distinctThemeRefList:
        new_i = str(i).lstrip().lower()
        distinctThemeRefList_strip.append(new_i)
    # print(distinctThemeRefList_strip)

    #Only strict matches
    statistics = ['rate', 'rates']
    economy = ['aid']
    environment1 = ['sea']
    health = ['care', 'hiv']
    data = ['data']
    #Only after
    middle_east = ['oman', 'iran']
    # environment2 = ['sea']
    law = ['law']

    ##########functions
    def list_strict_match(list1, list2):
        list_result = []
        for item in list1:
            split = item.split()
            for item2 in list2:
                # split = item.split()
                for j in split:
                    if j == item2:
                        # print(item)
                        list_result.append(item)
        return list(set(list_result))


    statistics_processed = list_strict_match(distinctThemeRefList_strip, statistics)
    economy_processed = list_strict_match(distinctThemeRefList_strip, economy)
    environment1_processed = list_strict_match(distinctThemeRefList_strip, environment1)
    health_processed = list_strict_match(distinctThemeRefList_strip, health)
    data_processed = list_strict_match(distinctThemeRefList_strip, data)

    # print(statistics_processed)
    # print(economy_processed)
    # print(environment1_processed)
    # print(health_processed)
    # print(data_processed)

    def list_derivation(list1, list2):
        list_result = []
        for item in list1:
            split = item.split()
            for item2 in list2:
                for j in split:
                    if j.startswith(item2):
                        # print(item)
                        list_result.append(item)
        return list(set(list_result))


    middle_east_processed = list_derivation(distinctThemeRefList_strip, middle_east)
    # environment2_processed = list_derivation(distinctThemeRefList_strip, environment2)
    law_processed = list_derivation(distinctThemeRefList_strip, law)

    # print(middle_east_processed)
    # print(environment2_processed)
    # print(law_processed)

    dico_themes['statistics'].extend(statistics_processed)
    # print(dico_themes['statistics'])
    dico_themes['statistics'].remove('rate')
    # print(dico_themes['statistics'])
    dico_themes['economy'].extend(economy_processed)
    dico_themes['economy'].remove('aid')
    # dico_themes['economy'].remove('aid')
    # print(dico_themes['economy'])
    dico_themes['environment'].extend(environment1_processed)
    dico_themes['environment'].remove('sea')
    dico_themes['health'].extend(health_processed)
    dico_themes['health'].remove('care')
    dico_themes['health'].remove('hiv')
    dico_themes['data'].extend(data_processed)
    dico_themes['data'].remove('data')
    dico_themes['middle east'].extend(middle_east_processed)
    dico_themes['middle east'].remove('oman')
    dico_themes['middle east'].remove('iran')
    # dico_themes['environment'].append(environment2_processed)
    dico_themes['laws'].extend(law_processed)
    dico_themes['laws'].remove('law')
    # dico_themes['laws'].remove('law')
    # print(dico_themes['laws'])
    # print(dico_themes)
    return dico_themes
# get_newdata_dico_themes()