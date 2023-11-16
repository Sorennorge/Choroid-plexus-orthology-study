# -*- coding: utf-8 -*-

### reduce count tables to only ortholog genes ###

## Libraries ##

import os
import pandas as pd

## Folders ##

folder1 = "Data/Biomart"
folder2 = "Data/Count tables/All genes"
folder3 = "Data/Count tables/Ortholog genes"

os.makedirs(folder3,exist_ok=True)

## Files ##

Ortholog_matrix_file = "Complete_Ortholog_Matrix.csv"

human_file = "Human_count_table_all.csv"
rat_file = "Rat_count_table_all.csv"
mouse_file = "Mouse_count_table_all.csv"
zebrafish_file = "Zebrafish_count_table_all.csv"

human_file_out = "Human_count_table_ortholog.csv"
rat_file_out = "Rat_count_table_ortholog.csv"
mouse_file_out = "Mouse_count_table_ortholog.csv"
zebrafish_file_out = "Zebrafish_count_table_ortholog.csv"

## Load data ##

# Ortholog matrix #
df_matrix = pd.read_csv(os.path.join(folder1,Ortholog_matrix_file),sep=";")

# Count tables #
df_human = pd.read_csv(os.path.join(folder2,human_file),sep=";")
df_rat = pd.read_csv(os.path.join(folder2,rat_file),sep=";")
df_mouse = pd.read_csv(os.path.join(folder2,mouse_file),sep=";")
df_zebrafish = pd.read_csv(os.path.join(folder2,zebrafish_file),sep=";")

## extract only ortholog genes ##
df_human_ortholog = df_human[df_human['Ensembl ID'].isin(df_matrix['Human ID'])]
df_rat_ortholog = df_rat[df_rat['Ensembl ID'].isin(df_matrix['Rat ID'])]
df_mouse_ortholog = df_mouse[df_mouse['Ensembl ID'].isin(df_matrix['Mouse ID'])]
df_zebrafish_ortholog = df_zebrafish[df_zebrafish['Ensembl ID'].isin(df_matrix['ZebraFish ID'])]

## Save genes (ortholog) count tables ## 
df_human_ortholog.to_csv(os.path.join(folder3,human_file_out),index=False,sep=";")
df_rat_ortholog.to_csv(os.path.join(folder3,rat_file_out),index=False,sep=";")
df_mouse_ortholog.to_csv(os.path.join(folder3,mouse_file_out),index=False,sep=";")
df_zebrafish_ortholog.to_csv(os.path.join(folder3,zebrafish_file_out),index=False,sep=";")

