# -*- coding: utf-8 -*-

### Create bar plot ###

## Libraries ##
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

## Folders ##

folder = "Data/Bar matrices"

folder_out = "Results/Bar plot"

os.makedirs(folder_out,exist_ok=True)

## Files ##

file = "Bar Matrix stacked.csv"

file_out = "Gene overview.png"

## Create color schemes for the different species 

color_scheme1 = ["#CF67E2","#DF9BEC","#EFCEF5","#91EB91","#A7EFA7","#E3FAE3","#A7A7A7","#C8C8C8","#E9E9E9","#A7DBF0","#C0E5F4","#D9EFF8"]

color_scheme2 = []
Human_color = ["#CF67E2","#DF9BEC","#EFCEF5"]
Rat_color = ["#91EB91","#A7EFA7","#E3FAE3",]
Mouse_color = ["#A7A7A7","#C8C8C8","#E9E9E9",]
Zebrafish_color = ["#A7DBF0","#C0E5F4","#D9EFF8"]

for i in range(0,3,1):
    color_scheme2.append(Human_color[i])
    color_scheme2.append(Rat_color[i])
    color_scheme2.append(Mouse_color[i])
    color_scheme2.append(Zebrafish_color[i])

## load data - Stacked matrix ##

df = pd.read_csv(os.path.join(folder,file),sep=";")
df_sums = df[['Shared genes in all species','Orthologues genes','Protein coding']].sum(axis=1)

## Create bar plot ##
p1 = df.plot(kind='bar', x='Species',width=0.65,rot=45,figsize=(5,12),fontsize=24,stacked=True,legend=None,linewidth=1,edgecolor="k",color=color_scheme1)

# Set labels and modify #
plt.xlabel('')
plt.ylabel('Number of genes',fontsize=30)
p1.yaxis.set_label_coords(-.35, .5)
plt.xticks(rotation=45,ha='right',rotation_mode='anchor')

# Remove borders from top and right #
p1.spines['top'].set_visible(False)
p1.spines['right'].set_visible(False)

# Add ticks to y axis #
p1.yaxis.set_ticks_position('left')
p1.yaxis.set_ticks(np.arange(0, 22000, 2000))

# Add borders to bars #
for i, bar in enumerate(p1.patches):
    bar.set_color(color_scheme2[i])
    bar.set_edgecolor('k')

# Add number of genes on top of all bars #
plt.bar_label(p1.containers[2], labels=[df_sums[0],df_sums[1],df_sums[2],df_sums[3]],fontsize=24, label_type='edge')

## Show or Save figure ##
#plt.show()
plt.savefig(os.path.join(folder_out,file_out),dpi=1200,bbox_inches='tight')