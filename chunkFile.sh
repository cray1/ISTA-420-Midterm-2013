#!/bin/bash
# sh scriptname filename numberOfChunks(limit:99)
split -dl$((`wc -l $1|sed 's/ .*$//'` / $2 + 1)) $1 $1-chunk.