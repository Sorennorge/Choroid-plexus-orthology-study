# -*- coding: utf-8 -*-

### ortholog matrix of ranked transporters ###

### Libraries ###

import os
import pandas as pd

## functions ##

def check_exist(folder,file):
    return os.path.exists(os.path.join(folder,file))

## Folders ##

folder1 = "Data/Transporter Lists"
folder2 = "Data/Count tables/All genes"
folder3 = "Data/Gene lists/Transporters/All genes"

out_folder = "Data/Transporter Lists/Ranked"

os.makedirs(out_folder,exist_ok=True)

## files ##

file_Transporter_rat = "Transporter_list_concatenated_rat.csv"
file_Transporter_human = "Transporter_list_concatenated_human.csv"
file_Transporter_mouse = "Transporter_list_concatenated_mouse.csv"
file_Transporter_zebrafish = "Transporter_list_concatenated_zebrafish.csv"


file_CT_rat = "Rat_count_table_all.csv"
file_CT_human = "Human_count_table_all.csv"
file_CT_zebrafish = "Zebrafish_count_table_all.csv"
file_CT_mouse = "Mouse_count_table_all.csv"

file_rat_shared_all = "Shared_orthologues_gene_in_all_species_list_Rat.csv"
file_human_shared_all = "Shared_orthologues_gene_in_all_species_list_Human.csv"
file_zebrafish_shared_all = "Shared_orthologues_gene_in_all_species_list_Zebrafish.csv"
file_mouse_shared_all = "Shared_orthologues_gene_in_all_species_list_Mouse.csv"

out_file_ranked_rat = "Ranked_Shared_Transporters_Rat.csv"
out_file_ranked_human = "Ranked_Shared_Transporters_Human.csv"
out_file_ranked_zebrafish = "Ranked_Shared_Transporters_Zebrafish.csv"
out_file_ranked_mouse = "Ranked_Shared_Transporters_Mouse.csv"


### Load data ###

# Transport lists #
df_transport_rat = pd.read_csv(os.path.join(folder1, file_Transporter_rat),sep=";")
df_transport_human = pd.read_csv(os.path.join(folder1, file_Transporter_human),sep=";")
df_transport_mouse = pd.read_csv(os.path.join(folder1, file_Transporter_mouse),sep=";")
df_transport_zebrafish = pd.read_csv(os.path.join(folder1, file_Transporter_zebrafish),sep=";")

## Count tables ##
# Rat #
df_CT_rat = pd.read_csv(os.path.join(folder2, file_CT_rat),sep=";")
df_CT_rat = df_CT_rat[['Ensembl ID','TPM']]
# Human #
df_CT_human = pd.read_csv(os.path.join(folder2, file_CT_human),sep=";")
df_CT_human = df_CT_human[['Ensembl ID','TPM']]
# Mouse #
df_CT_mouse = pd.read_csv(os.path.join(folder2, file_CT_mouse),sep=";")
df_CT_mouse = df_CT_mouse[['Ensembl ID','TPM']]
# Zebrafish #
df_CT_zebrafish = pd.read_csv(os.path.join(folder2, file_CT_zebrafish),sep=";")
df_CT_zebrafish = df_CT_zebrafish[['Ensembl ID','TPM']]

# Orthologues genes #

df_ortholog_rat = pd.read_csv(os.path.join(folder3, file_rat_shared_all),sep=";",header=None)[0].to_list()
df_ortholog_human = pd.read_csv(os.path.join(folder3, file_human_shared_all),sep=";",header=None)[0].to_list()
df_ortholog_mouse = pd.read_csv(os.path.join(folder3, file_mouse_shared_all),sep=";",header=None)[0].to_list()
df_ortholog_zebrafish = pd.read_csv(os.path.join(folder3, file_zebrafish_shared_all),sep=";",header=None)[0].to_list()


## Create matrix with Ensembl ID, Gene name, TPM and Rank ##

# Rat #
df_rat = df_transport_rat[['Ensembl ID','Gene symbol']].rename(columns={'Ensembl ID': 'Rat Ensembl ID','Gene symbol':'Rat Gene'})
df_rat = df_rat[df_rat['Rat Ensembl ID'].isin(df_ortholog_rat)]
df_rat = pd.concat([df_rat.set_index('Rat Ensembl ID'),df_CT_rat.set_index("Ensembl ID")],join='inner',axis=1)
df_rat = df_rat.reset_index().rename(columns={'index':"Rat Ensembl ID"})
df_rat = df_rat.sort_values(by='TPM',ascending=False).reset_index(drop=True)
df_rat['Rat Rank'] = df_rat['TPM'].rank(method = 'first',ascending=False)

# Human #
df_human = df_transport_human[['Ensembl ID','Gene symbol']].rename(columns={'Ensembl ID': 'Human Ensembl ID','Gene symbol':'Human Gene'})
df_human = df_human[df_human['Human Ensembl ID'].isin(df_ortholog_human)]
df_human = pd.concat([df_human.set_index('Human Ensembl ID'),df_CT_human.set_index("Ensembl ID")],join='inner',axis=1)
df_human = df_human.reset_index().rename(columns={'index':"Human Ensembl ID"})
df_human = df_human.sort_values(by='TPM',ascending=False).reset_index(drop=True)
df_human['Human Rank'] = df_human['TPM'].rank(method = 'first',ascending=False)

# Mouse #
df_mouse = df_transport_mouse[['Ensembl ID','Gene symbol']].rename(columns={'Ensembl ID': 'Mouse Ensembl ID','Gene symbol':'Mouse Gene'})
df_mouse = df_mouse[df_mouse['Mouse Ensembl ID'].isin(df_ortholog_mouse)]
df_mouse = pd.concat([df_mouse.set_index('Mouse Ensembl ID'),df_CT_mouse.set_index("Ensembl ID")],join='inner',axis=1)
df_mouse = df_mouse.reset_index().rename(columns={'index':"Mouse Ensembl ID"})
df_mouse = df_mouse.sort_values(by='TPM',ascending=False).reset_index(drop=True)
df_mouse['Mouse Rank'] = df_mouse['TPM'].rank(method = 'first',ascending=False)

# Zebrafish #
df_zebrafish = df_transport_zebrafish[['Ensembl ID','Gene symbol']].rename(columns={'Ensembl ID': 'Zebrafish Ensembl ID','Gene symbol':'Zebrafish Gene'})
df_zebrafish = df_zebrafish[df_zebrafish['Zebrafish Ensembl ID'].isin(df_ortholog_zebrafish)]
df_zebrafish = pd.concat([df_zebrafish.set_index('Zebrafish Ensembl ID'),df_CT_zebrafish.set_index("Ensembl ID")],join='inner',axis=1)
df_zebrafish = df_zebrafish.reset_index().rename(columns={'index':"Zebrafish Ensembl ID"})
df_zebrafish = df_zebrafish.sort_values(by='TPM',ascending=False).reset_index(drop=True)
df_zebrafish['Zebrafish Rank'] = df_zebrafish['TPM'].rank(method = 'first',ascending=False)

## save Ranked tables to files ##

# Rat #
df_rat.to_csv(os.path.join(out_folder,out_file_ranked_rat),sep=";",index=False)

# Human #
df_human.to_csv(os.path.join(out_folder,out_file_ranked_human),sep=";",index=False) 

# Mouse #
df_mouse.to_csv(os.path.join(out_folder,out_file_ranked_mouse),sep=";",index=False) 

# Zebrafish #
df_zebrafish.to_csv(os.path.join(out_folder,out_file_ranked_zebrafish),sep=";",index=False)


