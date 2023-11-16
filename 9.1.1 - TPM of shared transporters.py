# -*- coding: utf-8 -*-

### TPM ditribution of shared transporters ###

## Libraries ##

import os

## functions ##

def check_exist(folder,file):
    return os.path.exists(os.path.join(folder,file))

## Folders ##

folder1 = "Data/Transporter Lists"
folder2 = "Data/Count tables/All genes"
folder3 = "Data/Gene lists/Transporters/All genes"

out_folder = "Results/TPM"

os.makedirs(out_folder,exist_ok=True)
    
## files ##

file_Transporter_rat = "Transporter_list_concatenated_rat.csv"
file_Transporter_human = "Transporter_list_concatenated_human.csv"
file_Transporter_zebrafish = "Transporter_list_concatenated_zebrafish.csv"
file_Transporter_mouse = "Transporter_list_concatenated_mouse.csv"

file_CT_rat = "Rat_count_table_all.csv"
file_CT_human = "Human_count_table_all.csv"
file_CT_zebrafish = "Zebrafish_count_table_all.csv"
file_CT_mouse = "Mouse_count_table_all.csv"

file_rat_shared_all = "Shared_orthologues_gene_in_all_species_list_Rat.csv"
file_human_shared_all = "Shared_orthologues_gene_in_all_species_list_Human.csv"
file_zebrafish_shared_all = "Shared_orthologues_gene_in_all_species_list_Zebrafish.csv"
file_mouse_shared_all = "Shared_orthologues_gene_in_all_species_list_Mouse.csv"

file_single_shared_rat = "Single_species_shared_analysis_Rat.csv"
file_single_shared_human = "Single_species_shared_analysis_Human.csv"
file_single_shared_zebrafish = "Single_species_shared_analysis_Zebrafish.csv"
file_single_shared_mouse = "Single_species_shared_analysis_Mouse.csv"

## Variables ##

# File flags #

transporter_flag = "yes"
CT_flag = "yes"
shared_all_flag = "yes"
single_shared_flag = "yes"

# global #

Transporter_entries_Rat = []
Transporter_entries_Human = []
Transporter_entries_Zebrafish = []
Transporter_entries_Mouse = []

CT_dict_Rat = {}
CT_dict_Human = {}
CT_dict_Zebrafish = {}
CT_dict_Mouse = {}

Shared_entries_Rat = []
Shared_entries_Human = []
Shared_entries_Zebrafish = []
Shared_entries_Mouse = []

Mammals_shared_entries_Rat = []
Mammals_shared_entries_Human = []
Mammals_shared_entries_Mouse = []

Not_shared_entries_Rat = []
Not_shared_entries_Human = []
Not_shared_entries_Zebrafish = []
Not_shared_entries_Mouse = []

Shared_percent_all_Rat = 0
Shared_percent_all_Human = 0
Shared_percent_all_Zebrafish = 0
Shared_percent_all_Mouse = 0

Shared_percent_mammals_Rat = 0
Shared_percent_mammals_Human = 0
Shared_percent_mammals_Mouse = 0


Not_shared_percent_Rat = 0
Not_shared_percent_Human = 0
Not_shared_percent_Zebrafish = 0
Not_shared_percent_Mouse = 0

## read files ##

