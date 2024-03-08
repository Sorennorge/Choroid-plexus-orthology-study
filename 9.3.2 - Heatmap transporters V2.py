# -*- coding: utf-8 -*-

### Heatmap transporters ###

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import ListedColormap
from matplotlib.cm import register_cmap
import seaborn as sns

# Program input #

#sns.set(font_scale=2,style='white')
Top_rank = 20
Save_or_show = 1 # if not 1 the program will just show figures #
n_bins = 100 # colors
v_max = 90
font_size_label = 60

# folders #

folder = "Results/Transport - orthologeus"
folder2 = "Results/Images_new"
os.makedirs(folder2,exist_ok=True)
#folder_cmap = "Data/Cmap"
#os.makedirs(folder_cmap,exist_ok=True)

## Files ##

file = "Transport Ranked overview matrix version 2.xlsx"
file2 = "Transport overview matrix.xlsx"

File_out1 = "Heatmap_All_transporters.png"

## Load data ##

df = pd.read_excel(os.path.join(folder,file),nrows=Top_rank,index_col=False)
df_TPM = pd.read_excel(os.path.join(folder,file2),nrows=Top_rank,index_col=False)

# Create TPM matrix and index Merged_Gene_Alias #
df_index_conversion = df[['Human ID','Merged_Gene_Alias']]
TPM_df_ = pd.concat([df_index_conversion.set_index('Human ID'),df_TPM.set_index('Human ID')[[
    'Human TPM sum','Rat TPM sum','Mouse TPM sum','Zebrafish TPM sum']]],axis=1)
TPM_df_ = TPM_df_.set_index('Merged_Gene_Alias')

df_human = df[['Merged_Gene_Alias','Human Rank']]
df_human = df_human.rename(columns=({"Human Rank":"Human"}))
df_human = df_human.set_index(['Merged_Gene_Alias'])

df_rat = df[['Merged_Gene_Alias','Rat Rank']]
df_rat = df_rat.rename(columns=({"Rat Rank":"Rat"}))
df_rat = df_rat.set_index(['Merged_Gene_Alias'])

df_mouse = df[['Merged_Gene_Alias','Mouse Rank']]
df_mouse = df_mouse.rename(columns=({"Mouse Rank":"Mouse"}))
df_mouse = df_mouse.set_index(['Merged_Gene_Alias'])

df_zebrafish = df[['Merged_Gene_Alias','Zebrafish Rank']]
df_zebrafish = df_zebrafish.rename(columns=({"Zebrafish Rank":"Zebrafish"}))
df_zebrafish = df_zebrafish.set_index(['Merged_Gene_Alias'])

df_human = pd.concat([df_human,TPM_df_[['Human TPM sum']]],axis=1)
df_human['Human TPM sum'] = df_human['Human TPM sum'].round()
df_human['Label'] = df_human[['Human','Human TPM sum']].apply(lambda x : '{} ({})'.format(int(x[0]),int(x[1])), axis=1)

df_rat = pd.concat([df_rat,TPM_df_[['Rat TPM sum']]],axis=1)
df_rat['Rat TPM sum'] = df_rat['Rat TPM sum'].round()
df_rat['Label'] = df_rat[['Rat','Rat TPM sum']].apply(lambda x : '{} ({})'.format(int(x[0]),int(x[1])), axis=1)

df_mouse = pd.concat([df_mouse,TPM_df_[['Mouse TPM sum']]],axis=1)
df_mouse['Mouse TPM sum'] = df_mouse['Mouse TPM sum'].round()
df_mouse['Label'] = df_mouse[['Mouse','Mouse TPM sum']].apply(lambda x : '{} ({})'.format(int(x[0]),int(x[1])), axis=1)

df_zebrafish = pd.concat([df_zebrafish,TPM_df_[['Zebrafish TPM sum']]],axis=1)
df_zebrafish['Zebrafish TPM sum'] = df_zebrafish['Zebrafish TPM sum'].round()
df_zebrafish['Label'] = df_zebrafish[['Zebrafish','Zebrafish TPM sum']].apply(lambda x : '{} ({})'.format(int(x[0]),int(x[1])), axis=1)

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

