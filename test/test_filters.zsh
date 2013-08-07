#!/usr/bin/env zsh
tdir=/tmp/$USER #where the temporary files (the producer root file and the hlt dump file) wil be located
webroot=http://foton.fizik.anadolu.edu.tr/halil/openHLT #where the above mentioned files will be downloaded
cdir=$PWD

testdst() {
    dst=$1
    rfname=Products.$1.root
    hltfname=hlt_$1.py
    echo testing $1
    if [ ! -f $tdir/$rfname ]; then
        echo retrieving $rfname
        cd $tdir
        wget -c -N $webroot/$rfname || exit
        cd -
    fi
    if [ ! -f $hltfname ]; then
        wget -c -N $webroot/$hltfname || exit
    fi
    cmd="$cdir/openHLT.py -t $hltfname -i $tdir/$rfname -o $tdir/output.temp.root --go >&! $2"
    echo $cmd
    eval ${cmd} || exit
}

eval `scramv1 runtime -sh` || exit
for dst in `cat datasets.txt`; do
    testdst $dst openhlt.${dst}.txt
    if [ -f openhlt.${dst}_ref_notimereport.txt ]; then # reference file exists        
        echo vvvvv diff report vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        cat openhlt.${dst}.txt | grep -v TimeReport | diff openhlt.${dst}_ref_notimereport.txt -
    else
        mv openhlt.${dst}.txt openhlt.${dst}_ref.txt
        cat openhlt.${dst}_ref.txt | grep -v TimeReport > openhlt.${dst}_ref_notimereport.txt
        echo created reference files openhlt.${dst}_ref.txt and openhlt.${dst}_ref_notimereport.txt. Later runs will include a diff report.
    fi
done