# -*- coding: utf-8 -*-

### Biomarts orthologs - Complete matrice ###

import os

## functions ##

def check_exist(folder,file):
    return os.path.exists(os.path.join(folder,file))

## Folders ##

folder1 = "Data/Biomart/Ortholog matrices"
folder2 = "Data/Biomart"

## Files ##

# To get these files, go to ensembls biomart view (We use the Rnor_6 and 
# the ensembl reference genomes that links together with that.)

# Selected either Rat, Human, Zebrafish or Mouse and selected 'Attribute' Homologues
# -> the 3 other species in the same matrix

# Ensembl version 104 -> Rnor_6.0
rat_biomart = "Rat_Human_Zfish_Mouse_20_09_2022.txt"
# Ensembl version 104 -> GRCh38.p13
human_biomart = "Human_Rat_Zfish_Mouse_20_09_2022.txt"
# Ensembl version 104 -> GRCz11
zfish_biomart = "Zfish_Rat_Human_Mouse_20_09_2022.txt"
# Ensembl version 104 -> GRCm39
mouse_biomart = "Mouse_Rat_Human_Zfish_20_09_2022.txt"

# Output file
Complete_orto_matrix_file = "Complete_Ortholog_Matrix.csv"

## Variables ##

# The complete biomart list variable
Orthlog_mart = []

# Progress counters #
Rat_length_counter = 0
Human_length_counter = 0
Zfish_length_counter = 0
Mouse_length_counter = 0

## Read files ##

# read file lengths #
if check_exist(folder1, rat_biomart) and check_exist(folder1, human_biomart) and check_exist(folder1, zfish_biomart) and check_exist(folder1, mouse_biomart):
    with open(os.path.join(folder1,rat_biomart),'r') as read:
        next(read)
        for line in read:
            Rat_length_counter += 1
    read.close
    with open(os.path.join(folder1,human_biomart),'r') as read:
        next(read)
        for line in read:
            Human_length_counter += 1
    read.close
    with open(os.path.join(folder1,zfish_biomart),'r') as read:
        next(read)
        for line in read:
            Zfish_length_counter += 1
    read.close
    with open(os.path.join(folder1,mouse_biomart),'r') as read:
        next(read)
        for line in read:
            Mouse_length_counter += 1
    read.close
  
    # Rat orthlog biomart #
    progress_counter = 0
    percentage = 0
    with open(os.path.join(folder1,rat_biomart),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(",")
            #if there is a entry in rat biomart with all the other species add that entry
            if not line[1] == '' and not line[2] == '' and not line[3] == '':
                entry = [line[0],line[1],line[2],line[3]]
                Orthlog_mart.append(entry)
            # Progress counter
            if progress_counter % round(Rat_length_counter/100) == 0:
                percentage += 1
                if percentage % 10 == 0:
                    print("Reading rat file - Progress: {} / 100 %".format(percentage))
            progress_counter += 1
    read.close
    print("Orthlog matrix length Rat: {}".format(len(Orthlog_mart)))
    
    # Human orthlog biomart #
    progress_counter = 0
    percentage = 0
    with open(os.path.join(folder1,human_biomart),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(",")
            #if there is a entry in human biomart with all the other species add that entry
            if not line[1] == '' and not line[2] == '' and not line[3] == '':
                entry = [line[1],line[0],line[2],line[3]]
                Orthlog_mart.append(entry)
            # Progress counter
            if progress_counter % round(Human_length_counter/100) == 0:
                percentage += 1
                if percentage % 10 == 0:
                    print("Reading human file - Progress: {} / 100 %".format(percentage))
            progress_counter += 1
    read.close
    print("Orthlog matrix length Rat+Human: {}".format(len(Orthlog_mart)))
    
    # Zebrafish orthlog biomart #
    progress_counter = 0
    percentage = 0
    with open(os.path.join(folder1,zfish_biomart),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(",")
            #if there is a entry in zebrafish biomart with all the other species add that entry
            if not line[1] == '' and not line[2] == '' and not line[3] == '':
                entry = [line[1],line[2],line[0],line[3]]
                Orthlog_mart.append(entry)
            # Progress counter
            if progress_counter % round(Zfish_length_counter/100) == 0:
                percentage += 1
                if percentage % 10 == 0:
                    print("Reading Zebrafish file - Progress: {} / 100 %".format(percentage))
            progress_counter += 1
    read.close
    print("Orthlog matrix length Rat+Human+Zebrafish: {}".format(len(Orthlog_mart)))
    
    # Mouse orthlog biomart #
    progress_counter = 0
    percentage = 0
    with open(os.path.join(folder1,mouse_biomart),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(",")
            #if there is a entry in Mouse biomart with all the other species add that entry
            if not line[1] == '' and not line[2] == '' and not line[3] == '':
                entry = [line[1],line[2],line[3],line[0]]
                Orthlog_mart.append(entry)
            # Progress counter
            if progress_counter % round(Mouse_length_counter/100) == 0:
                percentage += 1
                if percentage % 10 == 0:
                    print("Reading Mouse file - Progress: {} / 100 %".format(percentage))
            progress_counter += 1
    read.close
    print("Orthlog matrix length Rat+Human+Zebrafish+Mouse: {}".format(len(Orthlog_mart)))
    
    # Take all the species entry from all the biomart and remove dublicates
    #set_of_Orthlog_mart = set(tuple(row) for row in Orthlog_mart)
    Redused_Orthlog_mart = [list(item) for item in set(tuple(row) for row in Orthlog_mart)]
    
    # check if a error has occured and a wrong entry is present in the wrong specie
    for key in Redused_Orthlog_mart:
        if not key[0].startswith("ENSRNOG"):
            print(key)
            break
        if not key[1].startswith("ENSG"):
            print(key)
            break
        if not key[2].startswith("ENSDARG"):
            print(key)
            break
        if not key[3].startswith("ENSMUSG"):
            print(key)
            break
    print("writing ortholog matrix")
    # Write the reduced biomart of all species to a file
    with open(os.path.join(folder2,Complete_orto_matrix_file),'w+') as out:
        out.write("Rat ID;Human ID;ZebraFish ID;Mouse ID\n")
        for key in Redused_Orthlog_mart:
            out.write("{}\n".format(";".join(key)))
    out.close
    print("done.")
else:
    print("Could not find ortholog files.")