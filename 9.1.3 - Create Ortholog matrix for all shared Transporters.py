# -*- coding: utf-8 -*-

### Biomarts orthologs - Complete matrice ###

import os

## Folders ##

folder1 = "Data/Transporter Lists/Ranked"
folder2 = "Data/Biomart"

folder3 = "Data/Biomart/Ranked transport"

os.makedirs(folder3,exist_ok=True)

## Files ##

# input files #

file_ranked_Rat = "Ranked_Shared_Transporters_Rat.csv"
file_ranked_Human = "Ranked_Shared_Transporters_Human.csv"
file_ranked_Zebrafish = "Ranked_Shared_Transporters_Zebrafish.csv"
file_ranked_Mouse = "Ranked_Shared_Transporters_Mouse.csv"

Complete_orto_matrix_file = "Complete_Ortholog_Matrix.csv"

# Output file #

Ortholog_matrix_shared_transporters = "Transporter_shared_ortholog_matrix.csv"

## Variables ##

# The complete biomart list variable
Orthlog_mart = []

# Progress counters #
Ortholog_matrix_length_counter = 0

# Gene lists #
Rat_entries = []
Human_entries = []
Zebrafish_entries = []
Mouse_entries = []

## Read files ##

# Ranked Rat #
with open(os.path.join(folder1,file_ranked_Rat),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        Rat_entries.append(line[0])
read.close

# Ranked Human #
with open(os.path.join(folder1,file_ranked_Human),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        Human_entries.append(line[0])
read.close

# Ranked Zebrafish #
with open(os.path.join(folder1,file_ranked_Zebrafish),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        Zebrafish_entries.append(line[0])
read.close

# Ranked Mouse #
with open(os.path.join(folder1,file_ranked_Mouse),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        Mouse_entries.append(line[0])
read.close


# read complete ortholog file lengths #
with open(os.path.join(folder2,Complete_orto_matrix_file),'r') as read:
    next(read)
    for line in read:
        Ortholog_matrix_length_counter += 1
read.close
    
# Complete orthlog matrix #
progress_counter = 0
percentage = 0
with open(os.path.join(folder2,Complete_orto_matrix_file),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        if line[0] in Rat_entries and line[1] in Human_entries and line[2] in Zebrafish_entries and line[3] in Mouse_entries:
            Orthlog_mart.append(line)
        else:
            pass
        # Progress counter
        if progress_counter % round(Ortholog_matrix_length_counter/100) == 0 and percentage < 110:
            percentage += 1
            if percentage % 10 == 0:
                print("Reading ortholog file - Progress: {} / 100 %".format(percentage))
        progress_counter += 1
read.close

Redused_Orthlog_mart = [list(item) for item in set(tuple(row) for row in Orthlog_mart)]

## Save ortholog matrix to file ##

with open(os.path.join(folder3,Ortholog_matrix_shared_transporters),'w+') as out:
    out.write("Rat ID;Human ID;ZebraFish ID;Mouse ID\n")
    for key in Redused_Orthlog_mart:
        out.write("{}\n".format(";".join(key)))
out.close()