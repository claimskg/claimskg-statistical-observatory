import re
from pathlib import Path

#transform hand writting list of theme int a dictionnary
def dico_themes():
    themes = {}
    list_themes = []
    nomlist = []
    # ct = 0
    somme_claim_themes = []

    base_path = Path(__file__).parent
    file_path = (base_path / "cle_classes_add1_newdata.txt").resolve()
    fk2 = open(file_path, "r")

    if fk2:
        # patternk2 ="(\w+[-]?\w*\s?\w*\s?\w*),\d+:*"
        # regexk2 = re.compile(patternk2, flags=re.IGNORECASE)
        for ligne in fk2.readlines():
            # resultatk2 = regexk2.search(ligne)
            res = re.search("(\w+[-]?\w*\s?\w*\s?\w*),\d+:", ligne)
            # res = re.findall("(\w+[-]?\w*\s?\w*\s?\w*),\d+[:]", ligne)
            res2 = re.findall("\'(\w+[-]?\w*\s?\w*\s?\w*)\'", ligne)
            res3 = re.findall(",(\d+)", ligne)
            # if res and res2 and res3 :
            if res:
                nomlist.append(res.group(1))

                if res2:
                    list_themes.append(res2)
                else:
                    list_themes.append('')
                if res3:
                    res3 = [int(i) for i in res3]
                    somme_claim_themes.append(res3)

    for i in range(0, len(list_themes)):
        # print(i)
        themes[nomlist[i]] = list_themes[i]
    # print(themes)
    return themes
# dico_themes()