# -*- coding: utf-8 -*-

### Create orthology matrix summaries for transporter venn plots ###

## input parameters ##

sanity_check = 0 #if 1 print sanity check, anything else - skip print

## Libraries ##

import os

## functions ##

def check_exist(folder,file):
    return os.path.exists(os.path.join(folder,file))

## Folders ##

folder1 = "Data/Transporter Lists"
folder2 = "Data/Gene lists/Transporters/All genes"

out_folder = "Results/Summary matrices/Transporters (all genes)"

os.makedirs(out_folder,exist_ok=True)

## files ##

file_CT_rat = "Transporter_list_concatenated_rat.csv"
file_CT_human = "Transporter_list_concatenated_human.csv"
file_CT_zebrafish = "Transporter_list_concatenated_zebrafish.csv"
file_CT_mouse = "Transporter_list_concatenated_mouse.csv"

file_rat_shared_all = "Shared_orthologues_gene_in_all_species_list_Rat.csv"
file_human_shared_all = "Shared_orthologues_gene_in_all_species_list_Human.csv"
file_zebrafish_shared_all = "Shared_orthologues_gene_in_all_species_list_Zebrafish.csv"
file_mouse_shared_all = "Shared_orthologues_gene_in_all_species_list_Mouse.csv"

file_single_shared_rat = "Single_species_shared_analysis_Rat.csv"
file_single_shared_human = "Single_species_shared_analysis_Human.csv"
file_single_shared_zebrafish = "Single_species_shared_analysis_Zebrafish.csv"
file_single_shared_mouse = "Single_species_shared_analysis_Mouse.csv"

file_summary_matrix = "Summary matrix table transporters all.csv"

## Variables ##

CT_rat = []
CT_human = []
CT_zebrafish = []
CT_mouse = []

Shared_all_rat = []
Shared_all_human = []
Shared_all_zebrafish = []
Shared_all_mouse = []

Single_rat = []
Single_human = []
Single_zebrafish = []
Single_mouse = []

Single_dict_rat = {}
Single_dict_human = {}
Single_dict_zebrafish = {}
Single_dict_mouse = {}

Summary_dict_rat = {}
Summary_dict_human = {}
Summary_dict_zebrafish = {}
Summary_dict_mouse = {}

# error key for missing input #
error_input_key = 0

## read files ##

