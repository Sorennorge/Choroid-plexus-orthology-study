# -*- coding: utf-8 -*-

### Create count tables for human, rat, mouse, and zebrafish ###

import os
import pandas as pd

## Folders ##

Folder_biomart = "Data/Biomart/Gene info"

Folder_human_data = "Data/RNA STAR/Human"
Folder_rat_data = "Data/RNA STAR/Rat"
Folder_mouse_data = "Data/RNA STAR/Mouse"
Folder_zebrafish_data = "Data/RNA STAR/Zebrafish"

Folder_count_tables = "Data/Count tables/All genes"

os.makedirs(Folder_count_tables,exist_ok=True)

## Files ##

File_human_biomart = "Human_biomart_ensembl_gene.txt"
File_rat_biomart = "Rat_biomart_ensembl_gene.txt"
File_mouse_biomart = "Mouse_biomart_ensembl_gene.txt"
File_zebrafish_biomart = "Zebrafish_biomart_ensembl_gene.txt"

File_human_raw = "Human_RSEM_protein_coding_1.txt"
File_rat_raw = "Rat_RSEM_protein_coding_1.txt"
File_mouse_raw = "Mouse_RSEM_protein_coding_1.txt"
File_zebrafish_raw = "Zebrafish_RSEM_protein_coding_1.txt"

File_human_count_table = "Human_count_table_all.csv"
File_rat_count_table = "Rat_count_table_all.csv"
File_mouse_count_table = "Mouse_count_table_all.csv"
File_zebrafish_count_table = "Zebrafish_count_table_all.csv"

### Load load ###

## Gene info ##

# Human #
df_info_human = pd.read_csv(os.path.join(Folder_biomart,File_human_biomart),sep=",")
df_info_human = df_info_human.rename(columns=({"Gene stable ID":"Ensembl ID"}))
df_info_human_dict = df_info_human.set_index("Ensembl ID")['Gene name'].to_dict()

# Rat #

df_info_rat = pd.read_csv(os.path.join(Folder_biomart,File_rat_biomart),sep=",")
df_info_rat = df_info_rat.rename(columns=({"Gene stable ID":"Ensembl ID"}))
df_info_rat_dict = df_info_rat.set_index("Ensembl ID")['Gene name'].to_dict()

# Mouse #

df_info_mouse = pd.read_csv(os.path.join(Folder_biomart,File_mouse_biomart),sep=",")
df_info_mouse = df_info_mouse.rename(columns=({"Gene stable ID":"Ensembl ID"}))
df_info_mouse_dict = df_info_mouse.set_index("Ensembl ID")['Gene name'].to_dict()

# zebrafish #

df_info_zebrafish = pd.read_csv(os.path.join(Folder_biomart,File_zebrafish_biomart),sep=",")
df_info_zebrafish = df_info_zebrafish.rename(columns=({"Gene stable ID":"Ensembl ID"}))
df_info_zebrafish_dict = df_info_zebrafish.set_index("Ensembl ID")['Gene name'].to_dict()

## Load data and create count tables ##

# Human #

df_human = pd.read_csv(os.path.join(Folder_human_data,File_human_raw),sep="\t",usecols=("gene_id","TPM"),decimal=".",dtype={"gene_id":str,"TPM":float})
df_human = df_human.rename(columns=({"gene_id":"Ensembl ID","TPM": "TPM 1"}))

for i in range(2,7,1):
    File_human_raw = "Human_RSEM_protein_coding_{}.txt".format(i)
    df_human_addition = pd.read_csv(os.path.join(Folder_human_data,File_human_raw),sep="\t",usecols=("gene_id","TPM"),decimal=".",dtype={"gene_id":str,"TPM":float})
    df_human_addition_dict = df_human_addition.set_index("gene_id")['TPM'].to_dict()
    df_human["TPM {}".format(i)] = df_human["Ensembl ID"].map(df_human_addition_dict)

# Calculate mean of all samples (round 2 decimals) -> TPM #
df_human['TPM'] = df_human[['TPM 1','TPM 2','TPM 3','TPM 4','TPM 5','TPM 6']].mean(axis=1).round(2)
# Map gene names #
df_human['Gene name'] = df_human["Ensembl ID"].map(df_info_human_dict)
# Fill non existing gene names as "N/A" #
df_human['Gene name'] = df_human['Gene name'].fillna("N/A")
# Create count table and reduce to TPM > zero #
df_human_count_table = df_human[["Ensembl ID","Gene name","TPM"]]
df_human_count_table = df_human_count_table.loc[df_human_count_table['TPM'] > 0]

# Rat #

