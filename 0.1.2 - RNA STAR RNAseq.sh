#!/bin/sh
my_sample_dir="Raw-data-folder" \

R1=$my_sample_dir"Sample-file_1.fq.gz" \ #Forward
R2=$my_sample_dir"Sample-file_2.fq.gz" \ #Reverse
Output_dir="Output-folder/" \
mysample=$Output_dir"Sample-Folder/"

STAR --genomeDir "Index-Folder" \
--sjdbGTFfile "GTF-File" \
--runThreadN 28 \
--readFilesIn <(zcat $R1) <(zcat $R2) \
--sjdbOverhang 100 \
--outSAMtype BAM SortedByCoordinate \
--outSAMunmapped Within \
--quantMode TranscriptomeSAM \
--outFileNamePrefix $mysample
