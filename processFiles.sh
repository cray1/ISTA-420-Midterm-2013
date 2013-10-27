#!/bin/bash
# This processes all the split files through grav.py
# Run this shell script by typing the following into bash: sh processFiles.sh folderName
find .$1 -name "*.txt" -exec python grav.py {} grav_pos.txt \;