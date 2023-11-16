# -*- coding: utf-8 -*-

### Orthology of transporters ###

## Program parameters ##

print_output = "yes" # "yes" print output, anything else save to files
print_output = "no"

# Libraries ##

import os

## functions ##

def check_exist(folder,file):
    return os.path.exists(os.path.join(folder,file))

## Folders ##

folder1 = "Data/Biomart"
folder2 = "Data/Transporter Lists/Ortholog genes"
folder3 = "Data/Gene lists/Transporters/Ortholog genes"

os.makedirs(folder3,exist_ok=True)

## Files ##

rat_file = "Transporter_list_concatenated_rat_ortholog.csv"
human_file = "Transporter_list_concatenated_human_ortholog.csv"
zebrafish_file = "Transporter_list_concatenated_zebrafish_ortholog.csv"
mouse_file = "Transporter_list_concatenated_mouse_ortholog.csv"

Ortholog_matrix_file = "Complete_Ortholog_Matrix.csv"

## output files ##
out_rat_file_shared_all = "Shared_orthologues_gene_in_all_species_list_Rat.csv"
out_human_file_shared_all = "Shared_orthologues_gene_in_all_species_list_Human.csv"
out_zebrafish_file_shared_all = "Shared_orthologues_gene_in_all_species_list_Zebrafish.csv"
out_mouse_file_shared_all = "Shared_orthologues_gene_in_all_species_list_Mouse.csv"

out_rat_file_not_shared = "Not_Shared_orthologues_gene_in_all_species_list_Rat.csv"
out_human_file_not_shared = "Not_Shared_orthologues_gene_in_all_species_list_Human.csv"
out_zebrafish_file_not_shared = "Not_Shared_orthologues_gene_in_all_species_list_Zebrafish.csv"
out_mouse_file_not_shared = "Not_Shared_orthologues_gene_in_all_species_list_Mouse.csv"


## Global variables ##

Ortholog_matrix = []

CT_rat_entries = []
CT_human_entries = []
CT_zebrafish_entries = []
CT_mouse_entries = []

Orthologs_shared_rat = []
Orthologs_shared_human = []
Orthologs_shared_zebrafish = []
Orthologs_shared_mouse = []


# check if all files are there and stop script if not ##

