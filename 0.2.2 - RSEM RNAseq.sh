#!/bin/sh

in_dir="RNA-STAR-Output-Folder" \
mysample=$in_dir"Sample-Folder/"
rsem_dir=$in_dir"Sample-Folder/rsem/rsem"

rsem-calculate-expression --bam --no-bam-output -p 28 --paired-end --forward-prob 0 $mysample"Aligned.toTranscriptome.out.bam" "RSEM-Index-Folder" $rsem_dir >& $rsem_dir"/rsem.log"
