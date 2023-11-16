# -*- coding: utf-8 -*-

## Libraries ##

import os
import pandas as pd

## Folders ##

folder1 = "Data/Biomart"
folder2 = "Data/Count tables/All genes"
folder3 = "Data/Count tables/Ortholog genes"
folder4 = "Data/Gene lists/All genes"
folder5 = "Data/Bar matrices"

os.makedirs(folder5,exist_ok=True)

## Files ##

# Count tables (all genes) #
human_file_count_table = "Human_count_table_all.csv"
rat_file_count_table = "Rat_count_table_all.csv"
mouse_file_count_table = "Mouse_count_table_all.csv"
zebrafish_file_count_table = "Zebrafish_count_table_all.csv"

# Count tables (orthologous genes)
human_file_count_table_ortholog = "Human_count_table_ortholog.csv"
rat_file_count_table_ortholog = "Rat_count_table_ortholog.csv"
mouse_file_count_table_ortholog = "Mouse_count_table_ortholog.csv"
zebrafish_file_count_table_ortholog = "Zebrafish_count_table_ortholog.csv"

# gene lists (shared) #
human_file_shared = "Shared_orthologues_gene_in_all_species_list_Human.csv"
rat_file_shared = "Shared_orthologues_gene_in_all_species_list_Rat.csv"
mouse_file_shared = "Shared_orthologues_gene_in_all_species_list_Mouse.csv"
zebrafish_file_shared = "Shared_orthologues_gene_in_all_species_list_Zebrafish.csv"

# Output files #
File_bar_matrix = "Bar Matrix.csv"
File_bar_matrix_stacked = "Bar Matrix stacked.csv"

### Load data ###

# Count tables - all genes #
df_human = pd.read_csv(os.path.join(folder2,human_file_count_table),sep=";")
df_rat = pd.read_csv(os.path.join(folder2,rat_file_count_table),sep=";")
df_mouse = pd.read_csv(os.path.join(folder2,mouse_file_count_table),sep=";")
df_zebrafish = pd.read_csv(os.path.join(folder2,zebrafish_file_count_table),sep=";")

# Count tables - orthologous genes #
df_human_ortholog = pd.read_csv(os.path.join(folder3,human_file_count_table_ortholog),sep=";")
df_rat_ortholog = pd.read_csv(os.path.join(folder3,rat_file_count_table_ortholog),sep=";")
df_mouse_ortholog = pd.read_csv(os.path.join(folder3,mouse_file_count_table_ortholog),sep=";")
df_zebrafish_ortholog = pd.read_csv(os.path.join(folder3,zebrafish_file_count_table_ortholog),sep=";")

# Shared genes #
df_human_shared = pd.read_csv(os.path.join(folder4,human_file_shared),sep=";")
df_rat_shared = pd.read_csv(os.path.join(folder4,rat_file_shared),sep=";")
df_mouse_shared = pd.read_csv(os.path.join(folder4,mouse_file_shared),sep=";")
df_zebrafish_shared = pd.read_csv(os.path.join(folder4,zebrafish_file_shared),sep=";")

## Create variables of counts ##
# All genes (Count tables) #
Count_human_all = len(df_human)
Count_rat_all  = len(df_rat)
Count_mouse_all  = len(df_mouse)
Count_zebrafish_all  = len(df_zebrafish)
# orthologues genes #
Count_human_ortholog = len(df_human_ortholog)
Count_rat_ortholog  = len(df_rat_ortholog)
Count_mouse_ortholog  = len(df_mouse_ortholog)
Count_zebrafish_ortholog  = len(df_zebrafish_ortholog)
# Shared genes #
Count_human_shared = len(df_human_shared)
Count_rat_shared = len(df_rat_shared)
Count_mouse_shared = len(df_mouse_shared)
Count_zebrafish_shared = len(df_zebrafish_shared)

with open(os.path.join(folder5,File_bar_matrix),'w+') as out:
    out.write(";Protein coding;Orthologues genes;Shared genes in all species\n")
    out.write("Human;{};{};{}\n".format(str(Count_human_all),str(Count_human_ortholog),str(Count_human_shared)))
    out.write("Rat;{};{};{}\n".format(str(Count_rat_all),str(Count_rat_ortholog),str(Count_rat_shared)))
    out.write("Mouse;{};{};{}\n".format(str(Count_mouse_all),str(Count_mouse_ortholog),str(Count_mouse_shared)))
    out.write("Zebrafish;{};{};{}\n".format(str(Count_zebrafish_all),str(Count_zebrafish_ortholog),str(Count_zebrafish_shared)))
out.close()


Stacked_value1_human = str(Count_human_shared)
Stacked_value2_human = str(Count_human_ortholog-int(Stacked_value1_human))
Stacked_value3_human = str(Count_human_all-int(Stacked_value1_human)-int(Stacked_value2_human))

Stacked_value1_rat = str(Count_rat_shared)
Stacked_value2_rat = str(Count_rat_ortholog-int(Stacked_value1_rat))
Stacked_value3_rat = str(Count_rat_all-int(Stacked_value1_rat)-int(Stacked_value2_rat))

Stacked_value1_mouse = str(Count_mouse_shared)
Stacked_value2_mouse = str(Count_mouse_ortholog-int(Stacked_value1_mouse))
Stacked_value3_mouse = str(Count_mouse_all-int(Stacked_value1_mouse)-int(Stacked_value2_mouse))

Stacked_value1_zebrafish = str(Count_zebrafish_shared)
Stacked_value2_zebrafish = str(Count_zebrafish_ortholog-int(Stacked_value1_zebrafish))
Stacked_value3_zebrafish = str(Count_zebrafish_all-int(Stacked_value1_zebrafish)-int(Stacked_value2_zebrafish))

with open(os.path.join(folder5,File_bar_matrix_stacked),'w+') as out:
    out.write("Species;Shared genes in all species;Orthologues genes;Protein coding\n")
    out.write("Human;{};{};{}\n".format(Stacked_value1_human,Stacked_value2_human,Stacked_value3_human))
    out.write("Rat;{};{};{}\n".format(Stacked_value1_rat,Stacked_value2_rat,Stacked_value3_rat))
    out.write("Mouse;{};{};{}\n".format(Stacked_value1_mouse,Stacked_value2_mouse,Stacked_value3_mouse))
    out.write("Zebrafish;{};{};{}\n".format(Stacked_value1_zebrafish,Stacked_value2_zebrafish,Stacked_value3_zebrafish))
out.close()