if check_exist(folder1,Ortholog_matrix_file):
    if check_exist(folder2, rat_file) and check_exist(folder2, human_file) and check_exist(folder2, zebrafish_file) and check_exist(folder2, mouse_file):
        ### Orthology in the all species ###
        print("Reading ortholog matrix...")
        # Read length of matrix file for progression output #
        with open(os.path.join(folder1,Ortholog_matrix_file),'r') as read:
            for count, line in enumerate(read):
                pass
        read.close()
        Length_matrix = int((count+1)/100)
        # Set progression counter #
        progress_counter = 0
        percentage = 0
        # Read matrix file #
        with open(os.path.join(folder1,Ortholog_matrix_file),'r') as read:
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
        
        ### read count trables ###
        # Rat file #
        print("Reading count tables...")
        with open(os.path.join(folder2,rat_file),'r') as read:
            next(read)
            for line in read:
                line = line.strip().split(";")
                CT_rat_entries.append(line[0])            
        read.close
        # human file #
        with open(os.path.join(folder2,human_file),'r') as read:
            next(read)
            for line in read:
                line = line.strip().split(";")
                CT_human_entries.append(line[0]) 
        read.close
        # zebrafish file #
        with open(os.path.join(folder2,zebrafish_file),'r') as read:
            next(read)
            for line in read:
                line = line.strip().split(";")
                CT_zebrafish_entries.append(line[0])  
        read.close
        # Mouse file #
        with open(os.path.join(folder2,mouse_file),'r') as read:
            next(read)
            for line in read:
                line = line.strip().split(";")
                CT_mouse_entries.append(line[0])
        read.close
        print("done.")
            
        ## Rat ortholog counting ##
        # progress output reset #
        print("Orthology analysis")
        progress_counter = 0
        percentage = 0
        # Run orthology program #
        
        for key in Ortholog_matrix:
            if key[0] in CT_rat_entries and key[1] in CT_human_entries and key[2] in CT_zebrafish_entries and key[3] in CT_mouse_entries:
                Orthologs_shared_rat.append(key[0])
                Orthologs_shared_human.append(key[1])
                Orthologs_shared_zebrafish.append(key[2])
                Orthologs_shared_mouse.append(key[3])
            else:
                pass
            # Progression #
            if progress_counter % round(len(Ortholog_matrix)/100,0) == 0:
                percentage += 1
                if percentage < 101:
                    if percentage % 10 == 0:
                        print("Orthology analysis - Progress: {} / 100 %".format(percentage))
            progress_counter += 1
        
        # reduce the shared gene lists #
        Reduced_orthologs_shared_rat = list(set(Orthologs_shared_rat))
        Reduced_orthologs_shared_human = list(set(Orthologs_shared_human))
        Reduced_orthologs_shared_zebrafish = list(set(Orthologs_shared_zebrafish))
        Reduced_orthologs_shared_mouse = list(set(Orthologs_shared_mouse))
        
        # Calculate the percentage of shared genes #
        percent_rat = round(len(Reduced_orthologs_shared_rat)/len(CT_rat_entries)*100,2)
        percent_human = round(len(Reduced_orthologs_shared_human)/len(CT_human_entries)*100,2)
        percent_zebrafish = round(len(Reduced_orthologs_shared_zebrafish)/len(CT_zebrafish_entries)*100,2)
        percent_mouse = round(len(Reduced_orthologs_shared_mouse)/len(CT_mouse_entries)*100,2)
        
        # create lists of non shared genes for further analysis #
        Non_shared_entries_rat =list(set(CT_rat_entries)-set(Reduced_orthologs_shared_rat))
        Non_shared_entries_human =list(set(CT_human_entries)-set(Reduced_orthologs_shared_human))
        Non_shared_entries_zebrafish =list(set(CT_zebrafish_entries)-set(Reduced_orthologs_shared_zebrafish))
        Non_shared_entries_mouse =list(set(CT_mouse_entries)-set(Reduced_orthologs_shared_mouse))
        
        
        # if print_output equals yes, then print else pass
        if print_output == "yes":
            print("Print output == yes")
            print("Species|Genes in species|Shared among all|Percentage shared|Non shared|sanity check (should be zero)")
            print("Rat|{}|{}|{}|{}|{}".format(len(CT_rat_entries),len(Reduced_orthologs_shared_rat),percent_rat,len(Non_shared_entries_rat),len(CT_rat_entries)-len(Reduced_orthologs_shared_rat)-len(Non_shared_entries_rat)))
            print("Human|{}|{}|{}|{}|{}".format(len(CT_human_entries),len(Reduced_orthologs_shared_human),percent_human,len(Non_shared_entries_human),len(CT_human_entries)-len(Reduced_orthologs_shared_human)-len(Non_shared_entries_human)))
            print("Zebrafish|{}|{}|{}|{}|{}".format(len(CT_zebrafish_entries),len(Reduced_orthologs_shared_zebrafish),percent_zebrafish,len(Non_shared_entries_zebrafish),len(CT_zebrafish_entries)-len(Reduced_orthologs_shared_zebrafish)-len(Non_shared_entries_zebrafish)))
            print("Mouse|{}|{}|{}|{}|{}".format(len(CT_mouse_entries),len(Reduced_orthologs_shared_mouse),percent_mouse,len(Non_shared_entries_mouse),len(CT_mouse_entries)-len(Reduced_orthologs_shared_mouse)-len(Non_shared_entries_mouse)))
        else:
            pass
        
        ## Save shared ortholog gene lists ##
        with open(os.path.join(folder3,out_rat_file_shared_all),'w+') as out:
            for key in Reduced_orthologs_shared_rat:
               out.write("{}\n".format(key))
        read.close
        
        # Human #
        with open(os.path.join(folder3,out_human_file_shared_all),'w+') as out:
           for key in Reduced_orthologs_shared_human:
               out.write("{}\n".format(key))
        read.close
        
        # zebrafish #
        with open(os.path.join(folder3,out_zebrafish_file_shared_all),'w+') as out:
           for key in Reduced_orthologs_shared_zebrafish:
               out.write("{}\n".format(key))
        read.close
        
        # Mouse #
        with open(os.path.join(folder3,out_mouse_file_shared_all),'w+') as out:
           for key in Reduced_orthologs_shared_mouse:
               out.write("{}\n".format(key))
        read.close
        
        ## Save non shared ortholog gene lists ##
        # Rat #
        with open(os.path.join(folder3,out_rat_file_not_shared),'w+') as out:
            for key in Non_shared_entries_rat:
               out.write("{}\n".format(key))
        read.close
        
        # Human #
        with open(os.path.join(folder3,out_human_file_not_shared),'w+') as out:
           for key in Non_shared_entries_human:
               out.write("{}\n".format(key))
        read.close
        
        # zebrafish #
        with open(os.path.join(folder3,out_zebrafish_file_not_shared),'w+') as out:
           for key in Non_shared_entries_zebrafish:
               out.write("{}\n".format(key))
        read.close
        
        # Mouse #
        with open(os.path.join(folder3,out_mouse_file_not_shared),'w+') as out:
           for key in Non_shared_entries_mouse:
               out.write("{}\n".format(key))
        read.close
    else:
        print("Count tables are missing or incorrect.")
else:
    print("Ortholog matrix are missing.")