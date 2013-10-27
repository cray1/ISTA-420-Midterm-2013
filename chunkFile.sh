#!/bin/bash
# Author: Christopher Ray

# This script splits the files into equal chunks equal to the number of lines desired by the second command argument
# and puts the file pieces into a folder titled "splitFiles"+number Of Lines as a 6 digit number (leading zeros). Each
# piece is then named (inputFileName).part_(6 digit number) 
# for example, if chunkFile.sh was ran on test1_density_grid.txt,
# with 100000 lines per file ( "sh chunkFile.sh test1_density_grid.txt 100000" ), 
# then the folderName would be "splitFiles100000",
# and the file pieces would be test1_density_grid.txt.part_000001, test1_density_grid.txt.part_000002,
# test1_density_grid.txt.part_000003 and so forth up to test1_density_grid.txt.part_000542)

# Run this shell script by typing the following into bash: sh chunkFile.sh filename numberOfLines

#if the directory "splitFiles" does not exist
if [ ! -d "splitFiles$2" ]; then
  #make the directory "splitFiles"
  mkdir splitFiles$2
fi #end if

#split the file into parts and put in directory splitFiles.
split -a 6 -d -l $2 $1 splitFiles$2/$1.part_  #note, limited to 999,999 files. To changes this limit edit the number following the -a

#command line arguments:  $1 is the first argument in the command line to chunkFile.sh, and $2 is the second argument in the command
# line to chunkFile.sh. For example, if chunkFile.sh was ran on test1_density_grid.txt,
# with 100000 lines per file ( "sh chunkFile.sh test1_density_grid.txt 100000" ),
# then $1 is equivalent to the string "test1_density_grid.txt" and $2 is equivalent to the integer 100000