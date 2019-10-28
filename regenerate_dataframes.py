from modules.dataframes import set_destack_themes, generate_global_dataframe, generate_per_label_dataframe, \
    themes_indexed, destack_themes_from_exploded

print("Generating global dataframe...")
generation_df = generate_global_dataframe()

print("Generating truth value dataframe...")
generation_pl = generate_per_label_dataframe()

print("Generating themes dataframe...")
g2 = destack_themes_from_exploded()
print(g2)

g3 = set_destack_themes()
print(g3)

g4 = themes_indexed()
print(g4)
