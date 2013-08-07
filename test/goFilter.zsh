#!/usr/bin/env zsh
DSET=`basename $PWD`
SOURCE="/tmp/halil/Products.${DSET}.root"
echo $HOST
echo Dataset is $DSET
OUTPUT=stdouterr.${DSET}.txt
rm -f $OUTPUT
echo $HOST > $OUTPUT
CMD="./openHLT.py -v -t hlt_${DSET}.py -i $SOURCE -o /tmp/halil/Filters.${DSET}.root --go 2>&1 | tee $OUTPUT"
echo $CMD
eval ${CMD}
