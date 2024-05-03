# Choroid plexus orthology study

## Introduction
The work and scripts are done by the MacAulay Lab in collaboration with the Jurisch-Yaksi Lab. \
All programs used are free and open-source. In the interest of open science and reproducibility, all data and source code used in our research is provided here. \
Feel free to copy and use code, but please cite: \
https://www.biorxiv.org/content/10.1101/2023.11.03.565468v1 \
Remember rewrite file_names and folder_names suitable for your pipeline. 
## Requirements ##
To be able to run all scripts you need:\
(1) Various RNA sequencing data from human, rat, mouse, and zebrafish.\
In these scripts these are located in "Data/RNA STAR/sub_folders (Human, Rat, Mouse, And Zebrafish)"\
(2) A folder with 4 biomart gene info files (generated at https://www.ensembl.org/biomart/martview) containing Ensembl IDs and Gene Symbols.\
In these scripts these are located in "Data/Biomart/Gene info"\
(3) A folder with 4 ortholog matrices from either the human, rat, mouse, and zebrafishs perspective (also generated with https://www.ensembl.org/biomart/martview) \
In these scripts these are located in "Data/Biomart/Ortholog matrices" \
(4) Transporter gene lists (required for 6.1.1) genereated with the Panther database (https://www.pantherdb.org/)

## The RNAseq Analysis follows these steps:
## Raw data analysis - Library Build, Mapping and Quantification ##
The analysis uses RNA STAR for mapping and RSEM for TPM quantification.
### RNA-STAR and RSEM Library build and indexing ###

0.1.1 - RNA_STAR_Indexing.sh \
0.2.1 - RSEM_Indexing.sh

### RNA-STAR Mapping and RSEM quantification ###

0.1.2 -RNA_STAR_RNAseq2.sh \
0.2.2 - RSEM_RNAseq2.sh

### Generate count tables ###
1.1.1 Generate count tables from raw data.py

## Ortholog analysis ##
### Create ortholog matrix for all species ###
1.2.1 - Complete Ortholog matrix with all species.py

### Reduce count tables to orthologeus genes ###
1.2.2 - Filter count tables to orthologous genes.py

### Calculate all shared genes in all species ###
2.1.1 - Ortholog shared in all species.py

### Bar plot - orthologeus genes ###
3.1.1 - Create matrix for bar plot.py \
3.1.2 - Bar plot.py

### Orthologeus gene analysis between species (single) ##
4.1.1 - Ortholog matrix for single species with not shared gene lists.py \
4.1.2 - Ortholog shared in single species.py
### Create venn diagrams for orthologeus genes ##
4.1.3 - Create orthology matricx for venn plot.py \
4.1.4 - Venndiagram of orthology study.R

### Orthologeus genes for species - all genes ###
5.1.1 - Ortholog shared in all species.py \
5.1.2 - Ortholog matrix for single species with not shared gene lists.py \
5.1.3 - Ortholog shared in single species.py

### Create venn diagram (orthologeus genes) for all genes between species ###
5.1.4 - Create orthology matricx for venn plot.py \
5.1.5 - Venndiagram of orthology study.R

## Transport analysis ##
### utializing panther database to collect transporters ###
6.1.1 Concatenate ensembl and gene lists from panther.py

### Orthologues transporters between species (all genes) ###
7.1.1 Orthology of transporters in all species.py \
7.1.2 - Ortholog matrix for single species with not shared gene lists.py \
7.1.3 - Orthology of transporters shared in single species.py

### Create venn diagram for transporters ###
7.1.4 - Create orthology matrix for transporter venn plot.py \
7.1.5 - Venndiagram of orthology study Transporters.R

### Transport analysis ###
8.1.1 - Extract orholog transporters.py \
8.1.2 - Orthology of transporters in species (ortholog genes).py \
8.1.3 - Ortholog matrix for single species with not shared gene lists (ortholog genes).py \
8.1.4 - Orthology of transporters shared in single species (ortholog genes).py

### Create venn diagram - transport ###
8.1.5 - Create orthology matrix for transporter (ortholog genes) venn plot.py \
8.1.6 - Venndiagram of orthology study Transporters (ortholog genes).R

### Calculate TPM for transport genes ##
9.1.1 - TPM of shared transporters.py

### Assign rank to transport genes ##
9.1.2 - Create Ranked Shared Gene Lists.py \
9.1.3 - Create Ortholog matrix for all shared Transporters.py \
9.2.1 - Create prematrix for ortholog transport.py \
9.2.2 - Add sum and rank to ortholog transport matrix.py

### Create heatmap of transport ###
9.3.1 - Heatmap transporters.py

### Generate heatmap for transporters of interest (CSF) ###
10.1.1 - Create matrix for transporters of interest.py \
10.1.2 - Heatmap for transporters of interest.py
