# -*- coding: utf-8 -*-

#### Concatenate Ensembl and Gene lists from panther ####

### Libraries ###

import os

### Folders ###

Folder1 = "Data/Count tables/All genes"
Folder2 = "Data/Panther DB"
Folder3 = "Data/Transporter Lists"

os.makedirs(Folder3,exist_ok=True)

### Files ###

## Count Tables ##

file_CT_rat = "Rat_count_table_all.csv"
file_CT_human = "Human_count_table_all.csv"
file_CT_mouse = "Mouse_count_table_all.csv"
file_CT_zebrafish = "Zebrafish_count_table_all.csv"

## Panther DB ##

# Rat #
file_P_rat_ensembl = "Panther_RAT_Ensembl_Transporters.txt"
file_P_rat_gene = "Panther_RAT_Gene_Transporters.txt"

# Human #
file_P_human_ensembl = "Panther_HUMAN_Ensembl_Transporters.txt"
file_P_human_gene = "Panther_HUMAN_Gene_Transporters.txt"

# Mouse #
file_P_mouse_ensembl = "Panther_MOUSE_Ensembl_Transporters.txt"
file_P_mouse_gene = "Panther_MOUSE_Gene_Transporters.txt"

# Zebrafish #
file_P_zebrafish_ensembl = "Panther_ZFISH_Ensembl_Transporters.txt"
file_P_zebrafish_gene = "Panther_ZFISH_Gene_Transporters.txt"

## Output files ##

out_file_rat = "Transporter_list_concatenated_rat.csv"
out_file_human = "Transporter_list_concatenated_human.csv"
out_file_mouse = "Transporter_list_concatenated_mouse.csv"
out_file_zebrafish = "Transporter_list_concatenated_zebrafish.csv"

### Varaibles ###

## Count tables ##
CT_dict_Rat = {}
CT_dict_Human = {}
CT_dict_Mouse = {}
CT_dict_Zebrafish = {}

## Rat ##

# Correct genes #
Rat_CT_gene_list = []

Rat_transporter_dict_TransporterType = {}

Rat_Transporter_list = []
Rat_Different_transporters = []
Rat_Ensembl_Uniprot_TransporterType = {}
Rat_Gene_Uniprot_TransporterType = {}
Rat_additional_ensembl_entries = {}

## Human ##

# Correct genes #
Human_CT_gene_list = []

Human_transporter_dict_TransporterType = {}

Human_Transporter_list = []
Human_Different_transporters = []
Human_Ensembl_Uniprot_TransporterType = {}
Human_Gene_Uniprot_TransporterType = {}
Human_additional_ensembl_entries = {}

## Mouse ##

# Correct genes #
Mouse_CT_gene_list = []

Mouse_transporter_dict_TransporterType = {}

Mouse_Transporter_list = []
Mouse_Different_transporters = []
Mouse_Ensembl_Uniprot_TransporterType = {}
Mouse_Gene_Uniprot_TransporterType = {}
Mouse_additional_ensembl_entries = {}

## Zebrafish ##

# Correct genes #
Zebrafish_CT_gene_list = []

Zebrafish_transporter_dict_TransporterType = {}

Zebrafish_Transporter_list = []
Zebrafish_Different_transporters = []
Zebrafish_Ensembl_Uniprot_TransporterType = {}
Zebrafish_Gene_Uniprot_TransporterType = {}
Zebrafish_additional_ensembl_entries = {}

### Read files ###

## Count Tables ##