# Transporters #
if check_exist(folder1, file_Transporter_rat) and check_exist(folder1, file_Transporter_human) and check_exist(folder1, file_Transporter_zebrafish) and check_exist(folder1, file_Transporter_mouse):
    ## read transporter lists ##
    # Rat #
    with open(os.path.join(folder1, file_Transporter_rat),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            Transporter_entries_Rat.append(line[0])
    read.close()
    # Human #
    with open(os.path.join(folder1, file_Transporter_human),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            Transporter_entries_Human.append(line[0])
    read.close()
    # Zebrafish #
    with open(os.path.join(folder1, file_Transporter_zebrafish),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            Transporter_entries_Zebrafish.append(line[0])
    read.close()
    # Mouse #
    with open(os.path.join(folder1, file_Transporter_mouse),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            Transporter_entries_Mouse.append(line[0])
    read.close()
else:
    print("Error: Missing Transporter files")
    transporter_flag = 'No'


# Count tables #
if check_exist(folder2, file_CT_rat) and check_exist(folder2, file_CT_human) and check_exist(folder2, file_CT_zebrafish) and check_exist(folder2, file_CT_mouse):
    ## read Count table values ##
    # Rat #
    with open(os.path.join(folder2, file_CT_rat),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            if line[0] in Transporter_entries_Rat:
                CT_dict_Rat[line[0]] = float(line[2])
            else:
                pass
    read.close()
    
    # Human #
    with open(os.path.join(folder2, file_CT_human),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            if line[0] in Transporter_entries_Human:
                CT_dict_Human[line[0]] = float(line[2])
            else:
                pass
    read.close()
    # Zebrafish #
    with open(os.path.join(folder2, file_CT_zebrafish),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            if line[0] in Transporter_entries_Zebrafish:
                CT_dict_Zebrafish[line[0]] = float(line[2])
            else:
                pass
    read.close()
    # Mouse #
    with open(os.path.join(folder2, file_CT_mouse),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            if line[0] in Transporter_entries_Mouse:
                CT_dict_Mouse[line[0]] = float(line[2])
            else:
                pass
    read.close()
    if len(Transporter_entries_Rat) == len(CT_dict_Rat) and len(Transporter_entries_Human) == len(CT_dict_Human) and len(Transporter_entries_Zebrafish) == len(CT_dict_Zebrafish) and len(Transporter_entries_Mouse) == len(CT_dict_Mouse):
        pass
    else:
        print("Error: lengths of transporter list and count table lists not the same")
        CT_flag = 'No'
else:
    print("Error: Missing Transporter files")
    CT_flag = 'No'
    
# Shared transporters in all species #
if check_exist(folder3, file_rat_shared_all) and check_exist(folder3, file_human_shared_all) and check_exist(folder3, file_zebrafish_shared_all) and check_exist(folder3, file_mouse_shared_all):
    ## read transporter lists ##
    # Rat #
    with open(os.path.join(folder3, file_rat_shared_all),'r') as read:
        for line in read:
            line = line.strip()
            Shared_entries_Rat.append(line)
    read.close()
    
    # Human #
    with open(os.path.join(folder3, file_human_shared_all),'r') as read:
        for line in read:
            line = line.strip()
            Shared_entries_Human.append(line)
    read.close()
    # Zebrafish #
    with open(os.path.join(folder3, file_zebrafish_shared_all),'r') as read:
        for line in read:
            line = line.strip()
            Shared_entries_Zebrafish.append(line)
    read.close()
    # Mouse #
    with open(os.path.join(folder3, file_mouse_shared_all),'r') as read:
        for line in read:
            line = line.strip()
            Shared_entries_Mouse.append(line)
    read.close()
else:
    print("Error: Missing shared in all species files")
    shared_all_flag = 'No'

counter = 0
# Shared transporters in single species #
if check_exist(folder3, file_single_shared_rat) and check_exist(folder3, file_single_shared_human) and check_exist(folder3, file_single_shared_zebrafish) and check_exist(folder3, file_single_shared_mouse):
    ## read transporter lists ##
    # Rat #
    with open(os.path.join(folder3, file_single_shared_rat),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            if len(line[1:]) == 1:
                Not_shared_entries_Rat.append(line[0])
            elif 'R' in line[1:] and 'H' in line[1:] and 'M' in line[1:]:
                Mammals_shared_entries_Rat.append(line[0])
            else:
                pass
    read.close()
    # Human #
    with open(os.path.join(folder3, file_single_shared_human),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            if len(line[1:]) == 1:
                Not_shared_entries_Human.append(line[0])
            elif 'R' in line[1:] and 'H' in line[1:] and 'M' in line[1:]:
                Mammals_shared_entries_Human.append(line[0])
            else:
                pass
    read.close()
    # Zebrafish #
    with open(os.path.join(folder3, file_single_shared_zebrafish),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            if len(line[1:]) == 1:
                Not_shared_entries_Zebrafish.append(line[0])
            else:
                pass
    read.close()
    # Mouse #
    with open(os.path.join(folder3, file_single_shared_mouse),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            if len(line[1:]) == 1:
                Not_shared_entries_Mouse.append(line[0])
            elif 'R' in line[1:] and 'H' in line[1:] and 'M' in line[1:]:
                Mammals_shared_entries_Mouse.append(line[0])
            else:
                pass
    read.close()
else:
    print("Error: Missing shared in all species files")
    single_shared_flag = 'No'


## Convert TPM to percentage of transporters ##

# Rat sum #
Sum_TPM_Rat = 0
for key in CT_dict_Rat:
    Sum_TPM_Rat += CT_dict_Rat[key]
Sum_TPM_Rat = round(Sum_TPM_Rat,2)
# Human sum #
Sum_TPM_Human = 0
for key in CT_dict_Human:
    Sum_TPM_Human += CT_dict_Human[key]
Sum_TPM_Human = round(Sum_TPM_Human,2)
Sum_TPM_Zebrafish = 0
# Zebrafish sum #
for key in CT_dict_Zebrafish:
    Sum_TPM_Zebrafish += CT_dict_Zebrafish[key]
Sum_TPM_Zebrafish = round(Sum_TPM_Zebrafish,2)
# Mouse sum #
Sum_TPM_Mouse = 0
for key in CT_dict_Mouse:
    Sum_TPM_Mouse += CT_dict_Mouse[key]
Sum_TPM_Mouse = round(Sum_TPM_Mouse,2)

# Rat percent #
CT_dict_Rat_percent = {}
for key in CT_dict_Rat:
    CT_dict_Rat_percent[key] = (CT_dict_Rat[key]/Sum_TPM_Rat)*100
# Human percent #
CT_dict_Human_percent = {}
for key in CT_dict_Human:
    CT_dict_Human_percent[key] = (CT_dict_Human[key]/Sum_TPM_Human)*100
CT_dict_Zebrafish_percent = {}
# Zebrafish percent #
for key in CT_dict_Zebrafish:
    CT_dict_Zebrafish_percent[key] = (CT_dict_Zebrafish[key]/Sum_TPM_Zebrafish)*100
# Mouse percent #
CT_dict_Mouse_percent = {}
for key in CT_dict_Mouse:
    CT_dict_Mouse_percent[key] = (CT_dict_Mouse[key]/Sum_TPM_Mouse)*100

### Percentage shared ###
## All ##
round_decimal = 2

for key in Shared_entries_Rat:
    Shared_percent_all_Rat += CT_dict_Rat_percent[key]
print("Shared all TPM percent Rat: {}%".format(round(Shared_percent_all_Rat,round_decimal)))

for key in Shared_entries_Human:
    Shared_percent_all_Human += CT_dict_Human_percent[key]
print("Shared all TPM percent Human: {}%".format(round(Shared_percent_all_Human,round_decimal)))

for key in Shared_entries_Zebrafish:
    Shared_percent_all_Zebrafish += CT_dict_Zebrafish_percent[key]
print("Shared all TPM percent Zebrafish: {}%".format(round(Shared_percent_all_Zebrafish,round_decimal)))

for key in Shared_entries_Mouse:
    Shared_percent_all_Mouse += CT_dict_Mouse_percent[key]
print("Shared all TPM percent Mouse: {}%".format(round(Shared_percent_all_Mouse,round_decimal)))

## Mammals ##

for key in Mammals_shared_entries_Rat:
    Shared_percent_mammals_Rat += CT_dict_Rat_percent[key]
print("Shared Mammals TPM percent Rat: {}%".format(round(Shared_percent_mammals_Rat,round_decimal)))

for key in Mammals_shared_entries_Human:
    Shared_percent_mammals_Human += CT_dict_Human_percent[key]
print("Shared Mammals TPM percent Human: {}%".format(round(Shared_percent_mammals_Human,round_decimal)))

for key in Mammals_shared_entries_Mouse:
    Shared_percent_mammals_Mouse += CT_dict_Mouse_percent[key]
print("Shared Mammals TPM percent Mouse: {}%".format(round(Shared_percent_mammals_Mouse,round_decimal)))

print("Combined all and mammals - Rat: {}%".format(round(Shared_percent_all_Rat+Shared_percent_mammals_Rat,round_decimal)))
print("Combined all and mammals - Human: {}%".format(round(Shared_percent_all_Human+Shared_percent_mammals_Human,round_decimal)))
print("Combined all and mammals - Mouse: {}%".format(round(Shared_percent_all_Mouse+Shared_percent_mammals_Mouse,round_decimal)))

## Non shared ##
# Rat #
for key in Not_shared_entries_Rat:
    Not_shared_percent_Rat += CT_dict_Rat_percent[key]
print("Non-shared genes in TPM percent Rat: {}%".format(round(Not_shared_percent_Rat,round_decimal)))
# Human #
for key in Not_shared_entries_Human:
    Not_shared_percent_Human += CT_dict_Human_percent[key]
print("Non-shared genes in TPM percent Human: {}%".format(round(Not_shared_percent_Human,round_decimal)))

# Zebrafish #
for key in Not_shared_entries_Zebrafish:
    Not_shared_percent_Zebrafish += CT_dict_Zebrafish_percent[key]
print("Non-shared genes in TPM percent Zebrafish: {}%".format(round(Not_shared_percent_Zebrafish,round_decimal)))

# Mouse #
for key in Not_shared_entries_Mouse:
    Not_shared_percent_Mouse += CT_dict_Mouse_percent[key]
print("Non-shared genes in TPM percent Mouse: {}%".format(round(Not_shared_percent_Mouse,round_decimal)))


