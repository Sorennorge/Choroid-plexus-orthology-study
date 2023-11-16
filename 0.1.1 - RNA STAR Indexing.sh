#!/bin/sh
STAR --runMode genomeGenerate \
    --genomeDir "Index-folder" \
    --sjdbGTFfile "GTF-file" \
    --genomeFastaFiles "DNA-toplevel-FASTA" \
    --runThreadN 28 \
    --outFileNamePrefix "Index-folder/Log-Folder"