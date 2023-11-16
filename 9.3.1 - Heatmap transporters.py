# -*- coding: utf-8 -*-

### Heatmap transporters ###

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.cm import register_cmap
import seaborn as sns

# Program input #
sns.set(font_scale=2,style='white')
Top_rank = 20
Save_or_show = 0 # if not 1 the program will just show figures #

# folders #

folder = "Results/Transport - orthologeus"
folder2 = "Results/Images_new"
os.makedirs(folder2,exist_ok=True)
folder_cmap = "Data/Cmap"
os.makedirs(folder_cmap,exist_ok=True)

## Files ##

file = "Transport Ranked overview matrix version 2.xlsx"

File_out1 = "Heatmap_Human.pdf"
File_out2 = "Heatmap_Rat.png"
File_out3 = "Heatmap_Mouse.png"
File_out4 = "Heatmap_Zebrafish.png"

## Load data ##

df = pd.read_excel(os.path.join(folder,file),nrows=Top_rank,index_col=False)

df_human = df[['Merged_Gene_Alias','Human Rank']]
df_human = df_human.rename(columns=({"Human Rank":"Human"}))
df_human = df_human.set_index(['Merged_Gene_Alias'])
#df_human['Human Rank'] = df_human['Human Rank'].astype(int)

df_rat = df[['Merged_Gene_Alias','Rat Rank']]
df_rat = df_rat.rename(columns=({"Rat Rank":"Rat"}))
df_rat = df_rat.set_index(['Merged_Gene_Alias'])
#df_rat['Rat Rank'] = df_rat['Rat Rank'].astype(int)


df_mouse = df[['Merged_Gene_Alias','Mouse Rank']]
df_mouse = df_mouse.rename(columns=({"Mouse Rank":"Mouse"}))
df_mouse = df_mouse.set_index(['Merged_Gene_Alias'])
#df_mouse['Mouse Rank'] = df_mouse['Mouse Rank'].astype(int)

df_zebrafish = df[['Merged_Gene_Alias','Zebrafish Rank']]
df_zebrafish = df_zebrafish.rename(columns=({"Zebrafish Rank":"Zebrafish"}))
df_zebrafish = df_zebrafish.set_index(['Merged_Gene_Alias'])
#df_zebrafish['Zebrafish Rank'] = df_zebrafish['Zebrafish Rank'].astype(int)
max_value_col_rat = df_rat[['Rat']].max()
max_value_col_human = df_human[['Human']].max()
max_value_col_mouse = df_mouse[['Mouse']].max()
max_value_col_zebrafish = df_zebrafish[['Zebrafish']].max()


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

# relative positions of colors in cmap/palette ##
pos = [0.0,1.0]
#max_value_palette = max(max_value_col_rat['Rat'],max_value_col_human['Human'],max_value_col_mouse['Mouse'],max_value_col_zebrafish['Zebrafish'])
max_value_palette = 110
## Human ##
Color = Human_color
cmap = LinearSegmentedColormap.from_list("", list(zip(pos, Color)))
register_cmap(os.path.join(folder_cmap,"cmap_human"), cmap)

#palette= sns.color_palette("my_cmap_human",n_colors=max_value_col_human['Human'])
palette= sns.color_palette(os.path.join(folder_cmap,"cmap_human"),n_colors=max_value_palette)

plt.figure(figsize=(2,20))
p1 = sns.heatmap(df_human,cbar=True,
                 annot_kws={'color':'black'},
                 cbar_kws={"shrink": .2,'ticks':[1,10,20,30,40,50,60,70,80, 90, 100]},
                 #vmax=max_value_col_human['Human'],
                 vmax=max_value_palette,
                 linecolor='black',linewidths=1.5,
                 clip_on=False,
                 fmt='g',
                 annot=True,
                 cmap=palette)
