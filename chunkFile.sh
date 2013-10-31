#!/bin/bash
# Author: Christopher Ray
#
# This script splits the files into equal chunks equal to the number of lines desired by the second command argument
# and puts the file pieces into a folder titled "splitFiles"+number Of Lines as a 6 digit number (leading zeros). Each
# piece is then named (inputFileName).part_(6 digit number)
# for example, if chunkFile.sh was ran on test1_density_grid.txt,
# with 100000 lines per file ( "sh chunkFile.sh test1_density_grid.txt 100000" ),
# then the folderName would be "splitFiles100000",
# and the file pieces would be test1_density_grid.txt.part_000001, test1_density_grid.txt.part_000002,
# test1_density_grid.txt.part_000003 and so forth up to test1_density_grid.txt.part_000542)
#
# Run this shell script by typing the following into bash: sh chunkFile.sh filename numberOfLines
#
#
#command line arguments:  $1 is the first argument in the command line to chunkFile.sh, and $2 is the second argument in the command
# line to chunkFile.sh. For example, if chunkFile.sh was ran on test1_density_grid.txt,
# with 100000 lines per file ( "sh chunkFile.sh test1_density_grid.txt 100000" ),
# then $1 is equivalent to the string "test1_density_grid.txt" and $2 is equivalent to the integer 100000
#
#if the directory "splitFiles" does not exist
#make the directory "splitFiles"
#echo "chunkFile.sh:     Making splitFiles$2 directory with 777 permissions if it doesn't exist"
#mkdir -v -p -m 777 splitFiles$2
#
# split the file into parts and put in directory splitFiles.
#  note, limited to 999,999 files. To changes this limit edit the number following the -a
echo "chunkFile.sh:     Splitting $1 into $2 line chunks"
split --verbose -a 6 -d -l $2 $1 $1.part_
echo "chunkFile.sh:     Done"