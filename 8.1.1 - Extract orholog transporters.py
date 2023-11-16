# -*- coding: utf-8 -*-

### Extract only ortholog transporters ###

import os
import pandas as pd

## Folders ##

folder1 = "Data/Biomart"
folder2 = "Data/Transporter Lists"
folder3 = "Data/Transporter Lists/Ortholog genes"

os.makedirs(folder3,exist_ok=True)

## Files ##

rat_file = "Transporter_list_concatenated_rat.csv"
human_file = "Transporter_list_concatenated_human.csv"
zebrafish_file = "Transporter_list_concatenated_zebrafish.csv"
mouse_file = "Transporter_list_concatenated_mouse.csv"

rat_file_out = "Transporter_list_concatenated_rat_ortholog.csv"
human_file_out = "Transporter_list_concatenated_human_ortholog.csv"
zebrafish_file_out = "Transporter_list_concatenated_zebrafish_ortholog.csv"
mouse_file_out = "Transporter_list_concatenated_mouse_ortholog.csv"

Ortholog_matrix_file = "Complete_Ortholog_Matrix.csv"

## Load data ##

# Ortholog matrix #
df_matrix = pd.read_csv(os.path.join(folder1,Ortholog_matrix_file),sep=";")

# Transporter lists #
df_rat = pd.read_csv(os.path.join(folder2,rat_file),sep=";")
df_human = pd.read_csv(os.path.join(folder2,human_file),sep=";")
df_mouse = pd.read_csv(os.path.join(folder2,mouse_file),sep=";")
df_zebrafish = pd.read_csv(os.path.join(folder2,zebrafish_file),sep=";")

# Extract ortholog transporters #
df_rat_ortholog = df_rat[df_rat['Ensembl ID'].isin(df_matrix['Rat ID'])]
df_human_ortholog = df_human[df_human['Ensembl ID'].isin(df_matrix['Human ID'])]
df_mouse_ortholog = df_mouse[df_mouse['Ensembl ID'].isin(df_matrix['Mouse ID'])]
df_zebrafish_ortholog = df_zebrafish[df_zebrafish['Ensembl ID'].isin(df_matrix['ZebraFish ID'])]

# Save ortholog transporters to files #
df_rat_ortholog.to_csv(os.path.join(folder3,rat_file_out),index=False,sep=";")
df_human_ortholog.to_csv(os.path.join(folder3,human_file_out),index=False,sep=";")
df_mouse_ortholog.to_csv(os.path.join(folder3,mouse_file_out),index=False,sep=";")
df_zebrafish_ortholog.to_csv(os.path.join(folder3,zebrafish_file_out),index=False,sep=";")