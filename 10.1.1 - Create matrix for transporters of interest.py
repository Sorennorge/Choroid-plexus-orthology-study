# -*- coding: utf-8 -*-

### Transport of interest ###

import os
import pandas  as pd
from natsort import natsort_keygen

## Folders ##

Folder1 = "Data/Transporter Lists"
Folder2 = "Results/Transport - orthologeus"

## Files ##

File1 = "Transport of interest.xlsx"
File2 = "Transport overview matrix.xlsx"

File3 = "Transport of interest - naturally sorted.xlsx"
File4 = "Transport of interest - Rank sorted.xlsx"

## Load data ##

df1 = pd.read_excel(os.path.join(Folder1, File1))
df2 = pd.read_excel(os.path.join(Folder2, File2))



## Concat Ensembl ID, Gene&Alias with TPM and rank ##
df3 = pd.concat([df1.set_index('Rat Ensembl ID'),df2.set_index("Rat ID")],join='inner',axis=1)
df3 = df3.sort_values(by=['Gene_Alias'],key=natsort_keygen(),ignore_index=True)
df4 = df3.sort_values(by=['Avg Rank'],ignore_index=True).copy()


df3 = df3[['Gene_Alias','Human TPM sum','Human Rank','Rat TPM sum','Rat Rank','Mouse TPM sum','Mouse Rank','Zebrafish TPM sum','Zebrafish Rank']]
df4 = df4[['Gene_Alias','Human TPM sum','Human Rank','Rat TPM sum','Rat Rank','Mouse TPM sum','Mouse Rank','Zebrafish TPM sum','Zebrafish Rank']]

## Add merged TPM and rank for label annotation ##
df3['Human TPM (Rank)'] = ['{} ({})'.format(int(round(x,0)), int(round(y,0))) for y, x in df3[['Human TPM sum', 'Human Rank']].values]
df3['Rat TPM (Rank)'] = ['{} ({})'.format(int(round(x,0)), int(round(y,0))) for y, x in df3[['Rat TPM sum', 'Rat Rank']].values]
df3['Mouse TPM (Rank)'] = ['{} ({})'.format(int(round(x,0)), int(round(y,0))) for y, x in df3[['Mouse TPM sum', 'Mouse Rank']].values]
df3['Zebrafish TPM (Rank)'] = ['{} ({})'.format(int(round(x,0)), int(round(y,0))) for y, x in df3[['Zebrafish TPM sum', 'Zebrafish Rank']].values]

df4['Human TPM (Rank)'] = ['{} ({})'.format(int(round(x,0)), int(round(y,0))) for y, x in df4[['Human TPM sum', 'Human Rank']].values]
df4['Rat TPM (Rank)'] = ['{} ({})'.format(int(round(x,0)), int(round(y,0))) for y, x in df4[['Rat TPM sum', 'Rat Rank']].values]
df4['Mouse TPM (Rank)'] = ['{} ({})'.format(int(round(x,0)), int(round(y,0))) for y, x in df4[['Mouse TPM sum', 'Mouse Rank']].values]
df4['Zebrafish TPM (Rank)'] = ['{} ({})'.format(int(round(x,0)), int(round(y,0))) for y, x in df4[['Zebrafish TPM sum', 'Zebrafish Rank']].values]

df3.to_excel(os.path.join(Folder2,File3),index=False)
df4.to_excel(os.path.join(Folder2,File4),index=False)