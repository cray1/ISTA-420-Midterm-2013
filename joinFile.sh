#!/bin/bash
# Run this shell script by typing the following into bash: sh joinFile.sh folderName fileName

cd $1

#if the directory "outputFiles" does not exist
if [ ! -d "outputFiles" ]; then 
  #make the directory "outputFiles"
  mkdir outputFiles
fi #end if


find . -name "*.out" -exec mv {} outputFiles \;

cd outputFiles

cat `ls` > $2

mv $2 ../../
