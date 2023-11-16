# -*- coding: utf-8 -*-

### Heatmap for transporters of interest ###

import os
import seaborn as sns 
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.cm import register_cmap
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Program input #
sns.set(font_scale=2,style='white')
Save_or_show = 1 # if not 1 the program will just show figures #
tick_array = [1,10,20,30,40,50,60,70,80]
max_value_palette = 90

## Folders ##

Folder1 = "Results/Transport - orthologeus"
Folder2 = "Results/Images_new/transport of interest"
os.makedirs(Folder2,exist_ok=True)
folder_cmap = "Data/Cmap/Transport of interest"
os.makedirs(folder_cmap,exist_ok=True)


## Files ##

# set wanted file #

File = "Transport of interest - Rank sorted.xlsx"
# Output files #
File_out1 = "Heatmap_Human_ranksort.png"
File_out2 = "Heatmap_Rat_ranksort.png"
File_out3 = "Heatmap_Mouse_ranksort.png"
File_out4 = "Heatmap_Zebrafish_ranksort.png"

## Load data ##

## Complete datafram ##
df = pd.read_excel(os.path.join(Folder1,File))

## Subset human ##
df_human = df[['Gene_Alias','Human Rank']]
df_human = df_human.set_index(['Gene_Alias'])
# generate label array for heatmap #
human_labels_anno = df['Human TPM (Rank)'].to_list()
human_labels_anno_correct = []
for key in human_labels_anno:
    human_labels_anno_correct.append([key])
human_labels_anno_correct = np.array(human_labels_anno_correct,dtype=str)

## Subset rat ##
df_rat = df[['Gene_Alias','Rat Rank']]
df_rat = df_rat.set_index(['Gene_Alias'])
# generate label array for heatmap #
rat_labels_anno = df['Rat TPM (Rank)'].to_list()
rat_labels_anno_correct = []
for key in rat_labels_anno:
    rat_labels_anno_correct.append([key])
rat_labels_anno_correct = np.array(rat_labels_anno_correct,dtype=str)

## Subset mouse ##
df_mouse = df[['Gene_Alias','Mouse Rank']]
df_mouse = df_mouse.set_index(['Gene_Alias'])
# generate label array for heatmap #
mouse_labels_anno = df['Mouse TPM (Rank)'].to_list()
mouse_labels_anno_correct = []
for key in mouse_labels_anno:
    mouse_labels_anno_correct.append([key])
mouse_labels_anno_correct = np.array(mouse_labels_anno_correct,dtype=str)

## Subset zebrafish ##
df_zebrafish = df[['Gene_Alias','Zebrafish Rank']]
df_zebrafish = df_zebrafish.set_index(['Gene_Alias'])
# generate label array for heatmap #
zebrafish_labels_anno = df['Zebrafish TPM (Rank)'].to_list()
zebrafish_labels_anno_correct = []
for key in zebrafish_labels_anno:
    zebrafish_labels_anno_correct.append([key])
zebrafish_labels_anno_correct = np.array(zebrafish_labels_anno_correct,dtype=str)

## Colors ##

# From their dark (normal) -> white #
Human_color = ["#CF67E2","#ffffff"]
#Human_color.reverse()
Rat_color = ["#91EB91","#ffffff",]
#Rat_color.reverse()
Mouse_color = ["#A7A7A7","#ffffff"]
#Mouse_color.reverse()
Zebrafish_color = ["#A7DBF0","#ffffff"]
#Zebrafish_color.reverse()

## relative positions of colors in cmap/palette ##
pos = [0.0,1.0]

## Human ##
Color = Human_color
cmap = LinearSegmentedColormap.from_list("", list(zip(pos, Color)))
register_cmap(os.path.join(folder_cmap,"Human_cmap"), cmap)

palette= sns.color_palette(os.path.join(folder_cmap,"Human_cmap"),n_colors=max_value_palette)