if check_exist(folder1, file_CT_rat) and check_exist(folder1, file_CT_human) and check_exist(folder1, file_CT_zebrafish) and check_exist(folder1, file_CT_mouse):
    # Read count tables
    # Rat file #
    print("Reading count tables...")
    with open(os.path.join(folder1,file_CT_rat),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            CT_rat.append(line[0])            
    read.close
    # human file #
    with open(os.path.join(folder1,file_CT_human),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            CT_human.append(line[0]) 
    read.close
    # zebrafish file #
    with open(os.path.join(folder1,file_CT_zebrafish),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            CT_zebrafish.append(line[0])  
    read.close
    # Mouse file #
    with open(os.path.join(folder1,file_CT_mouse),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            CT_mouse.append(line[0])
    read.close
    print("Done.")
else:
    print("Missing count tables files.")
    error_input_key = 1

if check_exist(folder2, file_rat_shared_all) and check_exist(folder2, file_human_shared_all) and check_exist(folder2, file_zebrafish_shared_all) and check_exist(folder2, file_mouse_shared_all):
    ## read shared gene lists in all species ##
    print("Reading shared in all tables...")
    with open(os.path.join(folder2,file_rat_shared_all),'r') as read:
        for line in read:
            line = line.strip()
            Shared_all_rat.append(line)
    read.close()
    with open(os.path.join(folder2,file_human_shared_all),'r') as read:
        for line in read:
            line = line.strip()
            Shared_all_human.append(line)
    read.close()
    with open(os.path.join(folder2,file_zebrafish_shared_all),'r') as read:
        for line in read:
            line = line.strip()
            Shared_all_zebrafish.append(line)
    read.close()
    with open(os.path.join(folder2,file_mouse_shared_all),'r') as read:
        for line in read:
            line = line.strip()
            Shared_all_mouse.append(line)
    read.close()
    print("Done.")
else:
    print("Missing all shared files.")
    error_input_key = 1
    
if check_exist(folder2, file_single_shared_rat) and check_exist(folder2, file_single_shared_human) and check_exist(folder2, file_single_shared_zebrafish) and check_exist(folder2, file_single_shared_mouse):
    ## read shared gene lists in single species ##
    print("Reading shared genes in single species tables...")
    with open(os.path.join(folder2,file_single_shared_rat),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            Single_rat.append(line[0])
            Single_dict_rat[line[0]] = line[1:]
    read.close()
    with open(os.path.join(folder2,file_single_shared_human),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            Single_human.append(line[0])
            Single_dict_human[line[0]] = line[1:]
    read.close()
    with open(os.path.join(folder2,file_single_shared_zebrafish),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            Single_zebrafish.append(line[0])
            Single_dict_zebrafish[line[0]] = line[1:]
    read.close()
    with open(os.path.join(folder2,file_single_shared_mouse),'r') as read:
        next(read)
        for line in read:
            line = line.strip().split(";")
            Single_mouse.append(line[0])
            Single_dict_mouse[line[0]] = line[1:]
    read.close()
    print("Done.")
else:
    print("Missing shared in single species files.")
    error_input_key = 1
    
if error_input_key == 0:
    ## if print sanity check == 1 print: ##
    if sanity_check == 1:
        print("Sanity check")
        print("Species - All genes - shared all - shared single - leftover (should be zero) - leftover(entry specific)")
        subtracted_rat = list(set(CT_rat)-set(Shared_all_rat)-set(Single_rat))
        print("Rat - {} - {} - {} - {} - {}".format(len(CT_rat),len(Shared_all_rat),len(Single_rat),len(CT_rat)-len(Shared_all_rat)-len(Single_rat),len(subtracted_rat)))
        subtracted_human = list(set(CT_human)-set(Shared_all_human)-set(Single_human))
        print("Human - {} - {} - {} - {} - {}".format(len(CT_human),len(Shared_all_human),len(Single_human),len(CT_human)-len(Shared_all_human)-len(Single_human),len(subtracted_human)))
        subtracted_zebrafish = list(set(CT_zebrafish)-set(Shared_all_zebrafish)-set(Single_zebrafish))
        print("Zebrafish - {} - {} - {} - {} - {}".format(len(CT_zebrafish),len(Shared_all_zebrafish),len(Single_zebrafish),len(CT_zebrafish)-len(Shared_all_zebrafish)-len(Single_zebrafish),len(subtracted_zebrafish)))
        subtracted_mouse = list(set(CT_mouse)-set(Shared_all_mouse)-set(Single_mouse))
        print("Mouse - {} - {} - {} - {} - {}".format(len(CT_mouse),len(Shared_all_mouse),len(Single_mouse),len(CT_mouse)-len(Shared_all_mouse)-len(Single_mouse),len(subtracted_mouse)))
    else:
        ### summary dict analysis for the single species dicts ###
        ## Rat ##
        for key in Single_dict_rat:
            #All
            if 'R' in Single_dict_rat[key] and 'H' in Single_dict_rat[key] and 'Z' in Single_dict_rat[key] and'M' in Single_dict_rat[key]:
                print("Error - all species in single rat dict - re-analyse")
                break
            #RHZ
            elif 'R' in Single_dict_rat[key] and 'H' in Single_dict_rat[key] and 'Z' in Single_dict_rat[key]:
                if not 'RHZ' in Summary_dict_rat:
                    Summary_dict_rat['RHZ'] = 1
                else:
                    Summary_dict_rat['RHZ'] += 1
            #RZM
            elif  'R' in Single_dict_rat[key] and 'Z' in Single_dict_rat[key] and 'M' in Single_dict_rat[key]:
                if not 'RZM' in Summary_dict_rat:
                    Summary_dict_rat['RZM'] = 1
                else:
                    Summary_dict_rat['RZM'] += 1
            #RHM
            elif  'R' in Single_dict_rat[key] and 'H' in Single_dict_rat[key] and 'M' in Single_dict_rat[key]:
                if not 'RHM' in Summary_dict_rat:
                    Summary_dict_rat['RHM'] = 1
                else:
                    Summary_dict_rat['RHM'] += 1
            #HZM - no rat
            #RH
            elif  'R' in Single_dict_rat[key] and 'H' in Single_dict_rat[key]:
                if not 'RH' in Summary_dict_rat:
                    Summary_dict_rat['RH'] = 1
                else:
                    Summary_dict_rat['RH'] += 1
            #RZ
            elif  'R' in Single_dict_rat[key] and 'Z' in Single_dict_rat[key]:
                if not 'RZ' in Summary_dict_rat:
                    Summary_dict_rat['RZ'] = 1
                else:
                    Summary_dict_rat['RZ'] += 1
            #RM
            elif  'R' in Single_dict_rat[key] and 'M' in Single_dict_rat[key]:
                if not 'RM' in Summary_dict_rat:
                    Summary_dict_rat['RM'] = 1
                else:
                    Summary_dict_rat['RM'] += 1
            #HZ - not rat
            #HM - not rat
            #ZM - not rat
            #R
            elif  'R' in Single_dict_rat[key]:
                if not 'R' in Summary_dict_rat:
                    Summary_dict_rat['R'] = 1
                else:
                    Summary_dict_rat['R'] += 1
            #H - not rat
            #Z - not rat
            #M - not rat
            else:
                print("something very odd is going on in rat dict, try to get the data correct.")
        ## Human ##
        for key in Single_dict_human:
            #All
            if 'R' in Single_dict_human[key] and 'H' in Single_dict_human[key] and 'Z' in Single_dict_human[key] and'M' in Single_dict_human[key]:
                print("Error - all species in single human dict - re-analyse")
                break
            #RHZ
            elif 'R' in Single_dict_human[key] and 'H' in Single_dict_human[key] and 'Z' in Single_dict_human[key]:
                if not 'RHZ' in Summary_dict_human:
                    Summary_dict_human['RHZ'] = 1
                else:
                    Summary_dict_human['RHZ'] += 1
            #RZM - not human
            
            #RHM
            elif  'R' in Single_dict_human[key] and 'H' in Single_dict_human[key] and 'M' in Single_dict_human[key]:
                if not 'RHM' in Summary_dict_human:
                    Summary_dict_human['RHM'] = 1
                else:
                    Summary_dict_human['RHM'] += 1
            #HZM
            elif  'H' in Single_dict_human[key] and 'Z' in Single_dict_human[key] and 'M' in Single_dict_human[key]:
                if not 'HZM' in Summary_dict_human:
                    Summary_dict_human['HZM'] = 1
                else:
                    Summary_dict_human['HZM'] += 1
            #RH
            elif  'R' in Single_dict_human[key] and 'H' in Single_dict_human[key]:
                if not 'RH' in Summary_dict_human:
                    Summary_dict_human['RH'] = 1
                else:
                    Summary_dict_human['RH'] += 1
            #RZ - not human
            
            #RM - not human
            
            #HZ
            elif  'H' in Single_dict_human[key] and 'Z' in Single_dict_human[key]:
                if not 'HZ' in Summary_dict_human:
                    Summary_dict_human['HZ'] = 1
                else:
                    Summary_dict_human['HZ'] += 1
            #HM 
            elif  'H' in Single_dict_human[key] and 'M' in Single_dict_human[key]:
                if not 'HM' in Summary_dict_human:
                    Summary_dict_human['HM'] = 1
                else:
                    Summary_dict_human['HM'] += 1
            #ZM - not human
            #R - not human
            #H
            elif  'H' in Single_dict_human[key]:
                if not 'H' in Summary_dict_human:
                    Summary_dict_human['H'] = 1
                else:
                    Summary_dict_human['H'] += 1
            #Z - not human
            #M - not human
            else:
                print("something very odd is going on in human dict, try to get the data correct.")
        
        ## Zebrafish ##
        for key in Single_dict_zebrafish:
            #All
            if 'R' in Single_dict_zebrafish[key] and 'H' in Single_dict_zebrafish[key] and 'Z' in Single_dict_zebrafish[key] and'M' in Single_dict_zebrafish[key]:
                print("Error - all species in single zebrafish dict - re-analyse")
                break
            #RHZ
            elif 'R' in Single_dict_zebrafish[key] and 'H' in Single_dict_zebrafish[key] and 'Z' in Single_dict_zebrafish[key]:
                if not 'RHZ' in Summary_dict_zebrafish:
                    Summary_dict_zebrafish['RHZ'] = 1
                else:
                    Summary_dict_zebrafish['RHZ'] += 1
            #RZM
            elif  'R' in Single_dict_zebrafish[key] and 'Z' in Single_dict_zebrafish[key] and 'M' in Single_dict_zebrafish[key]:
                if not 'RZM' in Summary_dict_zebrafish:
                    Summary_dict_zebrafish['RZM'] = 1
                else:
                    Summary_dict_zebrafish['RZM'] += 1
            #RHM - not zebrafish
            #HZM
            elif  'H' in Single_dict_zebrafish[key] and 'Z' in Single_dict_zebrafish[key] and 'M' in Single_dict_zebrafish[key]:
                if not 'HZM' in Summary_dict_zebrafish:
                    Summary_dict_zebrafish['HZM'] = 1
                else:
                    Summary_dict_zebrafish['HZM'] += 1
            #RH  - not zebrafish
            #RZ
            elif  'R' in Single_dict_zebrafish[key] and 'Z' in Single_dict_zebrafish[key]:
                if not 'RZ' in Summary_dict_zebrafish:
                    Summary_dict_zebrafish['RZ'] = 1
                else:
                    Summary_dict_zebrafish['RZ'] += 1
            #RM - not zebrafish            
            #HZ
            elif  'H' in Single_dict_zebrafish[key] and 'Z' in Single_dict_zebrafish[key]:
                if not 'HZ' in Summary_dict_zebrafish:
                    Summary_dict_zebrafish['HZ'] = 1
                else:
                    Summary_dict_zebrafish['HZ'] += 1
            #HM - not zebrafish
            #ZM
            elif  'Z' in Single_dict_zebrafish[key] and 'M' in Single_dict_zebrafish[key]:
                if not 'ZM' in Summary_dict_zebrafish:
                    Summary_dict_zebrafish['ZM'] = 1
                else:
                    Summary_dict_zebrafish['ZM'] += 1
            #R - not zebrafish
            #H - not zebrafish
            #Z
            elif  'Z' in Single_dict_zebrafish[key]:
                if not 'Z' in Summary_dict_zebrafish:
                    Summary_dict_zebrafish['Z'] = 1
                else:
                    Summary_dict_zebrafish['Z'] += 1
            #M - not zebrafish
            else:
                print("something very odd is going on in zebrafish dict, try to get the data correct.")
        
        ## Mouse ##
        for key in Single_dict_mouse:
            #All
            if 'R' in Single_dict_mouse[key] and 'H' in Single_dict_mouse[key] and 'Z' in Single_dict_mouse[key] and'M' in Single_dict_mouse[key]:
                print("Error - all species in single mouse dict - re-analyse")
                break
            
            #RHZ - Not Mouse
            
            #RZM
            elif  'R' in Single_dict_mouse[key] and 'Z' in Single_dict_mouse[key] and 'M' in Single_dict_mouse[key]:
                if not 'RZM' in Summary_dict_mouse:
                    Summary_dict_mouse['RZM'] = 1
                else:
                    Summary_dict_mouse['RZM'] += 1
            #RHM
            elif  'R' in Single_dict_mouse[key] and 'H' in Single_dict_mouse[key] and 'M' in Single_dict_mouse[key]:
                if not 'RHM' in Summary_dict_mouse:
                    Summary_dict_mouse['RHM'] = 1
                else:
                    Summary_dict_mouse['RHM'] += 1
            #HZM
            elif 'H' in Single_dict_mouse[key] and 'Z' in Single_dict_mouse[key] and 'M' in Single_dict_mouse[key]:
                if not 'HZM' in Summary_dict_mouse:
                    Summary_dict_mouse['HZM'] = 1
                else:
                    Summary_dict_mouse['HZM'] += 1
            
            #RH - Not Mouse
            
            #RZ - Not Mouse
            
            #RM
            elif  'R' in Single_dict_mouse[key] and 'M' in Single_dict_mouse[key]:
                if not 'RM' in Summary_dict_mouse:
                    Summary_dict_mouse['RM'] = 1
                else:
                    Summary_dict_mouse['RM'] += 1
            
            #HZ - Not Mouse
           
            #HM
            elif  'H' in Single_dict_mouse[key] and 'M' in Single_dict_mouse[key]:
                if not 'HM' in Summary_dict_mouse:
                    Summary_dict_mouse['HM'] = 1
                else:
                    Summary_dict_mouse['HM'] += 1
            
            #ZM
            elif  'Z' in Single_dict_mouse[key] and 'M' in Single_dict_mouse[key]:
                if not 'ZM' in Summary_dict_mouse:
                    Summary_dict_mouse['ZM'] = 1
                else:
                    Summary_dict_mouse['ZM'] += 1
            
            #R - Not Mouse
            #H - Not Mouse
            #Z - Not Mouse
            
            #M
            elif  'M' in Single_dict_mouse[key]:
                if not 'M' in Summary_dict_mouse:
                    Summary_dict_mouse['M'] = 1
                else:
                    Summary_dict_mouse['M'] += 1
            else:
                print("something very odd is going on in mouse dict, try to get the data correct.")
                break
        ## add the last dict entries for easy output writing ##
        #ALL
        Summary_dict_rat['All'] = len(Shared_all_rat)
        Summary_dict_human['All'] = len(Shared_all_human)
        Summary_dict_zebrafish['All'] = len(Shared_all_zebrafish)
        Summary_dict_mouse['All'] = len(Shared_all_mouse)
        #RHZ
        Summary_dict_mouse['RHZ'] = 0
        #RZM
        Summary_dict_human['RZM'] = 0
        #RHM
        Summary_dict_zebrafish['RHM'] = 0
        #HZM
        Summary_dict_rat['HZM'] = 0
        #RH
        Summary_dict_zebrafish['RH'] = 0
        Summary_dict_mouse['RH'] = 0
        #RZ
        Summary_dict_human['RZ'] = 0
        Summary_dict_mouse['RZ'] = 0
        #RM
        Summary_dict_human['RM'] = 0
        Summary_dict_zebrafish['RM'] = 0
        #HZ
        Summary_dict_rat['HZ'] = 0
        Summary_dict_mouse['HZ'] = 0
        #HM
        Summary_dict_rat['HM'] = 0
        Summary_dict_zebrafish['HM'] = 0
        #ZM
        Summary_dict_rat['ZM'] = 0
        Summary_dict_human['ZM'] = 0
        
        #R
        Summary_dict_human['R'] = 0
        Summary_dict_zebrafish['R'] = 0
        Summary_dict_mouse['R'] = 0
        #H
        Summary_dict_rat['H'] = 0
        Summary_dict_zebrafish['H'] = 0
        Summary_dict_mouse['H'] = 0
        #Z
        Summary_dict_rat['Z'] = 0
        Summary_dict_human['Z'] = 0
        Summary_dict_mouse['Z'] = 0
        #M
        Summary_dict_rat['M'] = 0
        Summary_dict_human['M'] = 0
        Summary_dict_zebrafish['M'] = 0
        
        ## save summary matrices ##
        with open(os.path.join(out_folder,file_summary_matrix),'w+') as out:
            out.write("Category;Rat;Human;Zebrafish;Mouse;mean\n")
            # All
            mean_all = int(round((Summary_dict_rat['All']+Summary_dict_human['All']+Summary_dict_zebrafish['All']+Summary_dict_mouse['All'])/4,0))
            out.write("All;{};{};{};{};{}\n".format(Summary_dict_rat['All'],Summary_dict_human['All'],Summary_dict_zebrafish['All'],Summary_dict_mouse['All'],mean_all))
            #RHZ
            mean_RHZ = int(round((Summary_dict_rat['RHZ']+Summary_dict_human['RHZ']+Summary_dict_zebrafish['RHZ']+Summary_dict_mouse['RHZ'])/3,0))
            out.write("RHZ;{};{};{};{};{}\n".format(Summary_dict_rat['RHZ'],Summary_dict_human['RHZ'],Summary_dict_zebrafish['RHZ'],Summary_dict_mouse['RHZ'],mean_RHZ))
            #RZM
            mean_RZM = int(round((Summary_dict_rat['RZM']+Summary_dict_human['RZM']+Summary_dict_zebrafish['RZM']+Summary_dict_mouse['RZM'])/3,0))
            out.write("RZM;{};{};{};{};{}\n".format(Summary_dict_rat['RZM'],Summary_dict_human['RZM'],Summary_dict_zebrafish['RZM'],Summary_dict_mouse['RZM'],mean_RZM))
            #RHM
            mean_RHM = int(round((Summary_dict_rat['RHM']+Summary_dict_human['RHM']+Summary_dict_zebrafish['RHM']+Summary_dict_mouse['RHM'])/3,0))
            out.write("RHM;{};{};{};{};{}\n".format(Summary_dict_rat['RHM'],Summary_dict_human['RHM'],Summary_dict_zebrafish['RHM'],Summary_dict_mouse['RHM'],mean_RHM))
            #HZM
            mean_HZM = int(round((Summary_dict_rat['HZM']+Summary_dict_human['HZM']+Summary_dict_zebrafish['HZM']+Summary_dict_mouse['HZM'])/3,0))
            out.write("HZM;{};{};{};{};{}\n".format(Summary_dict_rat['HZM'],Summary_dict_human['HZM'],Summary_dict_zebrafish['HZM'],Summary_dict_mouse['HZM'],mean_HZM))
            #RH
            mean_RH = int(round((Summary_dict_rat['RH']+Summary_dict_human['RH']+Summary_dict_zebrafish['RH']+Summary_dict_mouse['RH'])/2,0))
            out.write("RH;{};{};{};{};{}\n".format(Summary_dict_rat['RH'],Summary_dict_human['RH'],Summary_dict_zebrafish['RH'],Summary_dict_mouse['RH'],mean_RH))
            #RZ
            mean_RZ = int(round((Summary_dict_rat['RZ']+Summary_dict_human['RZ']+Summary_dict_zebrafish['RZ']+Summary_dict_mouse['RZ'])/2,0))
            out.write("RZ;{};{};{};{};{}\n".format(Summary_dict_rat['RZ'],Summary_dict_human['RZ'],Summary_dict_zebrafish['RZ'],Summary_dict_mouse['RZ'],mean_RZ))
            #RM
            mean_RM = int(round((Summary_dict_rat['RM']+Summary_dict_human['RM']+Summary_dict_zebrafish['RM']+Summary_dict_mouse['RM'])/2,0))
            out.write("RM;{};{};{};{};{}\n".format(Summary_dict_rat['RM'],Summary_dict_human['RM'],Summary_dict_zebrafish['RM'],Summary_dict_mouse['RM'],mean_RM))
            #HZ
            mean_HZ = int(round((Summary_dict_rat['HZ']+Summary_dict_human['HZ']+Summary_dict_zebrafish['HZ']+Summary_dict_mouse['HZ'])/2,0))
            out.write("HZ;{};{};{};{};{}\n".format(Summary_dict_rat['HZ'],Summary_dict_human['HZ'],Summary_dict_zebrafish['HZ'],Summary_dict_mouse['HZ'],mean_HZ))
            #HM
            mean_HM = int(round((Summary_dict_rat['HM']+Summary_dict_human['HM']+Summary_dict_zebrafish['HM']+Summary_dict_mouse['HM'])/2,0))
            out.write("HM;{};{};{};{};{}\n".format(Summary_dict_rat['HM'],Summary_dict_human['HM'],Summary_dict_zebrafish['HM'],Summary_dict_mouse['HM'],mean_HM))
            #ZM
            mean_ZM = int(round((Summary_dict_rat['ZM']+Summary_dict_human['ZM']+Summary_dict_zebrafish['ZM']+Summary_dict_mouse['ZM'])/2,0))
            out.write("ZM;{};{};{};{};{}\n".format(Summary_dict_rat['ZM'],Summary_dict_human['ZM'],Summary_dict_zebrafish['ZM'],Summary_dict_mouse['ZM'],mean_ZM))
            #R
            mean_R = int(round((Summary_dict_rat['R']+Summary_dict_human['R']+Summary_dict_zebrafish['R']+Summary_dict_mouse['R'])/1,0))
            out.write("R;{};{};{};{};{}\n".format(Summary_dict_rat['R'],Summary_dict_human['R'],Summary_dict_zebrafish['R'],Summary_dict_mouse['R'],mean_R))
            #H
            mean_H = int(round((Summary_dict_rat['H']+Summary_dict_human['H']+Summary_dict_zebrafish['H']+Summary_dict_mouse['H'])/1,0))
            out.write("H;{};{};{};{};{}\n".format(Summary_dict_rat['H'],Summary_dict_human['H'],Summary_dict_zebrafish['H'],Summary_dict_mouse['H'],mean_H))
            #Z
            mean_Z = int(round((Summary_dict_rat['Z']+Summary_dict_human['Z']+Summary_dict_zebrafish['Z']+Summary_dict_mouse['Z'])/1,0))
            out.write("Z;{};{};{};{};{}\n".format(Summary_dict_rat['Z'],Summary_dict_human['Z'],Summary_dict_zebrafish['Z'],Summary_dict_mouse['Z'],mean_Z))
            #M
            mean_M = int(round((Summary_dict_rat['M']+Summary_dict_human['M']+Summary_dict_zebrafish['M']+Summary_dict_mouse['M'])/1,0))
            out.write("M;{};{};{};{};{}\n".format(Summary_dict_rat['M'],Summary_dict_human['M'],Summary_dict_zebrafish['M'],Summary_dict_mouse['M'],mean_M))
        out.close()
else:
    print("An error has occured.")
