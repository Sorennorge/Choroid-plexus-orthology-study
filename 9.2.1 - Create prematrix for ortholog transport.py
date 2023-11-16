# -*- coding: utf-8 -*-

### Create prematrix ortholog Transport matrix ##

## Libraries ##

import os
import pandas as pd
import numpy as np

## Folders ##

folder1 = "Data/Transporter Lists/Ranked"
folder2 = "Data/Biomart/Ranked transport"
folder3 = "Data/Biomart orthologs/Merged orthology matrix"
os.makedirs(folder3,exist_ok=True)

## Files ##

# Ranked files #
file_ranked_Rat = "Ranked_Shared_Transporters_Rat.csv"
file_ranked_Human = "Ranked_Shared_Transporters_Human.csv"
file_ranked_Zebrafish = "Ranked_Shared_Transporters_Zebrafish.csv"
file_ranked_Mouse = "Ranked_Shared_Transporters_Mouse.csv"

# Ortholog matrix #
Ortholog_matrix_shared_transporters = "Transporter_shared_ortholog_matrix.csv"

#output #

Collapsed_ortholog_matrix = "Collapsed Transport ortholog matrix.xlsx"

## Load data ##

# Ranked lists #
df_rat = pd.read_csv(os.path.join(folder1, file_ranked_Rat),sep=";")
df_human = pd.read_csv(os.path.join(folder1, file_ranked_Human),sep=";")
df_mouse = pd.read_csv(os.path.join(folder1, file_ranked_Mouse),sep=";")
df_zebrafish = pd.read_csv(os.path.join(folder1, file_ranked_Zebrafish),sep=";")

# ortholog matrix#

df_ortholog = pd.read_csv(os.path.join(folder2, Ortholog_matrix_shared_transporters),sep=";")
df_ortholog = df_ortholog.rename(columns={"ZebraFish ID":"Zebrafish ID"})


## create convertion dict ##

# Genes #
rat_genes_dict = df_rat.set_index('Rat Ensembl ID')['Rat Gene'].to_dict()
human_genes_dict = df_human.set_index('Human Ensembl ID')['Human Gene'].to_dict()
mouse_genes_dict = df_mouse.set_index('Mouse Ensembl ID')['Mouse Gene'].to_dict()
zebrafish_genes_dict = df_zebrafish.set_index('Zebrafish Ensembl ID')['Zebrafish Gene'].to_dict()
# TPM #

rat_TPM_dict = df_rat.set_index('Rat Ensembl ID')['TPM'].to_dict()
human_TPM_dict = df_human.set_index('Human Ensembl ID')['TPM'].to_dict()
mouse_TPM_dict = df_mouse.set_index('Mouse Ensembl ID')['TPM'].to_dict()
zebrafish_TPM_dict = df_zebrafish.set_index('Zebrafish Ensembl ID')['TPM'].to_dict()



### In lack of a better function ###

# init global values #
df_collapsed_matrix = []
indexer = 0
progress_counter = 0
percentage = 0
# Run the brute algorithm #
for index, row in df_ortholog.iterrows():
    # Progress counter
    if progress_counter % round(len(df_ortholog)/100) == 0 and percentage < 110:
        percentage += 1
        if percentage % 10 == 0:
            print("Collapsing ortholog matrix - Progress: {} / 100 %".format(percentage))
    progress_counter += 1
    # if an entry of Rat, Human, Mouse or Zebrafish already in the collapsed matrix #
    if any((row['Rat ID'] in elem[0] or 
            row['Human ID'] in elem[1] or 
            row['Mouse ID'] in elem[2] or 
            row['Zebrafish ID'] in elem[3]) for elem in df_collapsed_matrix):
        # Run through all entries and append to the correct entry the additional species entry
        for i in range(0,len(df_collapsed_matrix),1):
            if (row['Rat ID'] in df_collapsed_matrix[i][0] or 
                row['Human ID'] in df_collapsed_matrix[i][1] or 
                row['Mouse ID'] in df_collapsed_matrix[i][2] or 
                row['Zebrafish ID'] in df_collapsed_matrix[i][3]):
                # If not the new entry is included in the row and column of specific species, append that entry
                if not row['Rat ID'] in df_collapsed_matrix[i][0]:
                    df_collapsed_matrix[i][0].append(row['Rat ID'])
                if not row['Human ID'] in df_collapsed_matrix[i][1]:
                    df_collapsed_matrix[i][1].append(row['Human ID'])
                if not row['Mouse ID'] in df_collapsed_matrix[i][2]:
                    df_collapsed_matrix[i][2].append(row['Mouse ID'])
                if not row['Zebrafish ID'] in df_collapsed_matrix[i][3]:
                    df_collapsed_matrix[i][3].append(row['Zebrafish ID'])
            else:
                pass
    else:
        df_collapsed_matrix.append([])
        df_collapsed_matrix[indexer] = ([],[],[],[])
        df_collapsed_matrix[indexer][0].append(row['Rat ID'])
        df_collapsed_matrix[indexer][1].append(row['Human ID'])
        df_collapsed_matrix[indexer][2].append(row['Mouse ID'])
        df_collapsed_matrix[indexer][3].append(row['Zebrafish ID'])
        #df_collapsed_matrix.append([row['Rat ID'],row['Human ID'],row['Mouse ID'],row['Zebrafish ID']])
        indexer += 1

