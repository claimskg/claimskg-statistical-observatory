
#
# print("start gen 1")
# g1 = destack_all.explode_keywords()
# print(g1)

from modules import construct_df_multi_queries_sparql
print("Generating global dataframe...")
generation_df = construct_df_multi_queries_sparql.generate_global_dataframe()

from modules import Data_Source_Veracite
print("Generating truth value dataframe...")
generation_pl = Data_Source_Veracite.generate_per_label_dataframe()

from modules import add_themes_df2_keywords_after_destack
print("Generating themes dataframe...")
g2 = add_themes_df2_keywords_after_destack.destack_themes_from_exploded()
print(g2)


from modules import drop_doubles_col_themes_destack
g3 = drop_doubles_col_themes_destack.set_destack_themes()
print(g3)

from modules import theme_indexer_newdata
g4 = theme_indexer_newdata.themes_indexed()
print(g4)
