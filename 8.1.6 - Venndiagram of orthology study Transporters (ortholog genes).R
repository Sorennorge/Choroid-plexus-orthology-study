# load Venn diagram package
library(VennDiagram)
library(grDevices)
library(nVennR)
library(rsvg)
library(grImport2)

# Set working directory #
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

## Folders ##
Folder_in = "Results/Summary matrices/Transporters (Ortholog genes)"
Folder_out = "Results/Images/Venn diagrams for Transporters (Ortholog genes)"

dir.create(Folder_out,recursive = TRUE,showWarnings = FALSE)

## Files ##

File_data <- "Summary matrix table Transporters (ortholog genes).csv"

File_out1 <- "VennDiagram_normal.png"
File_out2 <- "VennDiagram_SizeAdjusted.png"
File_out3 <- "VennDiagram_SizeAdjusted_clean.png"

# Load venn diagram data from orthology analysis
Orthology_data <- read.table(file.path(Folder_in,File_data), header=T, sep=";", stringsAsFactors=F)


### VennDiagram normal vectors ###

## The vector for normal venn is c(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15)
# and the individual numbers are "a1 = H", "a2 = HM", "a3 = M", "a4 = RH","a5 = RHM",
# "a6 = ALL", "a7 = HZM", "a8 = ZM","a9 = R","a10 = RM","a11 = RZM","a12 = RHZ",
# "a13 = HZ", "a14 = Z", "a15 = RZ"

## VennDiagram normal vector ##
Normal_venn_vector = c(Orthology_data$mean[13],
                       Orthology_data$mean[10],
                       Orthology_data$mean[15],
                       Orthology_data$mean[6],
                       Orthology_data$mean[4],
                       Orthology_data$mean[1],
                       Orthology_data$mean[5],
                       Orthology_data$mean[11],
                       Orthology_data$mean[12],
                       Orthology_data$mean[8],
                       Orthology_data$mean[3],
                       Orthology_data$mean[2],
                       Orthology_data$mean[9],
                       Orthology_data$mean[14],
                       Orthology_data$mean[7])

### VennDiagram size adjusted vectors ###

## The vector for size adjusted venn is sSizes = c(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15,v16)
# and the individual numbers are v1 = size of absent value (adjust the circle enclosures),
#"v2 = Z","v3 = M","v4 = ZM", "v5 = H","v6 = HZ","v7 = HM","v8 = HZM",
# "v9 = R", "v10 = RZ","v11 = RM", "v12 = RZM", "v13 = RH","v14 = RHZ",
#"v15 = RHM,"v16 = ALL"

## VennDiagram size adjusted vector - rank 100 ##

size_adjusted_venn_vector = c(0,
                                       Orthology_data$mean[14],
                                       Orthology_data$mean[15],
                                       Orthology_data$mean[11],
                                       Orthology_data$mean[13],
                                       Orthology_data$mean[9],
                                       Orthology_data$mean[10],
                                       Orthology_data$mean[5],
                                       Orthology_data$mean[12],
                                       Orthology_data$mean[7],
                                       Orthology_data$mean[8],
                                       Orthology_data$mean[3],
                                       Orthology_data$mean[6],
                                       Orthology_data$mean[2],
                                       Orthology_data$mean[4],
                                       Orthology_data$mean[1])
# Names for the legends #
rat_name = paste("Rat")
human_name = paste("Human")
zfish_name = paste("Zebrafish")
mouse_name = paste("Mouse")

# create Venn diagram with four sets
grid.newpage()
venn_normal <- draw.quad.venn(area.vector = Normal_venn_vector,
                              direct.area = T,
                              euler.d = T,
                              scaled = T,
                              category=c(rat_name,zfish_name,human_name,mouse_name),
                              col="Black",
                              fill=c("lightgreen", "skyblue", "#C33EDB", "darkgrey"),
                              lty="solid")
# save venn top 100
png(filename = file.path(Folder_out,File_out1),
    width = 8, height = 8, units = "in",
    bg = "transparent",res=600)
grid.draw(venn_normal)
dev.off()
dev.off()

## Plot and save size adjusted venn diagrams 
# Create venn object for plotting the size adjusted venn diagram #
SAvenn_obj_adjusted <-createVennObj(nSets = 4, sNames = c(rat_name,human_name,mouse_name,zfish_name), sSizes = size_adjusted_venn_vector)


## Print and save size adjusted venn diagrams
# size adjusted venn diagram top 100
png(filename = file.path(Folder_out,File_out2),
    width = 8, height = 8, units = "in",
    bg = "transparent",res=600)
    SAvenn_obj_plot <- plotVenn(nVennObj = SAvenn_obj_adjusted,nCycles=7000,setColors=c("lightgreen","#C33EDB", "darkgrey","skyblue"),opacity = 0.3, borderWidth = 3, labelRegions = F,fontScale = 1)
dev.off()

png(filename = file.path(Folder_out,File_out3),
    width = 8, height = 8, units = "in",
    bg = "transparent",res=600)
    SAvenn_obj_plot <- plotVenn(nVennObj = SAvenn_obj_adjusted,nCycles=7000,setColors=c("lightgreen","#C33EDB", "darkgrey","skyblue"),opacity = 0.3, borderWidth = 3,showNumbers=F, labelRegions = F,fontScale = 1)
dev.off()
