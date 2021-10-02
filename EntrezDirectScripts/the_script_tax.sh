


#!/bin/bash
#$ -cwd
#$ -V
#$ -l h_rt=48:00:00
#$ -l h_vmem=60G

econtact -email n.t.do@leeds.ac.uk -tool the_script.sh


exist=$(which epost)

if [ $(echo $? != 0) ]

then

echo "Entrez Direct not in \$PATH"

exit

fi




if [ -n "$1" ]

then

split -l 50 $1 input.



for f in input.*

do

ids=$(cat $f | tr "\n" ",")

epost -db protein -id $ids | efetch -format gpc|xtract -pattern INSDSeq -element INSDSeq_accession-version INSDSeq_definition INSDSeq_taxonomy INSDSeqid > $f.output
sleep 3
paste $f.output > $f.result
sleep 3
rm $f.output

sleep 3
done

sleep 1

cat *.result > $1.output

rm *.result

rm input.*

else

echo "Usage: bash the_script.sh <$1 input, the file containing a column of prot ids>"

fi

