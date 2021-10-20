# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 14:23:55 2021

@author: Kraemer
"""
"Import librairies"
import pandas as pd 
import os 
import numpy as np
import statistics as st
"Set the working directory"
os.chdir("C:/Users/Kraemer/Desktop/Projet python") #set the working directory
os.listdir() #see files

"Read the data in .txt format"
df = pd.read_fwf('PERGDP.TXT', header=None , delim_whitespace=True) #read .txt, header=None --> variable name automatically created

"Some details on data"
list(df.columns.values) #list the name of columns
df.columns.map(type) #see the header type 
df.dtypes #see the variables type
df = df.rename(columns={0: 'Varname', 1: 'Country', 2: 'Year', 3: 'GDP_cap'}) #rename columns

"Reshape the data"
df =df.replace({"   ..":np.NaN}) #replace missing values by NaN to convert into numeric
df["GDP_cap"] = pd.to_numeric(df["GDP_cap"]) #object to numeric
df = df.pivot_table(index="Year",columns="Country", values= "GDP_cap" ) #pivot the table 

"See nan by columns"
a = list(df.isna().sum())
st.median(a)

"Drop observation that have more than 11 NaN"
# df=df.dropna(thresh=31, axis =1)
df = df.T
df = df[df.isna().sum(axis=1) < 11]
df = df.T               
