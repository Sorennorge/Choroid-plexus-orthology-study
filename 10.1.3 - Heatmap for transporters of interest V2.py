# -*- coding: utf-8 -*-

### Heatmap for transporters of interest ###

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import ListedColormap
from matplotlib.cm import register_cmap
import seaborn as sns

# Program input #
sns.set(font_scale=6)
Top_rank = 20
Save_or_show = 1 # if not 1 the program will just show figures #
n_bins = 100 # colors
v_max = 90
font_size_label = 50
font_size_cbar = 40

## Folders ##

Folder1 = "Results/Transport - orthologeus"
Folder2 = "Results/Images_new/transport of interest"
os.makedirs(Folder2,exist_ok=True)
folder_cmap = "Data/Cmap/Transport of interest"
os.makedirs(folder_cmap,exist_ok=True)


## Files ##

# set wanted file #

#File = "Transport of interest - Rank sorted.xlsx"
File = "Transport of interest - naturally sorted.xlsx"
# Output files #
File_out = "Heatmap_transport_of_interest.png"


## Load data ##

## Complete datafram ##
df = pd.read_excel(os.path.join(Folder1,File))

## Subset human ##
df_human = df[['Gene_Alias','Human Rank','Human TPM (Rank)']]
df_human = df_human.set_index(['Gene_Alias'])


## Subset rat ##
df_rat = df[['Gene_Alias','Rat Rank','Rat TPM (Rank)']]


## Subset mouse ##
df_mouse = df[['Gene_Alias','Mouse Rank','Mouse TPM (Rank)']]
df_mouse = df_mouse.set_index(['Gene_Alias'])


## Subset zebrafish ##
df_zebrafish = df[['Gene_Alias','Zebrafish Rank','Zebrafish TPM (Rank)']]
df_zebrafish = df_zebrafish.set_index(['Gene_Alias'])

## Colors ##

## Colors ##
Human_color = "#CF67E2"
Rat_color = "#91EB91"
Mouse_color = "#A7A7A7"
Zebrafish_color = "#A7DBF0"
white = "#FFFFFF"

Human_RGB = to_rgba(Human_color)
Rat_RGB = to_rgba(Rat_color)
Mouse_RGB = to_rgba(Mouse_color)
Zebrafish_RGB = to_rgba(Zebrafish_color)
white_RGB = to_rgba(white)

colors_human = [Human_RGB,white_RGB]
colors_rat = [Rat_RGB,white_RGB]
colors_mouse = [Mouse_RGB,white_RGB]
colors_zebrafish = [Zebrafish_RGB,white_RGB]

cmap_human = LinearSegmentedColormap.from_list("cmap_name", colors_human, N=n_bins)
cmap_rat = LinearSegmentedColormap.from_list("cmap_name", colors_rat, N=n_bins)
cmap_mouse = LinearSegmentedColormap.from_list("cmap_name", colors_mouse, N=n_bins)
cmap_zebrafish = LinearSegmentedColormap.from_list("cmap_name", colors_zebrafish, N=n_bins)

fig = plt.figure(figsize=(20,20))
fmt_value = '.0%'
fmt_value_TT = ".0f"

gs = fig.add_gridspec(6,8,width_ratios=[1,1,1,1,0.25,0.15,0.5,0.15],height_ratios=[1,1,1,1,0,0],hspace=0,wspace=0)
ax1 = fig.add_subplot(gs[:-1, 0])
ax2 = fig.add_subplot(gs[:-1, 1])
ax3 = fig.add_subplot(gs[:-1, 2])
ax4 = fig.add_subplot(gs[:-1, 3])
ax5 = fig.add_subplot(gs[:-1, 4])
ax5.set_visible(False)
ax7 = fig.add_subplot(gs[:-1, 6])
ax7.set_visible(False)

# color bars 
gs2 = gs[:-1, 5].subgridspec(4, 1,height_ratios=[0.05,1,1,0.05], hspace=0.1, wspace=0)
ax_top_padding = fig.add_subplot(gs2[0, 0])
ax_C1 = fig.add_subplot(gs2[1, 0])
ax_C2 = fig.add_subplot(gs2[2, 0])

ax_bottom_padding = fig.add_subplot(gs2[3, 0])

gs3 = gs[:-1, 7].subgridspec(4, 1,height_ratios=[0.05,1,1,0.05], hspace=0.1, wspace=0)
ax_top_padding_2 = fig.add_subplot(gs3[0, 0])
ax_C3 = fig.add_subplot(gs3[1, 0])
ax_C4 = fig.add_subplot(gs3[2, 0])
ax_bottom_padding_2 = fig.add_subplot(gs3[3, 0])

