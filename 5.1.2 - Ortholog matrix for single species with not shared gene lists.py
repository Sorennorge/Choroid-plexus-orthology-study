# -*- coding: utf-8 -*-

### Ortholog matrix for single species (all genes) ###

## Libraries ##

import os

## functions ##

def check_exist(folder,file):
    return os.path.exists(os.path.join(folder,file))

## Folders ##

folder1 = "Data/Biomart/Ortholog matrices"
folder2 = "Data/Gene lists/Ortholog genes"
folder_out = "Data/Biomart/Ortholog genes"

os.makedirs(folder_out,exist_ok=True)

## Files ##

file_not_shared_rat = "Not_Shared_orthologues_gene_in_all_species_list_Rat.csv"
file_not_shared_human = "Not_Shared_orthologues_gene_in_all_species_list_Human.csv"
file_not_shared_zebrafish = "Not_Shared_orthologues_gene_in_all_species_list_Zebrafish.csv"
file_not_shared_mouse = "Not_Shared_orthologues_gene_in_all_species_list_Mouse.csv"

# biomart files #
# Ensembl version 104 -> Rnor_6.0
biomart_rat = "Rat_Human_Zfish_Mouse_20_09_2022.txt"
# Ensembl version 104 -> GRCh38.p13
biomart_human = "Human_Rat_Zfish_Mouse_20_09_2022.txt"
# Ensembl version 104 -> GRCz11
biomart_zebrafish = "Zfish_Rat_Human_Mouse_20_09_2022.txt"
# Ensembl version 104 -> GRCm39
biomart_mouse = "Mouse_Rat_Human_Zfish_20_09_2022.txt"


# Output file
Complete_orto_matrix_file = "Complete_Ortholog_single_species_Matrix.csv"

### Variables ###

non_shared_rat = []
non_shared_human = []
non_shared_mouse = []
non_shared_zebrafish = []

## Read files ##

# read file lengths #

with open(os.path.join(folder1,biomart_rat),'r') as read:
    for count, line in enumerate(read):
        pass
read.close()
Length_matrix_rat = int((count+1)/100)
with open(os.path.join(folder1,biomart_human),'r') as read:
    for count, line in enumerate(read):
        pass
read.close()
Length_matrix_human = int((count+1)/100)
with open(os.path.join(folder1,biomart_zebrafish),'r') as read:
    for count, line in enumerate(read):
        pass
read.close()
Length_matrix_zfish = int((count+1)/100)
with open(os.path.join(folder1,biomart_mouse),'r') as read:
    for count, line in enumerate(read):
        pass
read.close()
Length_matrix_mouse = int((count+1)/100)

## non shared gene lists for all species ##
if check_exist(folder2, file_not_shared_rat) and check_exist(folder2, file_not_shared_human) and check_exist(folder2, file_not_shared_zebrafish) and check_exist(folder2, file_not_shared_mouse):
    with open(os.path.join(folder2,file_not_shared_rat),'r') as read:
        for line in read:
            line = line.strip()
            non_shared_rat.append(line)
    read.close
    with open(os.path.join(folder2,file_not_shared_human),'r') as read:
        for line in read:
            line = line.strip()
            non_shared_human.append(line)
    read.close
    with open(os.path.join(folder2,file_not_shared_zebrafish),'r') as read:
        for line in read:
            line = line.strip()
            non_shared_zebrafish.append(line)
    read.close
    with open(os.path.join(folder2,file_not_shared_mouse),'r') as read:
        for line in read:
            line = line.strip()
            non_shared_mouse.append(line)
    read.close
else:
    print("could not find non shared files.")

## reduse entry lists ##

single_species_matrix = []

