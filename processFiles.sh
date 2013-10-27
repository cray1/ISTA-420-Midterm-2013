#!/bin/bash

# Author: Christopher Ray

# This processes all the split files through grav.py and produces one output file for every file in the folder given. 

# Run this shell script by typing the following into bash: sh processFiles.sh folderName
# folderName is the name of the folder that contains the split up files. For example, if chunkFile.sh was ran on test1_density_grid.txt,
# with 100000 lines per file ( "sh chunkFile.sh test1_density_grid.txt 100000" ), then the folderName would be "splitFiles100000".
find $1 -name "*.txt.*" -exec python grav.py {} grav_pos.txt \;