# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

%reset -f "clear"

import pandas as pd


"lire le fichier Excel"
df = pd.ExcelFile(
            'bp-stats-review-2021-all-data.xlsx',
            )
# "afficher les feuilless Excel"
# # print(df.sheet_names)

"Transformer la feuille en DataFrame"
PEconso=pd.read_excel(df,'Primary Energy Consumption')

"Modifier les indexes des lignes"
PEconso=PEconso.set_index('Primary Energy: Consumption*')

" on transpose la matrice et on modifier les indexes des lignes"
PEconso=PEconso.T.set_index('Exajoules')

"on supprime les lignes il moins de 3 trois elements non-nan"
PEconso=PEconso.T.dropna(thresh=3)

"remplace les nan par zero"
PEconso=PEconso.fillna(0)

"supprimer les 5 dernieres colonnes"
PEconso = PEconso.iloc[:-3,:-5]

"creer une DF des totales"
PEconsoTT=PEconso[PEconso.index.str.contains('Total'or'OECD', regex=False)]
# PEconso=PEconso[PEconso.index.str.contains('Total'or'OECD', regex=False)]

"on concatene les TT avec la dataframe de base"
PEconso=pd.concat([PEconso,PEconsoTT])

"on supprime les doublons"
PEconso=PEconso.drop_duplicates(keep=False)

# PEconso.T.plot(figsize=(12, 6))