sns.set(font_scale=6)
fig = plt.figure(figsize=(20,80))
fmt_value = '.0%'
fmt_value_TT = ".0f"

gs = fig.add_gridspec(6,6,width_ratios=[1,1,1,1,0.25,0.25],height_ratios=[1,1,1,1,0,0],hspace=0,wspace=0)
ax1 = fig.add_subplot(gs[:-1, 0])
ax2 = fig.add_subplot(gs[:-1, 1])
ax3 = fig.add_subplot(gs[:-1, 2])
ax4 = fig.add_subplot(gs[:-1, 3])
ax5 = fig.add_subplot(gs[:-1, 4])
ax5.set_visible(False)

# color bars 
gs2 = gs[:-1, 5].subgridspec(6, 1,height_ratios=[0.05,1,1,1,1,0.05], hspace=0.1, wspace=0)
ax_top_padding = fig.add_subplot(gs2[0, 0])
ax_C1 = fig.add_subplot(gs2[1, 0])
ax_C2 = fig.add_subplot(gs2[2, 0])
ax_C3 = fig.add_subplot(gs2[3, 0])
ax_C4 = fig.add_subplot(gs2[4, 0])
ax_bottom_padding = fig.add_subplot(gs2[5, 0])


# Human #
sns.heatmap(df_human[['Human']],cbar=False,
                 annot_kws={'color':'black',"fontsize":font_size_label},
                 cbar_kws={"shrink": .25},
                 linecolor='black',linewidths=1.5,
                 clip_on=False,
                 fmt='',                 
                 annot=df_human[['Label']],
                 cmap=cmap_human,
                 vmin=1, vmax=v_max,ax=ax1)


# Rat #
sns.heatmap(df_rat[['Rat']],cbar=False,
                 annot_kws={'color':'black',"fontsize":font_size_label},
                 linecolor='black',linewidths=1.5,
                 clip_on=False,
                 fmt='',
                 annot=df_rat[['Label']],
                 cmap=cmap_rat,
                 vmin=1, vmax=v_max,ax=ax2)

# Mouse #
sns.heatmap(df_mouse[['Mouse']],cbar=False,
                 annot_kws={'color':'black',"fontsize":font_size_label},
                 linecolor='black',linewidths=1.5,
                 clip_on=False,
                 fmt='',
                 annot=df_mouse[['Label']],
                 cmap=cmap_mouse,
                 vmin=1, vmax=v_max,ax=ax3)

# Zebrafish #
sns.heatmap(df_zebrafish[['Zebrafish']],cbar=False,
                 annot_kws={'color':'black',"fontsize":font_size_label},
                 linecolor='black',linewidths=1.5,
                 clip_on=False,
                 fmt='',
                 annot=df_zebrafish[['Label']],
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



cbar2 = fig.colorbar(ax2.get_children()[0], ax=ax_C2, cax=ax_C2,orientation="vertical",ticks=[1,10,20,30,40,50,60,70,80])
cbar2.ax.invert_yaxis()
cbar2.outline.set_color('Black')
cbar2.outline.set_linewidth(2)


cbar3 = fig.colorbar(ax3.get_children()[0], ax=ax_C3, cax=ax_C3,orientation="vertical",ticks=[1,10,20,30,40,50,60,70,80])
cbar3.ax.invert_yaxis()
cbar3.outline.set_color('Black')
cbar3.outline.set_linewidth(2)


cbar4 = fig.colorbar(ax4.get_children()[0], ax=ax_C4, cax=ax_C4,orientation="vertical",ticks=[1,10,20,30,40,50,60,70,80])
cbar4.ax.invert_yaxis()
cbar4.outline.set_color('Black')
cbar4.outline.set_linewidth(2)

cbar_top = fig.delaxes(ax=ax_top_padding)
cbar_top = fig.delaxes(ax=ax_bottom_padding)

if Save_or_show == 1:
    plt.savefig(os.path.join(folder2,File_out1),dpi=600,bbox_inches='tight')
else:
    plt.show()
