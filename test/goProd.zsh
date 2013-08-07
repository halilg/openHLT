#!/usr/bin/env zsh
SOURCE=""
DSET=`basename $PWD`
echo $HOST
echo Dataset is $DSET
OUTPUT=Products.${DSET}.root.txt
for q in `cat root_files_${DSET}.txt`;do SOURCE="$q"; done #!! only the last file
rm -f $OUTPUT
echo $HOST > $OUTPUT
CMD="./openHLT.py -p -v -t hlt_${DSET}.py -i $SOURCE -o /tmp/halil/Products.${DSET}.root --go 2>&1 | tee $OUTPUT"
echo $CMD
eval ${CMD}