# Rat orthlog biomart #
progress_counter = 0
percentage = 0
with open(os.path.join(folder1,biomart_rat),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(",")
        #if there is a entry in rat biomart and it has an ortholog in one or more species
        if line[0] in non_shared_rat:
            if line[1] == '' and line[2] == '' and line[3] == '':
                pass
            else:
                entry = [line[0],line[1],line[2],line[3]]
                single_species_matrix.append(entry)
        else:
            pass
        # Progress counter
        if progress_counter % Length_matrix_rat == 0:
            percentage += 1
            if percentage % 10 == 0:
                print("Reading rat file - Progress: {} / 100 %".format(percentage))
        progress_counter += 1
read.close
print("Orthlog matrix length Rat: {}".format(len(single_species_matrix)))

# Human orthlog biomart #
progress_counter = 0
percentage = 0
with open(os.path.join(folder1,biomart_human),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(",")
        # if entry in the redused lists #
        if line[0] in non_shared_human:
            #if there is a entry in human biomart with all the other species add that entry
            if line[1] == '' and line[2] == '' and line[3] == '':
                pass
            else:
                entry = [line[1],line[0],line[2],line[3]]
                single_species_matrix.append(entry)
        else:
            pass
        # Progress counter
        if progress_counter % Length_matrix_human == 0:
            percentage += 1
            if percentage % 10 == 0:
                print("Reading human file - Progress: {} / 100 %".format(percentage))
        progress_counter += 1
read.close
print("Orthlog matrix length Rat+Human: {}".format(len(single_species_matrix)))

# Zebrafish orthlog biomart #
progress_counter = 0
percentage = 0
with open(os.path.join(folder1,biomart_zebrafish),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(",")
        #if there is a entry in zebrafish biomart with all the other species add that entry
        if line[0] in non_shared_zebrafish:
            if line[1] == '' and line[2] == '' and line[3] == '':
                pass
            else:
                entry = [line[1],line[2],line[0],line[3]]
                single_species_matrix.append(entry)
        else:
            pass
        # Progress counter
        if progress_counter % Length_matrix_zfish == 0:
            percentage += 1
            if percentage % 10 == 0:
                print("Reading Zfish file - Progress: {} / 100 %".format(percentage))
        progress_counter += 1
read.close
print("Orthlog matrix length Rat+Human+Zebrafish: {}".format(len(single_species_matrix)))

# mouse orthlog biomart #
progress_counter = 0
percentage = 0
with open(os.path.join(folder1,biomart_mouse),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(",")
        # if entry in the redused lists #
        if line[0] in non_shared_mouse:
            #if there is a entry in human biomart with all the other species add that entry
            if line[1] == '' and line[2] == '' and line[3] == '':
                pass
            else:
                entry = [line[1],line[2],line[3],line[0]]
                single_species_matrix.append(entry)
        else:
            pass
        # Progress counter
        if progress_counter % Length_matrix_mouse == 0:
            percentage += 1
            if percentage % 10 == 0:
                print("Reading Mouse file - Progress: {} / 100 %".format(percentage))
        progress_counter += 1
read.close
print("Orthlog matrix length Rat+Human+Zebrafish+Mouse: {}".format(len(single_species_matrix)))


# Take all the species entry from all the biomart and remove dublicates
Redused_Orthlog_mart = [list(item) for item in set(tuple(row) for row in single_species_matrix)]

# check if a error has occured and a wrong entry is present in the wrong specie
error_key = 0
for key in Redused_Orthlog_mart:
    if not key[0].startswith("ENSRNOG") and not key[0] == '':
        print(key)
        error_key = 1
        break
    if not key[1].startswith("ENSG") and not key[1] == '':
        print(key)
        error_key = 1
        break
    if not key[2].startswith("ENSDARG") and not key[2] == '':
        print(key)
        error_key = 1
        break
    if not key[3].startswith("ENSMUSG") and not key[3] == '':
        print(key)
        error_key = 1
        break
    
# Write the reduced biomart of all species to a file
if error_key == 0:
    print("saving matrix file...")
    with open(os.path.join(folder_out,Complete_orto_matrix_file),'w+') as out:
        out.write("Rat ID;Human ID;ZebraFish ID;Mouse ID\n")
        for key in Redused_Orthlog_mart:
            out.write("{}\n".format(";".join(key)))
    out.close
    print("Done.")
else:
    print("did not save due to error")

