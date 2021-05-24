#!/bin/bash
LANG_FOLDER=$1

for f in $LANG_FOLDER/*.po
do
    msgfmt "$f" -o "${f%.*}.mo"
done
