#!/bin/bash
# Run this shell script by typing the following into bash: sh joinFile.sh folderName fileName
cd $1
cat `ls` > $2