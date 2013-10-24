#!/bin/bash
# Run this shell script by typing the following into bash: sh chunkFile.sh filename numberOfLines

#if the directory "splitFiles" does not exist
if [ ! -d "splitFiles$2" ]; then
  #make the directory "splitFiles"
  mkdir splitFiles$2
fi #end if

#split the file into parts and put in directory splitFiles.
split -a 6 -d -l $2 $1 splitFiles$2/$1.part_  #note, limited to 999,999 files. To changes this limit edit the number following the -a