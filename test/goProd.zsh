#!/usr/bin/env zsh
SOURCE=""
if [[ $# -lt 1 ]]; then
	echo "usage: $0 <dataset>"
	exit
fi
DSET=$1 #`basename $PWD`
echo $HOST
echo Dataset is $DSET
OUTPUT=Products.${DSET}.root.txt
for q in `cat root_file_uris/root_files_${DSET}.txt`;do SOURCE="$q"; done #!! only the last file
rm -f $OUTPUT
echo $HOST > $OUTPUT
CMD="./openHLT.py -p -v -t hlt_${DSET}.py -i $SOURCE -o /tmp/halil/Products.${DSET}.root --go 2>&1 | tee $OUTPUT"
rm -f hlt_${DSET}.py
ln -s hlt_files/hlt_${DSET}.py
echo $CMD
eval ${CMD}
rm -f hlt_${DSET}.py