# Rat #
with open(os.path.join(Folder1,file_CT_rat),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        CT_dict_Rat[line[0]] = line[1]
        Rat_CT_gene_list.append(line[1])
read.close()

# Human #

with open(os.path.join(Folder1,file_CT_human),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        CT_dict_Human[line[0]] = line[1]
        Human_CT_gene_list.append(line[1])
read.close()

# Mouse #

with open(os.path.join(Folder1,file_CT_mouse),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        CT_dict_Mouse[line[0]] = line[1]
        Mouse_CT_gene_list.append(line[1])
read.close()

# Zebrafish #

with open(os.path.join(Folder1,file_CT_zebrafish),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split(";")
        CT_dict_Zebrafish[line[0]] = line[1]
        Zebrafish_CT_gene_list.append(line[1])
read.close()

### Panther DB ###

## Rat ##
# Rat ensembl #
Rat_Ensembl_file_counter = 0
with open(os.path.join(Folder2,file_P_rat_ensembl),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split("\t")
        # Assign uniprot ID #
        if "UniProtKB" not in line[0]:
            print("Error in rat ensembl file")
            print(line[0])
            break
        else:
            Identifiers = line[0].split("|")
            uniprot = Identifiers[2].split("=")[1]
            ensembl_id = line[1]
            if ensembl_id not in CT_dict_Rat:
                ensembl_entries = ensembl_id.split(",")
                gene_name = line[2].split(";")[1]
                for entry in ensembl_entries:
                    if entry in CT_dict_Rat:
                        if CT_dict_Rat[entry] == gene_name:
                            Rat_Ensembl_Uniprot_TransporterType[entry] = [uniprot,line[4]]
                            Rat_Ensembl_file_counter += 1
                        else:
                            pass
            else:
                Rat_Ensembl_Uniprot_TransporterType[ensembl_id] = [uniprot,line[4]]
                Rat_Ensembl_file_counter += 1
read.close()

# Rat Gene #
Rat_Gene_file_counter = 0
with open(os.path.join(Folder2,file_P_rat_gene),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split("\t")
        # Assign uniprot ID #
        if "UniProtKB" not in line[0]:
            print("Error in rat gene file")
            print(line[0])
            break
        else:
            Identifiers = line[0].split("|")
            uniprot = Identifiers[2].split("=")[1]
            Rat_Gene_file_counter += 1
            gene_name = line[2].split(";")[1]
            if ',' in line[1]:
                correct_gene_name = ''
                entries = line[1].split(",")
                for key in entries:
                    if key == gene_name:
                        correct_gene_name = key
                    else:
                        pass
                if correct_gene_name == '':
                    correct_gene_name = entries[0]
            else:   
                correct_gene_name = line[1]
            # if entry not in Count table -> a wrong annotation have happend by panther DB        
            if correct_gene_name not in Rat_CT_gene_list:
                pass
            else:
                # print out dublicates
                if correct_gene_name in Rat_Gene_Uniprot_TransporterType:
                    if correct_gene_name not in Rat_CT_gene_list:
                        pass
                    else:
                        # evaluate entries and write case handling
                        if correct_gene_name == 'Mfsd4b':
                            Rat_Gene_Uniprot_TransporterType[correct_gene_name] = ['Q80T22',line[4]]
                        elif correct_gene_name == 'Pam16':
                            Rat_Gene_Uniprot_TransporterType[correct_gene_name] = ['Q6EIX2',line[4]]
                        else:    
                            print(correct_gene_name,uniprot)
                            print(correct_gene_name,Rat_Gene_Uniprot_TransporterType[correct_gene_name])
                else:
                    Rat_Gene_Uniprot_TransporterType[correct_gene_name] = [uniprot,line[4]]    
read.close()

# Add all ensembl entries to Transporter list #
for key in Rat_Ensembl_Uniprot_TransporterType:
    if key not in Rat_Transporter_list:
        Rat_Transporter_list.append(key)
    else:
        print("this key is a dublicate",key)
    if key not in Rat_transporter_dict_TransporterType:
        Rat_transporter_dict_TransporterType[key] = [CT_dict_Rat[key],Rat_Ensembl_Uniprot_TransporterType[key][0],Rat_Ensembl_Uniprot_TransporterType[key][1]]
    else:
        print("This key is a dublicate in the final transporter dict")
Rat_gene_PASS = 'No'
Rat_gene_PASS_length = 'Yes'
## lookup all additional genes from gene name dict and add ensembls to transporter list ##
Rat_dublicate_control_check = {}
for key in Rat_Gene_Uniprot_TransporterType:
    for item in CT_dict_Rat:
        if key == CT_dict_Rat[item]:
            if key not in Rat_dublicate_control_check:
                Rat_dublicate_control_check[key] = []
                Rat_dublicate_control_check[key].append(item)
            else:
                Rat_dublicate_control_check[key].append(item)
for key in Rat_dublicate_control_check:
    if len(Rat_dublicate_control_check[key]) > 1:
        print(key,Rat_dublicate_control_check[key])
        Rat_gene_PASS_length = 'No'
    else:
        pass
if len(Rat_dublicate_control_check) == len(Rat_Gene_Uniprot_TransporterType):
    print("rat gene dublicate check passed")
    Rat_gene_PASS = 'Yes'
else:
    print("rat gene dublicate check NOT passed")
    print("length of dublicate {} does not equal length of Gene_Uniprot_transporterType {}".format(len(Rat_dublicate_control_check),len(Rat_Gene_Uniprot_TransporterType)))

Rat_dublicate_key_counter = 0
if Rat_gene_PASS == 'Yes' and Rat_gene_PASS_length == 'Yes':
    for key in Rat_dublicate_control_check:
        Rat_additional_ensembl_entries[Rat_dublicate_control_check[key][0]] = key
    for key in Rat_additional_ensembl_entries:
        if key in Rat_transporter_dict_TransporterType:
            Rat_dublicate_key_counter += 1
        else:
            Rat_transporter_dict_TransporterType[key] = [Rat_additional_ensembl_entries[key],Rat_Gene_Uniprot_TransporterType[Rat_additional_ensembl_entries[key]][0],Rat_Gene_Uniprot_TransporterType[Rat_additional_ensembl_entries[key]][1]]
else:
    print("Rat gene PASS not correct...")



## Human ##
# Human ensembl #
Human_Ensembl_file_counter = 0
with open(os.path.join(Folder2,file_P_human_ensembl),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split("\t")
        # Assign uniprot ID #
        if "UniProtKB" not in line[0]:
            print("Error in Human ensembl file")
            print(line[0])
            break
        else:
            Identifiers = line[0].split("|")
            uniprot = Identifiers[2].split("=")[1]
            ensembl_id = line[1]
            if ensembl_id not in CT_dict_Human:
                ensembl_entries = ensembl_id.split(",")
                gene_name = line[2].split(";")[1]
                for entry in ensembl_entries:
                    if entry in CT_dict_Human:
                        if CT_dict_Human[entry] == gene_name:
                            Human_Ensembl_Uniprot_TransporterType[entry] = [uniprot,line[4]]
                            Human_Ensembl_file_counter += 1
                        else:
                            pass
            else:
                Human_Ensembl_Uniprot_TransporterType[ensembl_id] = [uniprot,line[4]]
                Human_Ensembl_file_counter += 1
read.close()

# Human Gene #
Human_Gene_file_counter = 0
with open(os.path.join(Folder2,file_P_human_gene),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split("\t")
        # Assign uniprot ID #
        if "UniProtKB" not in line[0]:
            print("Error in Human gene file")
            print(line[0])
            break
        else:
            Identifiers = line[0].split("|")
            uniprot = Identifiers[2].split("=")[1]
            Human_Gene_file_counter += 1
            gene_name = line[2].split(";")[1]
            if ',' in line[1]:
                correct_gene_name = ''
                entries = line[1].split(",")
                for key in entries:
                    if key == gene_name:
                        correct_gene_name = key
                    else:
                        pass
                if correct_gene_name == '':
                    correct_gene_name = entries[0]
            else:   
                correct_gene_name = line[1]
            # if entry not in Count table -> a wrong annotation have happend by panther DB        
            if correct_gene_name not in Human_CT_gene_list:
                pass
            else:
                # print out dublicates
                if correct_gene_name in Human_Gene_Uniprot_TransporterType:
                    if correct_gene_name not in Human_CT_gene_list:
                        pass
                    else:
                        # evaluate entries and write case handling
                        if correct_gene_name == 'KCNG3':
                            Human_Gene_Uniprot_TransporterType[correct_gene_name] = ['Q8TAE7',line[4]]
                        elif correct_gene_name == 'CHRNA7':
                            Human_Gene_Uniprot_TransporterType[correct_gene_name] = ['P36544',line[4]]
                        elif correct_gene_name == 'NET1':
                            Human_Gene_Uniprot_TransporterType[correct_gene_name] = ['P23975',line[4]]
                        else:    
                            print(correct_gene_name,uniprot)
                            print(correct_gene_name,Human_Gene_Uniprot_TransporterType[correct_gene_name])
                else:
                    Human_Gene_Uniprot_TransporterType[correct_gene_name] = [uniprot,line[4]]    
read.close()

# Add all ensembl entries to Transporter list #
for key in Human_Ensembl_Uniprot_TransporterType:
    if key not in Human_Transporter_list:
        Human_Transporter_list.append(key)
    else:
        print("this key is a dublicate",key)
    if key not in Human_transporter_dict_TransporterType:
        Human_transporter_dict_TransporterType[key] = [CT_dict_Human[key],Human_Ensembl_Uniprot_TransporterType[key][0],Human_Ensembl_Uniprot_TransporterType[key][1]]
    else:
        print("This key is a dublicate in the final transporter dict")
Human_gene_PASS = 'No'
Human_gene_PASS_length = 'Yes'
## lookup all additional genes from gene name dict and add ensembls to transporter list ##
Human_dublicate_control_check = {}
for key in Human_Gene_Uniprot_TransporterType:
    for item in CT_dict_Human:
        if key == CT_dict_Human[item]:
            if key not in Human_dublicate_control_check:
                Human_dublicate_control_check[key] = []
                Human_dublicate_control_check[key].append(item)
            else:
                Human_dublicate_control_check[key].append(item)
for key in Human_dublicate_control_check:
    if len(Human_dublicate_control_check[key]) > 1:
        print(key,Human_dublicate_control_check[key])
        Human_gene_PASS_length = 'No'
    else:
        pass
if len(Human_dublicate_control_check) == len(Human_Gene_Uniprot_TransporterType):
    print("Human gene dublicate check passed")
    Human_gene_PASS = 'Yes'
else:
    print("Human gene dublicate check NOT passed")
    print("length of dublicate {} does not equal length of Gene_Uniprot_transporterType {}".format(len(Human_dublicate_control_check),len(Human_Gene_Uniprot_TransporterType)))

Human_dublicate_key_counter = 0
if Human_gene_PASS == 'Yes' and Human_gene_PASS_length == 'Yes':
    for key in Human_dublicate_control_check:
        Human_additional_ensembl_entries[Human_dublicate_control_check[key][0]] = key
    for key in Human_additional_ensembl_entries:
        if key in Human_transporter_dict_TransporterType:
            Human_dublicate_key_counter += 1
        else:
            Human_transporter_dict_TransporterType[key] = [Human_additional_ensembl_entries[key],Human_Gene_Uniprot_TransporterType[Human_additional_ensembl_entries[key]][0],Human_Gene_Uniprot_TransporterType[Human_additional_ensembl_entries[key]][1]]
else:
    print("Human gene PASS not correct...")

## Mouse ##
# Mouse ensembl #
Mouse_Ensembl_file_counter = 0
with open(os.path.join(Folder2,file_P_mouse_ensembl),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split("\t")
        # Assign uniprot ID #
        if "UniProtKB" not in line[0]:
            print("Error in Mouse ensembl file")
            print(line[0])
            break
        else:
            Identifiers = line[0].split("|")
            uniprot = Identifiers[2].split("=")[1]
            ensembl_id = line[1]
            if ensembl_id not in CT_dict_Mouse:
                ensembl_entries = ensembl_id.split(",")
                gene_name = line[2].split(";")[1]
                for entry in ensembl_entries:
                    if entry in CT_dict_Mouse:
                        if CT_dict_Mouse[entry] == gene_name:
                            Mouse_Ensembl_Uniprot_TransporterType[entry] = [uniprot,line[4]]
                            Mouse_Ensembl_file_counter += 1
                        else:
                            pass
            else:
                Mouse_Ensembl_Uniprot_TransporterType[ensembl_id] = [uniprot,line[4]]
                Mouse_Ensembl_file_counter += 1
read.close()
    
# Mouse Gene #
Mouse_Gene_file_counter = 0
with open(os.path.join(Folder2,file_P_mouse_gene),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split("\t")
        # Assign uniprot ID #
        if "UniProtKB" not in line[0]:
            print("Error in Mouse gene file")
            print(line[0])
            break
        else:
            Identifiers = line[0].split("|")
            uniprot = Identifiers[2].split("=")[1]
            Mouse_Gene_file_counter += 1
            gene_name = line[2].split(";")[1]
            if ',' in line[1]:
                correct_gene_name = ''
                entries = line[1].split(",")
                for key in entries:
                    if key == gene_name:
                        correct_gene_name = key
                    else:
                        pass
                if correct_gene_name == '':
                    correct_gene_name = entries[0]
            else:   
                correct_gene_name = line[1]
            # if entry not in Count table -> a wrong annotation have happend by panther DB        
            if correct_gene_name not in Mouse_CT_gene_list:
                pass
            else:
                # print out dublicates
                if correct_gene_name in Mouse_Gene_Uniprot_TransporterType:
                    if correct_gene_name not in Mouse_CT_gene_list:
                        pass
                    else:
                        # evaluate entries and write case handling
                        if correct_gene_name == 'Ms4a1':
                            Mouse_Gene_Uniprot_TransporterType[correct_gene_name] = ['P19437',line[4]]
                        else:    
                            print("uniprot incorrect",correct_gene_name,uniprot)
                            print(correct_gene_name,Mouse_Gene_Uniprot_TransporterType[correct_gene_name])
                else:
                    Mouse_Gene_Uniprot_TransporterType[correct_gene_name] = [uniprot,line[4]]    
read.close()

# Add all ensembl entries to Transporter list #
for key in Mouse_Ensembl_Uniprot_TransporterType:
    if key not in Mouse_Transporter_list:
        Mouse_Transporter_list.append(key)
    else:
        print("this key is a dublicate",key)
    if key not in Mouse_transporter_dict_TransporterType:
        Mouse_transporter_dict_TransporterType[key] = [CT_dict_Mouse[key],Mouse_Ensembl_Uniprot_TransporterType[key][0],Mouse_Ensembl_Uniprot_TransporterType[key][1]]
    else:
        print("This key is a dublicate in the final transporter dict")
Mouse_gene_PASS = 'No'
Mouse_gene_PASS_length = 'Yes'
## lookup all additional genes from gene name dict and add ensembls to transporter list ##
Mouse_dublicate_control_check = {}
for key in Mouse_Gene_Uniprot_TransporterType:
    for item in CT_dict_Mouse:
        if key == CT_dict_Mouse[item]:
            if key not in Mouse_dublicate_control_check:
                Mouse_dublicate_control_check[key] = []
                Mouse_dublicate_control_check[key].append(item)
            else:
                Mouse_dublicate_control_check[key].append(item)
## Check entries and manually append correct entries ##
"""
for key in Mouse_dublicate_control_check:
    if len(Mouse_dublicate_control_check[key]) > 1:
        if key == "Atp5o":
            Mouse_dublicate_control_check[key] = ['ENSMUSG00000022956']
        else:
            print("dublicate detected",key,Mouse_dublicate_control_check[key])
            Mouse_gene_PASS_length = 'No'
    else:
        pass


if len(Mouse_dublicate_control_check) == len(Mouse_Gene_Uniprot_TransporterType):
    print("Mouse gene dublicate check passed")
    Mouse_gene_PASS = 'Yes'
else:
    print("Mouse gene dublicate check NOT passed")
    print("length of dublicate {} does not equal length of Gene_Uniprot_transporterType {}".format(len(Mouse_dublicate_control_check),len(Mouse_Gene_Uniprot_TransporterType)))
"""
Mouse_gene_PASS = 'Yes'
Mouse_gene_PASS_length = 'Yes'
Mouse_dublicate_key_counter = 0
if Mouse_gene_PASS == 'Yes' and Mouse_gene_PASS_length == 'Yes':
    for key in Mouse_dublicate_control_check:
        if len(Mouse_dublicate_control_check[key]) > 1:
            for item in Mouse_dublicate_control_check[key]:
                Mouse_additional_ensembl_entries[item] = key
        else:
            Mouse_additional_ensembl_entries[Mouse_dublicate_control_check[key][0]] = key
    for key in Mouse_additional_ensembl_entries:
        if key in Mouse_transporter_dict_TransporterType:
            Mouse_dublicate_key_counter += 1
        else:
            Mouse_transporter_dict_TransporterType[key] = [Mouse_additional_ensembl_entries[key],Mouse_Gene_Uniprot_TransporterType[Mouse_additional_ensembl_entries[key]][0],Mouse_Gene_Uniprot_TransporterType[Mouse_additional_ensembl_entries[key]][1]]
else:
    print("Mouse gene PASS not correct...")
print("Mouse cleared")

## Zebrafish ##
# Zebrafish ensembl #
Zebrafish_Ensembl_file_counter = 0
with open(os.path.join(Folder2,file_P_zebrafish_ensembl),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split("\t")
        # Assign uniprot ID #
        if "UniProtKB" not in line[0]:
            print("Error in Zebrafish ensembl file")
            print(line[0])
            break
        else:
            Identifiers = line[0].split("|")
            uniprot = Identifiers[2].split("=")[1]
            ensembl_id = line[1]
            if ensembl_id not in CT_dict_Zebrafish:
                ensembl_entries = ensembl_id.split(",")
                gene_name = line[2].split(";")[1]
                for entry in ensembl_entries:
                    if entry in CT_dict_Zebrafish:
                        if CT_dict_Zebrafish[entry] == gene_name:
                            Zebrafish_Ensembl_Uniprot_TransporterType[entry] = [uniprot,line[4]]
                            Zebrafish_Ensembl_file_counter += 1
                        else:
                            pass
            else:
                Zebrafish_Ensembl_Uniprot_TransporterType[ensembl_id] = [uniprot,line[4]]
                Zebrafish_Ensembl_file_counter += 1
read.close()

# Zebrafish Gene #
Zebrafish_Gene_file_counter = 0
with open(os.path.join(Folder2,file_P_zebrafish_gene),'r') as read:
    next(read)
    for line in read:
        line = line.strip().split("\t")
        # Assign uniprot ID #
        if "UniProtKB" not in line[0]:
            print("Error in Zebrafish gene file")
            print(line[0])
            break
        else:
            Identifiers = line[0].split("|")
            uniprot = Identifiers[2].split("=")[1]
            Zebrafish_Gene_file_counter += 1
            gene_name = line[2].split(";")[1]
            if ',' in line[1]:
                correct_gene_name = ''
                entries = line[1].split(",")
                for key in entries:
                    if key == gene_name:
                        correct_gene_name = key
                    else:
                        pass
                if correct_gene_name == '':
                    correct_gene_name = entries[0]
            else:   
                correct_gene_name = line[1]
            # if entry not in Count table -> a wrong annotation have happend by panther DB        
            if correct_gene_name not in Zebrafish_CT_gene_list:
                pass
            else:
                # print out dublicates
                if correct_gene_name in Zebrafish_Gene_Uniprot_TransporterType:
                    if correct_gene_name not in Zebrafish_CT_gene_list:
                        pass
                    else:
                        # evaluate entries and write case handling of uniprot ids
                        if correct_gene_name == 'slc24a6a':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['A0A2R8PV75',line[4]]
                        elif correct_gene_name == 'slc44a2':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['Q7SYC9',line[4]]
                        elif correct_gene_name == 'slc5a8':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['Q3ZMH1',line[4]]
                        elif correct_gene_name == 'slc25a29':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['F1QHQ1',line[4]]
                        elif correct_gene_name == 'zmp:0000001102':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['E7F7N3',line[4]]
                        elif correct_gene_name == 'kcnq5b':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['F1RB62',line[4]]
                        elif correct_gene_name == 'atp11a':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['F8W2B0',line[4]]
                        elif correct_gene_name == 'cachd1':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['E7F5Q0',line[4]]
                        elif correct_gene_name == 'oca2':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['F8W4N1',line[4]] 
                        elif correct_gene_name == 'slc44a5b':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['B0S5A7',line[4]] 
                        elif correct_gene_name == 'flvcr2b':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['A0A2R8PZF0',line[4]] 
                        elif correct_gene_name == 'slc38a8b':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['A0A2R8QRL8',line[4]] 
                        elif correct_gene_name == 'atp8a2':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['A0A2R8QNN7',line[4]] 
                        elif correct_gene_name == 'slc24a5':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['Q49SH1',line[4]] 
                        elif correct_gene_name == 'slc6a16a':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['F1REB8',line[4]] 
                        elif correct_gene_name == 'cnga2b':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['A0A2R8RZU5',line[4]] 
                        elif correct_gene_name == 'slc47a1':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['A1L1P9',line[4]]
                        elif correct_gene_name == 'ano8b':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['E7F191',line[4]] 
                        elif correct_gene_name == 'pitpnab':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['F1QIB6',line[4]]
                        elif correct_gene_name == 'slc6a15':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['Q1LYS8',line[4]] 
                        elif correct_gene_name == 'kcnq3':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['F1RE25',line[4]]
                        elif correct_gene_name == 'slc39a5':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['F8W5D4',line[4]] 
                        elif correct_gene_name == 'pgap1':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['E9QJ74',line[4]]
                        elif correct_gene_name == 'slc16a12a':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['E7FGJ9',line[4]]
                        elif correct_gene_name == 'slc24a1':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['F1R8N3',line[4]]
                        elif correct_gene_name == 'mfsd4b':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['A4QN56',line[4]]
                        elif correct_gene_name == 'slc4a4b':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['A0A2R8QJJ4',line[4]]
                        elif correct_gene_name == 'kcng3':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['U3JA85',line[4]]
                        elif correct_gene_name == 'tnpo1':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['F1RDR1',line[4]]
                        elif correct_gene_name == 'slc5a7a':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['F1Q620',line[4]]
                        elif correct_gene_name == 'TMC1':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['F1QFU0',line[4]]
                        elif correct_gene_name == 'slc44a5a':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['A5PMW0',line[4]]
                        elif correct_gene_name == 'abch1':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['E7F3Y5',line[4]]
                        elif correct_gene_name == 'slc16a13':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['A0A2R8QIL1',line[4]]
                        elif correct_gene_name == 'xkr6a':
                            Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = ['A0A2R8RWC9',line[4]]                
                        else:    
                            print("uniprot incorrect",correct_gene_name,uniprot)
                            print(correct_gene_name,Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name])
                else:
                    Zebrafish_Gene_Uniprot_TransporterType[correct_gene_name] = [uniprot,line[4]]    
read.close()

# Add all ensembl entries to Transporter list #
for key in Zebrafish_Ensembl_Uniprot_TransporterType:
    if key not in Zebrafish_Transporter_list:
        Zebrafish_Transporter_list.append(key)
    else:
        print("this key is a dublicate",key)
    if key not in Zebrafish_transporter_dict_TransporterType:
        Zebrafish_transporter_dict_TransporterType[key] = [CT_dict_Zebrafish[key],Zebrafish_Ensembl_Uniprot_TransporterType[key][0],Zebrafish_Ensembl_Uniprot_TransporterType[key][1]]
    else:
        print("This key is a dublicate in the final transporter dict")
Zebrafish_gene_PASS = 'No'
Zebrafish_gene_PASS_length = 'Yes'
## lookup all additional genes from gene name dict and add ensembls to transporter list ##
Zebrafish_dublicate_control_check = {}
for key in Zebrafish_Gene_Uniprot_TransporterType:
    for item in CT_dict_Zebrafish:
        if key == CT_dict_Zebrafish[item]:
            if key not in Zebrafish_dublicate_control_check:
                Zebrafish_dublicate_control_check[key] = []
                Zebrafish_dublicate_control_check[key].append(item)
            else:
                Zebrafish_dublicate_control_check[key].append(item)
        else:
            pass
## Check entries and manually append correct entries ##
"""
for key in Zebrafish_dublicate_control_check:
    if len(Zebrafish_dublicate_control_check[key]) > 1:
        print("dublicate found",key,Zebrafish_dublicate_control_check[key])
        Zebrafish_gene_PASS_length = 'No'
    else:
        pass
if len(Zebrafish_dublicate_control_check) == len(Zebrafish_Gene_Uniprot_TransporterType):
    print("Zebrafish gene dublicate check passed")
    Zebrafish_gene_PASS = 'Yes'
else:
    print("Zebrafish gene dublicate check NOT passed")
    print("length of dublicate {} does not equal length of Gene_Uniprot_transporterType {}".format(len(Zebrafish_dublicate_control_check),len(Zebrafish_Gene_Uniprot_TransporterType)))
"""
Zebrafish_dublicate_key_counter = 0
#if Zebrafish_gene_PASS == 'Yes' and Zebrafish_gene_PASS_length == 'Yes':
for key in Zebrafish_dublicate_control_check:
    if len(Zebrafish_dublicate_control_check[key]) > 1:
        for item in Zebrafish_dublicate_control_check[key]:
            Zebrafish_additional_ensembl_entries[item] = key
    else:
        Zebrafish_additional_ensembl_entries[Zebrafish_dublicate_control_check[key][0]] = key
for key in Zebrafish_additional_ensembl_entries:
    if key in Zebrafish_transporter_dict_TransporterType:
        Zebrafish_dublicate_key_counter += 1
    else:
        Zebrafish_transporter_dict_TransporterType[key] = [Zebrafish_additional_ensembl_entries[key],Zebrafish_Gene_Uniprot_TransporterType[Zebrafish_additional_ensembl_entries[key]][0],Zebrafish_Gene_Uniprot_TransporterType[Zebrafish_additional_ensembl_entries[key]][1]]
"""
else:
    print("Zebrafish gene PASS not correct...")
"""
print("zebrafish cleared")

### Print transporter lists to files ###
## Rat ##
with open(os.path.join(Folder3,out_file_rat),'w+') as out:
    out.write("Ensembl ID;Gene symbol;Uniprot ID;Transporter type\n")
    for key in Rat_transporter_dict_TransporterType:
        if Rat_transporter_dict_TransporterType[key][2] == 'ATP synthase(PC00002)' or Rat_transporter_dict_TransporterType[key][2] == 'mitochondrial carrier protein(PC00158)':
            pass
        else:
            out.write("{};{}\n".format(key,";".join(Rat_transporter_dict_TransporterType[key])))
out.close()

## Human ##
with open(os.path.join(Folder3,out_file_human),'w+') as out:
    out.write("Ensembl ID;Gene symbol;Uniprot ID;Transporter type\n")
    for key in Human_transporter_dict_TransporterType:
        if Human_transporter_dict_TransporterType[key][2] == 'ATP synthase(PC00002)' or Human_transporter_dict_TransporterType[key][2] == 'mitochondrial carrier protein(PC00158)':
            pass
        else:
            out.write("{};{}\n".format(key,";".join(Human_transporter_dict_TransporterType[key])))
out.close()

## Mouse ##
with open(os.path.join(Folder3,out_file_mouse),'w+') as out:
    out.write("Ensembl ID;Gene symbol;Uniprot ID;Transporter type\n")
    for key in Mouse_transporter_dict_TransporterType:
        if Mouse_transporter_dict_TransporterType[key][2] == 'ATP synthase(PC00002)' or Mouse_transporter_dict_TransporterType[key][2] == 'mitochondrial carrier protein(PC00158)':
            pass
        else:
            out.write("{};{}\n".format(key,";".join(Mouse_transporter_dict_TransporterType[key])))
out.close()

## Zebrafish ##
with open(os.path.join(Folder3,out_file_zebrafish),'w+') as out:
    out.write("Ensembl ID;Gene symbol;Uniprot ID;Transporter type\n")
    for key in Zebrafish_transporter_dict_TransporterType:
        if Zebrafish_transporter_dict_TransporterType[key][2] == 'ATP synthase(PC00002)' or Zebrafish_transporter_dict_TransporterType[key][2] == 'mitochondrial carrier protein(PC00158)':
            pass
        else:
            out.write("{};{}\n".format(key,";".join(Zebrafish_transporter_dict_TransporterType[key])))
out.close()
    