plt.figure(figsize=(2,10))
p1 = sns.heatmap(df_human,cbar=True,annot_kws={'color':'black',"fontsize":20},
                 cbar_kws={"shrink": .3,'ticks':tick_array},
                 linecolor='black',linewidths=1.5,clip_on=False,
                 vmin=1,
                 vmax=max_value_palette,
                 fmt='4',annot=human_labels_anno_correct,cmap=palette)
plt.ylabel('')
p1.set(xticklabels=[])
p1.set(xlabel=None)
plt.gcf().axes[1].invert_yaxis()
if Save_or_show == 1:
    plt.savefig(os.path.join(Folder2,File_out1),dpi=600,bbox_inches='tight')
else:
    plt.show()

## Rat ##
Color = Rat_color
cmap = LinearSegmentedColormap.from_list("", list(zip(pos, Color)))
register_cmap(os.path.join(folder_cmap,"Rat_cmap"), cmap)

palette= sns.color_palette(os.path.join(folder_cmap,"Rat_cmap"),n_colors=max_value_palette)

plt.figure(figsize=(2,10))
p2 = sns.heatmap(df_rat,cbar=True,annot_kws={'color':'black',"fontsize":20},
                 cbar_kws={"shrink": .3,'ticks':tick_array},
                 linecolor='black',linewidths=1.5,clip_on=False,
                 vmin=1,
                 vmax=max_value_palette,
                 fmt='',annot=rat_labels_anno_correct,cmap=palette)
plt.ylabel('')
p2.set(xticklabels=[])
p2.set(xlabel=None)
plt.gcf().axes[1].invert_yaxis()
if Save_or_show == 1:
    plt.savefig(os.path.join(Folder2,File_out2),dpi=600,bbox_inches='tight')
else:
    plt.show()

## Mouse ##
Color = Mouse_color
cmap = LinearSegmentedColormap.from_list("", list(zip(pos, Color)))
register_cmap(os.path.join(folder_cmap,"Mouse_cmap"), cmap)

palette= sns.color_palette(os.path.join(folder_cmap,"Mouse_cmap"),n_colors=max_value_palette)

plt.figure(figsize=(2,10))
p3 = sns.heatmap(df_mouse,cbar=True,annot_kws={'color':'black',"fontsize":20},
                 cbar_kws={"shrink": .3,'ticks':tick_array},
                 vmin=1,
                 vmax=max_value_palette,
                 linecolor='black',linewidths=1.5,clip_on=False,
                 fmt='',annot=mouse_labels_anno_correct,cmap=palette)
plt.ylabel('')
p3.set(xticklabels=[])
p3.set(xlabel=None)
plt.gcf().axes[1].invert_yaxis()
if Save_or_show == 1:
    plt.savefig(os.path.join(Folder2,File_out3),dpi=600,bbox_inches='tight')
else:
    plt.show()
    
## Zebrafish ##
Color = Zebrafish_color
cmap = LinearSegmentedColormap.from_list("", list(zip(pos, Color)))
register_cmap(os.path.join(folder_cmap,"Zebrafish_cmap"), cmap)

palette= sns.color_palette(os.path.join(folder_cmap,"Zebrafish_cmap"),n_colors=max_value_palette)

plt.figure(figsize=(2,10))
p4 = sns.heatmap(df_zebrafish,cbar=True,annot_kws={'color':'black',"fontsize":20},
                 cbar_kws={"shrink": .3,'ticks':tick_array},
                 linecolor='black',linewidths=1.5,clip_on=False,
                 vmin=1,
                 vmax=max_value_palette,
                 fmt='',annot=zebrafish_labels_anno_correct,cmap=palette)
plt.ylabel('')
p4.set(xticklabels=[])
p4.set(xlabel=None)
plt.gcf().axes[1].invert_yaxis()
if Save_or_show == 1:
    plt.savefig(os.path.join(Folder2,File_out4),dpi=600,bbox_inches='tight')
else:
    plt.show()