# -*- coding: utf-8 -*-

### Orthology in non shared transporters in all species --> single species analysis ###

## Libraries ##

import os

## functions ##

def check_exist(folder,file):
    return os.path.exists(os.path.join(folder,file))

## Folders ##

folder1 = "Data/Biomart/Transporters/All genes"
folder2 = "Data/Gene lists/Transporters/All genes"

## files ##

file_not_shared_rat = "Not_Shared_orthologues_gene_in_all_species_list_Rat.csv"
file_not_shared_human = "Not_Shared_orthologues_gene_in_all_species_list_Human.csv"
file_not_shared_zebrafish = "Not_Shared_orthologues_gene_in_all_species_list_Zebrafish.csv"
file_not_shared_mouse = "Not_Shared_orthologues_gene_in_all_species_list_Mouse.csv"

out_file_rat = "Single_species_shared_analysis_Rat.csv"
out_file_human = "Single_species_shared_analysis_Human.csv"
out_file_zebrafish = "Single_species_shared_analysis_Zebrafish.csv"
out_file_mouse = "Single_species_shared_analysis_Mouse.csv"

Complete_orto_single_matrix_file = "Complete_Ortholog_single_species_Matrix.csv"

### Variables ###

non_shared_rat = []
non_shared_human = []
non_shared_mouse = []
non_shared_zebrafish = []

Ortholog_matrix = []

Orthology_dict_rat = {}
Orthology_dict_human = {}
Orthology_dict_zebrafish = {}
Orthology_dict_mouse = {}

reduced_Orthology_dict_rat = {}
reduced_Orthology_dict_human = {}
reduced_Orthology_dict_zebrafish = {}
reduced_Orthology_dict_mouse = {}

## Read files ##

