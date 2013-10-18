#!/bin/bash
# sh scriptname filename
split -dl$((`wc -l $1|sed 's/ .*$//'` / 3 + 1)) $1 $1-chunk.