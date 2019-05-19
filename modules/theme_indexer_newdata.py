import csv
import pandas as pd
from pathlib import Path
from modules import drop_doubles_col_themes_destack


#generate df_destack_themes_v2_set.csv
# generation = drop_doubles_col_themes_destack.set_destack_themes()
# print(generation)

def themes_indexed():
    ###load df
    # df_destack_set = pd.read_csv('df_destack_themes_v2_set.csv', dtype={"id1": str, "id2": str, "entity": str, "themes":str}, header=0)
    base_path = Path(__file__).parent
    file_path = (base_path / "df_destack_themes_v2_set.csv").resolve()
    df_destack_set = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)

    # df_destack_set = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_destack_themes_v2_set.csv', dtype={"id1": str, "id2": str, "entity": str, "themes":str}, header=0)
    # df_destack_set = pd.read_csv('/home/dadou/PycharmProjects/FactCheckStat+back/modules/df_destack_themes_v2_set.csv', dtype={"id1": str, "id2": str, "entity": str}, header=0)

    ####load distinct theme ref list
    # creation liste de themes distincts
    # print(df_destack_set['themes'])
    # df_destack_set['themes'] = df_destack_set['themes'].str.split(',')
    print(df_destack_set['themes'])

    # df_list_themes = df_destack_set['themes'].dropna().drop_duplicates().values.tolist()
    #
    # def distinct_themes_list():
    df_list_themes = df_destack_set['themes'].dropna().drop_duplicates()
    #
    # # df_list_themes = str(df_destack_set['themes'].dropna().values.tolist())
    # print(df_list_themes)
    #
    listr = []
    for row in df_list_themes:
        # print(row)
        st = str(row)
        # print(st)
        new_st = st.replace('[','')
        new_st = new_st.replace(']', '')
        # print(new_st)
        new_st = new_st.replace("'", "")
        # print(new_st)
        ll = new_st.split(',')
        # print(ll)
        listr.append(ll)

    flat_list = [item for sublist in listr for item in sublist]
    # print(flat_list)

    distinctThemeRefList = list(set(flat_list))
    distinctThemeRefList.sort()
    # print(distinctThemeRefList)

    distinctThemeRefList2 = []
    for i in distinctThemeRefList:
        i = i.lstrip()
        distinctThemeRefList2.append(i)
    # print(distinctThemeRefList2)

    distinctThemeRefList3 = list(set(distinctThemeRefList2))
    distinctThemeRefList3.sort()
    # print(distinctThemeRefList3)


    def col_destack_to_list(ligne):
        tolist = ligne['themes']
        if pd.isnull(tolist):
            return tolist
        else:
            listr = []
            new_stolist = tolist.replace('[', '')
            new_stolist = new_stolist.replace(']', '')
            new_stolist = new_stolist.replace("'", "")
            # print(new_stolist)
            llist = new_stolist.split(',')
            # print(llist)
            for i in llist:
                i = i.lstrip()
                # print(i)
                listr.append(i)
            # listr.append(llist)
            #     print(listr)
            return listr

    df_destack_set['themes'] = df_destack_set.apply(lambda row: col_destack_to_list(row), axis=1)

    # df_destack_set['themes'] = df_destack_set['themes'].str.split(',')
    # print(df_destack_set['themes'])
    print(isinstance(df_destack_set['themes'][23],(list,)))
    print(isinstance(df_destack_set['themes'][23],(str,)))
    print(df_destack_set['themes'][23])
    # p = list(df_destack_set['themes'][23])
    # print(p)
    # df_destack_set['themes'] = str(df_destack_set['themes'])
    print(df_destack_set['themes'])

    # df_destack_set['themes'] = df_destack_set['themes'].str.split(',')
    # print(df_destack_set['themes'])
    # todo memo
    #  .fillna('missing')
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
    # Note that pandas/NumPy uses the fact that np.nan != np.nan, and treats None like np.nan.

    def list_indexer_themes(row_internal, liste_refs):
        # get theme_list from row
        col_list = row_internal['themes']
        # construction du vecteur vide a la bonne taille
        sparse_vector = [0] * len(liste_refs)
        # cas nominal : liste de string
        if isinstance(col_list,(list,)):
            #  on met a 1 les theme qui existe dans le vecteur
            for theme in col_list:
                index =  liste_refs.index(theme)
                sparse_vector[index]=1

            return sparse_vector
        else:
            return sparse_vector
        # else:
        #     index = liste_refs.index(col_list)
        #     sparse_vector[index]=1
        #     return sparse_vector

    df_destack_set['themesIndexed'] = df_destack_set.apply(lambda row: list_indexer_themes(row, distinctThemeRefList3), axis=1)
    print(df_destack_set['themesIndexed'])
    #
    df_destack_set[distinctThemeRefList3] = pd.DataFrame(df_destack_set.themesIndexed.values.tolist(), index= df_destack_set.index)
    #
    # #df to csv
    df_destack_set.to_csv('df_destack_themes_indexed.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    return 'ok df themes indexed'
