import csv
from pathlib import Path

import pandas as pd


def themes_indexed():
    ###load df
    # df_destack_set = pd.read_csv('df_destack_themes_v2_set.csv', dtype={"id1": str, "id2": str, "entity": str, "themes":str}, header=0)
    base_path = Path(__file__).parent
    file_path = (base_path / "df_destack_themes_v2_set.csv").resolve()
    df_destack_set = pd.read_csv(file_path, dtype={"id1": str, "id2": str, "entity": str}, header=0)

    print(df_destack_set['themes'])

    df_list_themes = df_destack_set['themes'].dropna().drop_duplicates()

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

    # print(isinstance(df_destack_set['themes'][23],(list,)))
    # print(isinstance(df_destack_set['themes'][23],(str,)))
    # print(df_destack_set['themes'][23])
    # print(df_destack_set['themes'])

    # https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
    # Note that pandas/NumPy uses the fact that np.nan != np.nan, and treats None like np.nan.

    def list_indexer_themes(row_internal, liste_refs):
        # get theme_list from row
        col_list = row_internal['themes']
        # construction of empty vector at accurate size
        sparse_vector = [0] * len(liste_refs)
        # cas nominal : liste de string
        if isinstance(col_list,(list,)):
            #  Setting to one the existing themes
            for theme in col_list:
                index =  liste_refs.index(theme)
                sparse_vector[index]=1

            return sparse_vector
        else:
            return sparse_vector


    df_destack_set['themesIndexed'] = df_destack_set.apply(lambda row: list_indexer_themes(row, distinctThemeRefList3), axis=1)
    print(df_destack_set['themesIndexed'])
    #
    df_destack_set[distinctThemeRefList3] = pd.DataFrame(df_destack_set.themesIndexed.values.tolist(), index= df_destack_set.index)
    #
    # #df to csv
    df_destack_set.to_csv('df_destack_themes_indexed.csv', quoting=csv.QUOTE_MINIMAL, na_rep='NaN', index=False)
    return 'ok df themes indexed'
