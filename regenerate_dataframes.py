from modules import destack_all, add_themes_df2_keywords_after_destack, drop_doubles_col_themes_destack, \
    theme_indexer_newdata
#
# print("start gen 1")
# g1 = destack_all.explode_keywords()
# print(g1)

print("start gen 2")
g2 = add_themes_df2_keywords_after_destack.destack_themes_from_exploded()
print(g2)

print("start gen 3")
g3 = drop_doubles_col_themes_destack.set_destack_themes()
print(g3)

print("start gen 4")
g4 = theme_indexer_newdata.themes_indexed()
print(g4)
