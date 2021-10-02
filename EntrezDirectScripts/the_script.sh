


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

split -l 500 $1 input.



for f in input.*

do

ids=$(cat $f | tr "\n" ",")

epost -db protein -id $ids | efetch -format docsum|xtract -pattern DocumentSummary -element Caption Title Extra  > $f.output

paste $f.output > $f.result

rm $f.output

sleep 1
done



cat *.result > $1.output

rm *.result

rm input.*

else

echo "Usage: bash the_script.sh <$1 input, the file containing a column of prot ids>"

fi

