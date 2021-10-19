# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd


"lire le fichier Excel"
df = pd.ExcelFile(
            'bp-stats-review-2021-all-data.xlsx',
            )
# "afficher les feuilless Excel"
# # print(df.sheet_names)

"Transformer la feuille en DataFrame"
A=pd.read_excel(df,'Primary Energy Consumption')
"Modifier les indexes des lignes"
A=A.set_index('Primary Energy: Consumption*')
" on transpose la matrice et on modifier les indexes des lignes"
A=A.T
A=A.set_index('Exajoules')
"on remet la matrice a sa place"
A=A.T
"on suprimme les lignes il moins de 3 trois elements non-nan"
A=A.dropna(thresh=3)

"remplace les nan par zero"
A=A.fillna(0)

"supprimer les deux dernieres colonnes"
A = A.iloc[: ,:-2]


A.T.plot(figsize=(12, 6))