if check_exist(folder1,Complete_orto_single_matrix_file):
    if check_exist(folder2, file_not_shared_rat) and check_exist(folder2, file_not_shared_human) and check_exist(folder2, file_not_shared_zebrafish) and check_exist(folder2, file_not_shared_mouse):
        ### Orthology in the all species ###
        print("Reading ortholog matrix...")
        # Read length of matrix file for progression output #
        with open(os.path.join(folder1,Complete_orto_single_matrix_file),'r') as read:
            for count, line in enumerate(read):
                pass
        read.close()
        Length_matrix = int((count+1)/100)
        # Set progression counter #
        progress_counter = 0
        percentage = 0
        # Read matrix file #
        with open(os.path.join(folder1,Complete_orto_single_matrix_file),'r') as read:
            next(read)
            for line in read:
                line = line.strip().split(";")
                Ortholog_matrix.append(line)
                # Progress counter
                if progress_counter % Length_matrix == 0:
                    percentage += 1
                    if percentage % 10 == 0:
                        print("Reading Matrix file - Progress: {} / 100 %".format(percentage))
                progress_counter += 1
        read.close
        print("done.")
        
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
        
        print("Orthology analysis")
        progress_counter = 0
        percentage = 0
        ### Run orthology program ###
        for key in Ortholog_matrix:
            ## Rat ##
            if key[0] in non_shared_rat:
                # if key not in ortholog rat dict, create key
                if not key[0] in Orthology_dict_rat:
                    Orthology_dict_rat[key[0]] = ['R']
                else:
                    pass
                # If ortholog genes are in human
                if key[1] in non_shared_human:
                    Orthology_dict_rat[key[0]].append("H")
                else:
                    pass
                # If ortholog genes are in zebrafish
                if key[2] in non_shared_zebrafish:
                    Orthology_dict_rat[key[0]].append("Z")
                else:
                    pass
                # If ortholog genes are in mouse
                if key[3] in non_shared_mouse:
                    Orthology_dict_rat[key[0]].append("M")
                else:
                    pass
            else:
                pass
            ## Human ##
            if key[1] in non_shared_human:
                # if key not in ortholog human dict, create key
                if not key[1] in Orthology_dict_human:
                    Orthology_dict_human[key[1]] = ['H']
                else:
                    pass
                # If ortholog genes are in human
                if key[0] in non_shared_rat:
                    Orthology_dict_human[key[1]].append("R")
                else:
                    pass
                # If ortholog genes are in zebrafish
                if key[2] in non_shared_zebrafish:
                    Orthology_dict_human[key[1]].append("Z")
                else:
                    pass
                # If ortholog genes are in mouse
                if key[3] in non_shared_mouse:
                    Orthology_dict_human[key[1]].append("M")
                else:
                    pass
            else:
                pass
            ## Zebrafish ##
            if key[2] in non_shared_zebrafish:
                # if key not in ortholog zebrafish dict, create key
                if not key[2] in Orthology_dict_zebrafish:
                    Orthology_dict_zebrafish[key[2]] = ['Z']
                else:
                    pass
                # If ortholog genes are in human
                if key[0] in non_shared_rat:
                    Orthology_dict_zebrafish[key[2]].append("R")
                else:
                    pass
                # If ortholog genes are in zebrafish
                if key[1] in non_shared_human:
                    Orthology_dict_zebrafish[key[2]].append("H")
                else:
                    pass
                # If ortholog genes are in mouse
                if key[3] in non_shared_mouse:
                    Orthology_dict_zebrafish[key[2]].append("M")
                else:
                    pass
            else:
                pass
            ## mouse ##
            if key[3] in non_shared_mouse:
                # if key not in ortholog zebrafish dict, create key
                if not key[3] in Orthology_dict_mouse:
                    Orthology_dict_mouse[key[3]] = ['M']
                else:
                    pass
                # If ortholog genes are in human
                if key[0] in non_shared_rat:
                    Orthology_dict_mouse[key[3]].append("R")
                else:
                    pass
                # If ortholog genes are in zebrafish
                if key[1] in non_shared_human:
                    Orthology_dict_mouse[key[3]].append("H")
                else:
                    pass
                # If ortholog genes are in mouse
                if key[2] in non_shared_zebrafish:
                    Orthology_dict_mouse[key[3]].append("Z")
                else:
                    pass
            else:
                pass
                
            # Progression #
            if progress_counter % round(len(Ortholog_matrix)/100,0) == 0:
                percentage += 1
                if percentage < 101:
                    if percentage % 10 == 0: #if fast
                        print("Orthology analysis - Progress: {} / 100 %".format(percentage))
            progress_counter += 1
        
        ## Reducing lists ##
        # Rat #
        for key in Orthology_dict_rat:
            reduced_Orthology_dict_rat[key] = list(set(Orthology_dict_rat[key]))
        # Human #
        for key in Orthology_dict_human:
            reduced_Orthology_dict_human[key] = list(set(Orthology_dict_human[key]))
        # Zebrafish #
        for key in Orthology_dict_zebrafish:
            reduced_Orthology_dict_zebrafish[key] = list(set(Orthology_dict_zebrafish[key]))
        # Mouse #
        for key in Orthology_dict_mouse:
            reduced_Orthology_dict_mouse[key] = list(set(Orthology_dict_mouse[key]))
        
        ## Add non shared entries to orthology dicts ##
        # Rat #
        for key in non_shared_rat:
            if key not in reduced_Orthology_dict_rat:
                reduced_Orthology_dict_rat[key] = ['R']
            else:
                pass
        # Human #
        for key in non_shared_human:
            if key not in reduced_Orthology_dict_human:
                reduced_Orthology_dict_human[key] = ['H']
            else:
                pass
        # Rat #
        for key in non_shared_zebrafish:
            if key not in reduced_Orthology_dict_zebrafish:
                reduced_Orthology_dict_zebrafish[key] = ['Z']
            else:
                pass
        # Rat #
        for key in non_shared_mouse:
            if key not in reduced_Orthology_dict_mouse:
                reduced_Orthology_dict_mouse[key] = ['M']
            else:
                pass
        
        ## Save analysis lists for single species ##
        # Rat #
        with open(os.path.join(folder2,out_file_rat),'w+') as out:
            out.write("Ensembl;species orthology\n")
            for key in reduced_Orthology_dict_rat:
                out.write("{};{}\n".format(key,";".join(reduced_Orthology_dict_rat[key])))
        out.close()
        # Human #
        with open(os.path.join(folder2,out_file_human),'w+') as out:
            out.write("Ensembl;species orthology\n")
            for key in reduced_Orthology_dict_human:
                out.write("{};{}\n".format(key,";".join(reduced_Orthology_dict_human[key])))
        out.close()
        # Zebrafish #
        with open(os.path.join(folder2,out_file_zebrafish),'w+') as out:
            out.write("Ensembl;species orthology\n")
            for key in reduced_Orthology_dict_zebrafish:
                out.write("{};{}\n".format(key,";".join(reduced_Orthology_dict_zebrafish[key])))
        out.close()
        # Mouse #
        with open(os.path.join(folder2,out_file_mouse),'w+') as out:
            out.write("Ensembl;species orthology\n")
            for key in reduced_Orthology_dict_mouse:
                out.write("{};{}\n".format(key,";".join(reduced_Orthology_dict_mouse[key])))
        out.close()
    else:
        print("could not find non shared files.")
else:
    print("Matrix for single species are missing.")
    
    