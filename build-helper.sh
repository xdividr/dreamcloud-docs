#!/bin/bash

toxinidir="$1"

if [ -z "$toxinidir" ] ; then
    echo "Run tox instead of running this script directly"
    exit 1
fi

raw_keywords="$(grep -R '.. only::' ${toxinidir}/source/dream* | sed 's/\.\. only::/ /g' | awk '{print $2}' | sort -u)"

for i in $raw_keywords ; do
    files="$(grep -R ".. only:: ${i}" ${toxinidir}/source/dream* | sed 's/:\.\. only::/ /g' | awk '{print $1}' | sort -u | xargs)"
    echo "$files"
    sphinx-build -E -b html -t "$i" -d "${toxinidir}/build-${i}/doctrees" "${toxinidir}/source" "${toxinidir}/build-${i}/html" "$files"
    status=$?
    if [ $status -ne 0 ] ; then
        exit $status
    fi
done

sphinx-build -W -E -b html -d ${toxinidir}/build/doctrees ${toxinidir}/source ${toxinidir}/build/html
status=$?
if [ $status -ne 0 ] ; then
    exit $status
fi