# Human #
sns.heatmap(df_human[['Human Rank']],cbar=False,
                 annot_kws={'color':'black',"fontsize":font_size_label},
                 cbar_kws={"shrink": .25},
                 linecolor='black',linewidths=1.5,
                 clip_on=False,
                 fmt='',                 
                 annot=df_human[['Human TPM (Rank)']],
                 cmap=cmap_human,
                 vmin=1, vmax=v_max,ax=ax1)


# Rat #
sns.heatmap(df_rat[['Rat Rank']],cbar=False,
                 annot_kws={'color':'black',"fontsize":font_size_label},
                 linecolor='black',linewidths=1.5,
                 clip_on=False,
                 fmt='',
                 annot=df_rat[['Rat TPM (Rank)']],
                 cmap=cmap_rat,
                 vmin=1, vmax=v_max,ax=ax2)

# Mouse #
sns.heatmap(df_mouse[['Mouse Rank']],cbar=False,
                 annot_kws={'color':'black',"fontsize":font_size_label},
                 linecolor='black',linewidths=1.5,
                 clip_on=False,
                 fmt='',
                 annot=df_mouse[['Mouse TPM (Rank)']],
                 cmap=cmap_mouse,
                 vmin=1, vmax=v_max,ax=ax3)

# Zebrafish #
sns.heatmap(df_zebrafish[['Zebrafish Rank']],cbar=False,
                 annot_kws={'color':'black',"fontsize":font_size_label},
                 linecolor='black',linewidths=1.5,
                 clip_on=False,
                 fmt='',
                 annot=df_zebrafish[['Zebrafish TPM (Rank)']],
                 cmap=cmap_zebrafish,
                 vmin=1, vmax=v_max,ax=ax4)


# ylabels #
ax1.set_ylabel('')
ax2.set_ylabel('')
ax3.set_ylabel('')
ax4.set_ylabel('')

# xlabels #
ax1.set_xticks([])
ax2.set_xticks([])
ax3.set_xticks([])
ax4.set_xticks([])

# remove genes -> yticks #
ax2.set_yticks([])
ax3.set_yticks([])
ax4.set_yticks([])
# Add some padding for the labels #
ax1.tick_params(axis='y', pad=30)

# Color bars #
cbar1 = fig.colorbar(ax1.get_children()[0], ax=ax_C1, cax=ax_C1,orientation="vertical",ticks=[1,10,20,30,40,50,60,70,80])
cbar1.ax.invert_yaxis()
cbar1.outline.set_color('Black')
cbar1.outline.set_linewidth(2)
cbar1.ax.tick_params(axis='y', labelsize=font_size_cbar)


cbar2 = fig.colorbar(ax2.get_children()[0], ax=ax_C2, cax=ax_C2,orientation="vertical",ticks=[1,10,20,30,40,50,60,70,80])
cbar2.ax.invert_yaxis()
cbar2.outline.set_color('Black')
cbar2.outline.set_linewidth(2)
cbar2.ax.tick_params(axis='y', labelsize=font_size_cbar)


cbar3 = fig.colorbar(ax3.get_children()[0], ax=ax_C3, cax=ax_C3,orientation="vertical",ticks=[1,10,20,30,40,50,60,70,80])
cbar3.ax.invert_yaxis()
cbar3.outline.set_color('Black')
cbar3.outline.set_linewidth(2)
cbar3.ax.tick_params(axis='y', labelsize=font_size_cbar)


cbar4 = fig.colorbar(ax4.get_children()[0], ax=ax_C4, cax=ax_C4,orientation="vertical",ticks=[1,10,20,30,40,50,60,70,80])
cbar4.ax.invert_yaxis()
cbar4.outline.set_color('Black')
cbar4.outline.set_linewidth(2)
cbar4.ax.tick_params(axis='y', labelsize=font_size_cbar)

cbar_top = fig.delaxes(ax=ax_top_padding)
cbar_bottom = fig.delaxes(ax=ax_bottom_padding)
cbar_top_2 = fig.delaxes(ax=ax_top_padding_2)
cbar_bottom_2 = fig.delaxes(ax=ax_bottom_padding_2)

if Save_or_show == 1:
    plt.savefig(os.path.join(Folder2,File_out),dpi=600,bbox_inches='tight')
else:
    plt.show()