df_rat = pd.read_csv(os.path.join(Folder_rat_data,File_rat_raw),sep="\t",usecols=("gene_id","TPM"),decimal=".",dtype={"gene_id":str,"TPM":float})
df_rat = df_rat.rename(columns=({"gene_id":"Ensembl ID","TPM": "TPM"}))

# Map gene names #
df_rat['Gene name'] = df_rat["Ensembl ID"].map(df_info_rat_dict)
# Fill non existing gene names as "N/A" #
df_rat['Gene name'] = df_rat['Gene name'].fillna("N/A")
# Create count table and reduce to TPM > zero #
df_rat_count_table = df_rat[["Ensembl ID","Gene name","TPM"]]
df_rat_count_table = df_rat_count_table.loc[df_rat_count_table['TPM'] > 0]

# Mouse #

df_mouse = pd.read_csv(os.path.join(Folder_mouse_data,File_mouse_raw),sep="\t",usecols=("gene_id","TPM"),decimal=".",dtype={"gene_id":str,"TPM":float})
df_mouse = df_mouse.rename(columns=({"gene_id":"Ensembl ID","TPM": "TPM 1"}))

for i in range(2,9,1):
    File_mouse_raw = "Mouse_RSEM_protein_coding_{}.txt".format(i)
    df_mouse_addition = pd.read_csv(os.path.join(Folder_mouse_data,File_mouse_raw),sep="\t",usecols=("gene_id","TPM"),decimal=".",dtype={"gene_id":str,"TPM":float})
    df_mouse_addition_dict = df_mouse_addition.set_index("gene_id")['TPM'].to_dict()
    df_mouse["TPM {}".format(i)] = df_mouse["Ensembl ID"].map(df_mouse_addition_dict)

# Calculate mean of all samples (round 2 decimals) -> TPM #
df_mouse['TPM'] = df_mouse[['TPM 1','TPM 2','TPM 3','TPM 4','TPM 5','TPM 6','TPM 7','TPM 8']].mean(axis=1).round(2)
# Map gene names #
df_mouse['Gene name'] = df_mouse["Ensembl ID"].map(df_info_mouse_dict)
# Fill non existing gene names as "N/A" #
df_mouse['Gene name'] = df_mouse['Gene name'].fillna("N/A")
# Create count table and reduce to TPM > zero #
df_mouse_count_table = df_mouse[["Ensembl ID","Gene name","TPM"]]
df_mouse_count_table = df_mouse_count_table.loc[df_mouse_count_table['TPM'] > 0]

# Zebrafish #

df_zebrafish = pd.read_csv(os.path.join(Folder_zebrafish_data,File_zebrafish_raw),sep="\t",usecols=("gene_id","TPM"),decimal=".",dtype={"gene_id":str,"TPM":float})
df_zebrafish = df_zebrafish.rename(columns=({"gene_id":"Ensembl ID","TPM": "TPM 1"}))

for i in range(2,3,1):
    File_zebrafish_raw = "Zebrafish_RSEM_protein_coding_{}.txt".format(i)
    df_zebrafish_addition = pd.read_csv(os.path.join(Folder_zebrafish_data,File_zebrafish_raw),sep="\t",usecols=("gene_id","TPM"),decimal=".",dtype={"gene_id":str,"TPM":float})
    df_zebrafish_addition_dict = df_zebrafish_addition.set_index("gene_id")['TPM'].to_dict()
    df_zebrafish["TPM {}".format(i)] = df_zebrafish["Ensembl ID"].map(df_zebrafish_addition_dict)

# Calculate mean of all samples (round 2 decimals) -> TPM #
df_zebrafish['TPM'] = df_zebrafish[['TPM 1','TPM 2']].mean(axis=1).round(2)
# Map gene names #
df_zebrafish['Gene name'] = df_zebrafish["Ensembl ID"].map(df_info_zebrafish_dict)
# Fill non existing gene names as "N/A" #
df_zebrafish['Gene name'] = df_zebrafish['Gene name'].fillna("N/A")
# Create count table and reduce to TPM > zero #
df_zebrafish_count_table = df_zebrafish[["Ensembl ID","Gene name","TPM"]]
df_zebrafish_count_table = df_zebrafish_count_table.loc[df_zebrafish_count_table['TPM'] > 0]

### Save count tables ###

df_human_count_table.to_csv(os.path.join(Folder_count_tables,File_human_count_table),index=False,sep=";")
df_rat_count_table.to_csv(os.path.join(Folder_count_tables,File_rat_count_table),index=False,sep=";")
df_mouse_count_table.to_csv(os.path.join(Folder_count_tables,File_mouse_count_table),index=False,sep=";")
df_zebrafish_count_table.to_csv(os.path.join(Folder_count_tables,File_zebrafish_count_table),index=False,sep=";")

