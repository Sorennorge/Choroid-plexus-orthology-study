# -*- coding: utf-8 -*-

### Transport matrix sum and rank ###

## Libraries ##

import os
import pandas as pd
import numpy as np

## Folders ##

folder1 = "Data/Biomart orthologs/Merged orthology matrix"
folder2 = "Results/Transport - orthologeus"
os.makedirs(folder2, exist_ok=True)

## Files ##
Collapsed_ortholog_matrix = "Collapsed Transport ortholog matrix.xlsx"

Transport_overview_file = "Transport overview matrix.xlsx"
Transport_Ranked_overview_file = "Transport Ranked overview matrix.xlsx"

## Load data ##

Transport_matrix = pd.read_excel(os.path.join(folder1,Collapsed_ortholog_matrix))

## Create sum and rank for individual species ##

# Create rat matrix #
Rat_matrix = Transport_matrix[['Rat ID','Rat genes','Rat TPM']].copy()
Rat_matrix['Rat TPM float'] = Rat_matrix['Rat TPM'].str.split("|")
Rat_matrix['Rat TPM float'] = Rat_matrix['Rat TPM float'].apply(lambda x: [float(i) for i in x])
# Add sum #
Rat_matrix['Rat TPM sum'] = Rat_matrix['Rat TPM float'].apply(lambda x: np.sum(x))
# Sort by sum and add Rank #
Rat_matrix = Rat_matrix.sort_values(by='Rat TPM sum',ascending=False).reset_index(drop=True)
Rat_matrix['Rat Rank'] = Rat_matrix['Rat TPM sum'].rank(method = 'first',ascending=False)

# Create Human matrix #
Human_matrix = Transport_matrix[['Human ID','Human genes','Human TPM']].copy()
Human_matrix['Human TPM float'] = Human_matrix['Human TPM'].str.split("|")
Human_matrix['Human TPM float'] = Human_matrix['Human TPM float'].apply(lambda x: [float(i) for i in x])
# Add sum #
Human_matrix['Human TPM sum'] = Human_matrix['Human TPM float'].apply(lambda x: np.sum(x))
# Sort by sum and add Rank #
Human_matrix = Human_matrix.sort_values(by='Human TPM sum',ascending=False).reset_index(drop=True)
Human_matrix['Human Rank'] = Human_matrix['Human TPM sum'].rank(method = 'first',ascending=False)

# Create Mouse matrix #
Mouse_matrix = Transport_matrix[['Mouse ID','Mouse genes','Mouse TPM']].copy()
Mouse_matrix['Mouse TPM float'] = Mouse_matrix['Mouse TPM'].str.split("|")
Mouse_matrix['Mouse TPM float'] = Mouse_matrix['Mouse TPM float'].apply(lambda x: [float(i) for i in x])
# Add sum #
Mouse_matrix['Mouse TPM sum'] = Mouse_matrix['Mouse TPM float'].apply(lambda x: np.sum(x))
# Sort by sum and add Rank #
Mouse_matrix = Mouse_matrix.sort_values(by='Mouse TPM sum',ascending=False).reset_index(drop=True)
Mouse_matrix['Mouse Rank'] = Mouse_matrix['Mouse TPM sum'].rank(method = 'first',ascending=False)

# Create Zebrafish matrix #
Zebrafish_matrix = Transport_matrix[['Zebrafish ID','Zebrafish genes','Zebrafish TPM']].copy()
Zebrafish_matrix['Zebrafish TPM float'] = Zebrafish_matrix['Zebrafish TPM'].str.split("|")
Zebrafish_matrix['Zebrafish TPM float'] = Zebrafish_matrix['Zebrafish TPM float'].apply(lambda x: [float(i) for i in x])
# Add sum #
Zebrafish_matrix['Zebrafish TPM sum'] = Zebrafish_matrix['Zebrafish TPM float'].apply(lambda x: np.sum(x))
# Sort by sum and add Rank #
Zebrafish_matrix = Zebrafish_matrix.sort_values(by='Zebrafish TPM sum',ascending=False).reset_index(drop=True)
Zebrafish_matrix['Zebrafish Rank'] = Zebrafish_matrix['Zebrafish TPM sum'].rank(method = 'first',ascending=False)

## Create appending matrixes ##

Rat_matrix_add = Rat_matrix[['Rat ID','Rat TPM sum','Rat Rank']].set_index('Rat ID')
Human_matrix_add = Human_matrix[['Human ID','Human TPM sum','Human Rank']].set_index('Human ID')
Mouse_matrix_add = Mouse_matrix[['Mouse ID','Mouse TPM sum','Mouse Rank']].set_index('Mouse ID')
Zebrafish_matrix_add = Zebrafish_matrix[['Zebrafish ID','Zebrafish TPM sum','Zebrafish Rank']].set_index('Zebrafish ID')

## Create new dataframe for adding sum and rank ##
Transport_matrix_concatenated = Transport_matrix.copy()

## Concat dataframes ##
# Add Rat #
Transport_matrix_concatenated = pd.concat([Transport_matrix_concatenated.set_index('Rat ID'),Rat_matrix_add],join='inner',axis=1).reset_index()
# Add Human #
Transport_matrix_concatenated = pd.concat([Transport_matrix_concatenated.set_index('Human ID'),Human_matrix_add],join='inner',axis=1).reset_index()
# Add Mouse #
Transport_matrix_concatenated = pd.concat([Transport_matrix_concatenated.set_index('Mouse ID'),Mouse_matrix_add],join='inner',axis=1).reset_index()
# Add Zebrafish #
Transport_matrix_concatenated = pd.concat([Transport_matrix_concatenated.set_index('Zebrafish ID'),Zebrafish_matrix_add],join='inner',axis=1).reset_index()

## Rearrange dataframe ##

Transport_matrix_concatenated = Transport_matrix_concatenated[['Rat ID','Rat genes','Rat TPM','Rat TPM sum','Rat Rank',
                                                               'Human ID','Human genes','Human TPM','Human TPM sum','Human Rank',
                                                               'Mouse ID','Mouse genes','Mouse TPM','Mouse TPM sum','Mouse Rank',
                                                               'Zebrafish ID','Zebrafish genes','Zebrafish TPM','Zebrafish TPM sum','Zebrafish Rank']]

Transport_matrix_concatenated['Avg Rank'] = Transport_matrix_concatenated[['Rat Rank','Human Rank','Mouse Rank','Zebrafish Rank']].mean(axis=1)
#Transport_rank_check = Transport_matrix_concatenated[['Rat Rank','Human Rank','Mouse Rank','Zebrafish Rank','Avg Rank']]

Transport_matrix_concatenated = Transport_matrix_concatenated.sort_values(by='Avg Rank').reset_index(drop=True)
Transport_matrix_concatenated.to_excel(os.path.join(folder2,Transport_overview_file),sheet_name="Transport overview",index=False)

Transport_matrix_ranked_only = Transport_matrix_concatenated[['Human ID','Human genes','Human Rank','Rat genes','Rat Rank','Mouse genes','Mouse Rank','Zebrafish genes','Zebrafish Rank','Avg Rank']]
Transport_matrix_ranked_only.to_excel(os.path.join(folder2,Transport_Ranked_overview_file),sheet_name="Transport ranked overview",index=False)