plt.ylabel('')
p1.set(xticklabels=[])
p1.set(xlabel=None)
plt.gcf().axes[1].invert_yaxis()
if Save_or_show == 1:
    plt.savefig(os.path.join(folder2,File_out1),dpi=600,bbox_inches='tight')
else:
    plt.show()

## Rat ##
Color = Rat_color
cmap = LinearSegmentedColormap.from_list("", list(zip(pos, Color)))
register_cmap(os.path.join(folder_cmap,"cmap_rat"), cmap)

#palette= sns.color_palette("my_cmap_rat",n_colors=max_value_col_rat['Rat'])
palette= sns.color_palette(os.path.join(folder_cmap,"cmap_rat"),n_colors=max_value_palette)

plt.figure(figsize=(2,20))
p2 = sns.heatmap(df_rat,cbar=True,
                 annot_kws={'color':'black'},
                 cbar_kws={"shrink": .2,'ticks':[1,10,20,30,40,50,60,70,80]},
                 #vmax=max_value_col_rat['Rat'],
                 vmax=max_value_palette,
                 linecolor='black',
                 linewidths=1.5,clip_on=False,
                 fmt='g',
                 annot=True,
                 cmap=palette)
plt.ylabel('')
p2.set(xticklabels=[])
p2.set(xlabel=None)
plt.gcf().axes[1].invert_yaxis()
if Save_or_show == 1:
    plt.savefig(os.path.join(folder2,File_out2),dpi=600,bbox_inches='tight')
else:
    plt.show()

## Mouse ##
Color = Mouse_color
cmap = LinearSegmentedColormap.from_list("", list(zip(pos, Color)))
register_cmap(os.path.join(folder_cmap,"mouse_cmap"), cmap)

#palette= sns.color_palette("my_cmap",n_colors=max_value_col_mouse['Mouse'])
palette= sns.color_palette(os.path.join(folder_cmap,"mouse_cmap"),n_colors=max_value_palette)

plt.figure(figsize=(2,20))
p3 = sns.heatmap(df_mouse,cbar=True,
                 annot_kws={'color':'black'},
                 cbar_kws={"shrink": .2,'ticks':[1,10,20,30,40,50,60,70,80]},
                 #vmax=max_value_col_mouse['Mouse'],
                 vmax=max_value_palette,
                 linecolor='black',
                 linewidths=1.5,
                 clip_on=False,
                 fmt='g',
                 annot=True,
                 cmap=palette)
plt.ylabel('')
p3.set(xticklabels=[])
p3.set(xlabel=None)
plt.gcf().axes[1].invert_yaxis()
if Save_or_show == 1:
    plt.savefig(os.path.join(folder2,File_out3),dpi=600,bbox_inches='tight')
else:
    plt.show()

## Zebrafish ##
Color = Zebrafish_color
cmap = LinearSegmentedColormap.from_list("", list(zip(pos, Color)))
register_cmap(os.path.join(folder_cmap,"Zebrafish_cmap"), cmap)

#palette= sns.color_palette("my_cmap",n_colors=max_value_col_zebrafish['Zebrafish'])
palette= sns.color_palette(os.path.join(folder_cmap,"Zebrafish_cmap"),n_colors=max_value_palette)

plt.figure(figsize=(2,20))
p3 = sns.heatmap(df_zebrafish,cbar=True,
                 annot_kws={'color':'black'},
                 cbar_kws={"shrink": .2,'ticks':[1,10,20,30,40,50,60,70,80]},
                 #vmax=max_value_col_zebrafish['Zebrafish'],
                 vmax=max_value_palette,
                 linecolor='black',
                 linewidths=1.5,
                 clip_on=False,
                 fmt='g',
                 annot=True,
                 cmap=palette)
plt.ylabel('')
p3.set(xticklabels=[])
p3.set(xlabel=None)
plt.gcf().axes[1].invert_yaxis()
if Save_or_show == 1:
    plt.savefig(os.path.join(folder2,File_out4),dpi=600,bbox_inches='tight')
else:
    plt.show()
