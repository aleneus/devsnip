#!/bin/bash

PACKAGE_FOLDER=$1
LANG_FOLDER=$2


for f in $PACKAGE_FOLDER/*.py
do
    s=${f#*/}
    fo=$LANG_FOLDER/${s%.*}.po

    if [ -f $fo ]
    then
        xgettext $f -j --no-location -o $fo
    else
        xgettext $f --no-location -o $fo
    fi

    if [ -f $fo ] ; then
        msginit --no-translator --input=$fo --locale=ru_RU.UTF-8 -o $fo
    fi

done