## Reduced dublicated entries ##

df_collapsed_matrix_accepted = []
df_collapsed_matrix_dublicate_check_rat = []
df_collapsed_matrix_dublicate_check_human = []
df_collapsed_matrix_dublicate_check_mouse = []
df_collapsed_matrix_dublicate_check_zebrafish = []
for row in df_collapsed_matrix:
    if (tuple(sorted(row[0])) not in df_collapsed_matrix_dublicate_check_rat and
    tuple(sorted(row[1])) not in df_collapsed_matrix_dublicate_check_human and
    tuple(sorted(row[2])) not in df_collapsed_matrix_dublicate_check_mouse and
    tuple(sorted(row[3])) not in df_collapsed_matrix_dublicate_check_zebrafish):
        df_collapsed_matrix_dublicate_check_rat.append(tuple(sorted(row[0])))
        df_collapsed_matrix_dublicate_check_human.append(tuple(sorted(row[1])))
        df_collapsed_matrix_dublicate_check_mouse.append(tuple(sorted(row[2])))
        df_collapsed_matrix_dublicate_check_zebrafish.append(tuple(sorted(row[3])))
        df_collapsed_matrix_accepted.append(row)
    else:
        pass


## create dataframe from collapsed matrix of accepted ortholog transporter entries ##
df = pd.DataFrame(df_collapsed_matrix_accepted, columns =['Rat ID', 'Human ID', 'Mouse ID', 'Zebrafish ID'])


## Genes convertion functions ##
func_rat_genes = lambda x: [rat_genes_dict.get(y,y) for y in x]
func_human_genes = lambda x: [human_genes_dict.get(y,y) for y in x]
func_mouse_genes = lambda x: [mouse_genes_dict.get(y,y) for y in x]
func_zebrafish_genes = lambda x: [zebrafish_genes_dict.get(y,y) for y in x]

## TPM convertion functions ##
func_rat_TPM = lambda x: [rat_TPM_dict.get(y,y) for y in x]
func_human_TPM = lambda x: [human_TPM_dict.get(y,y) for y in x]
func_mouse_TPM = lambda x: [mouse_TPM_dict.get(y,y) for y in x]
func_zebrafish_TPM = lambda x: [zebrafish_TPM_dict.get(y,y) for y in x]


# Rat genes #
df['Rat genes'] = df['Rat ID']
df['Rat genes'] = df['Rat genes'].apply(func_rat_genes)

# Human genes #
df['Human genes'] = df['Human ID']
df['Human genes'] = df['Human genes'].apply(func_human_genes)
# Mouse genes #
df['Mouse genes'] = df['Mouse ID']
df['Mouse genes'] = df['Mouse genes'].apply(func_mouse_genes)
# Zebrafish genes #
df['Zebrafish genes'] = df['Zebrafish ID']
df['Zebrafish genes'] = df['Zebrafish genes'].apply(func_zebrafish_genes)

# Rat TPM #
df['Rat TPM'] = df['Rat ID']
df['Rat TPM'] = df['Rat TPM'].apply(func_rat_TPM)
# Human TPM #
df['Human TPM'] = df['Human ID']
df['Human TPM'] = df['Human TPM'].apply(func_human_TPM)
# Mouse TPM #
df['Mouse TPM'] = df['Mouse ID']
df['Mouse TPM'] = df['Mouse TPM'].apply(func_mouse_TPM)
# Zebrafish TPM #
df['Zebrafish TPM'] = df['Zebrafish ID']
df['Zebrafish TPM'] = df['Zebrafish TPM'].apply(func_zebrafish_TPM)


## Convert to string -> save dataframe to file ##

# Ensembl ids #
df['Rat ID'] = df['Rat ID'].str.join("|")
df['Human ID'] = df['Human ID'].str.join("|")
df['Mouse ID'] = df['Mouse ID'].str.join("|")
df['Zebrafish ID'] = df['Zebrafish ID'].str.join("|")

# Genes #
df['Rat genes'] = df['Rat genes'].str.join("|")
df['Human genes'] = df['Human genes'].str.join("|")
df['Mouse genes'] = df['Mouse genes'].str.join("|")
df['Zebrafish genes'] = df['Zebrafish genes'].str.join("|")

# TPM #
df['Rat TPM'] = df['Rat TPM'].apply(lambda x: "|".join(map(str, x)))
df['Human TPM'] = df['Human TPM'].apply(lambda x: "|".join(map(str, x)))
df['Mouse TPM'] = df['Mouse TPM'].apply(lambda x: "|".join(map(str, x)))
df['Zebrafish TPM'] = df['Zebrafish TPM'].apply(lambda x: "|".join(map(str, x)))

df = df[['Rat ID','Rat genes', 'Rat TPM','Human ID','Human genes', 'Human TPM','Mouse ID','Mouse genes', 'Mouse TPM','Zebrafish ID','Zebrafish genes', 'Zebrafish TPM']]

df.to_excel(os.path.join(folder3,Collapsed_ortholog_matrix),index=False)
