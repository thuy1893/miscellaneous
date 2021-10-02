


#!/bin/bash
#$ -cwd
#$ -V
#$ -l h_rt=48:00:00
#$ -l h_vmem=60G

econtact -email n.t.do@leeds.ac.uk -tool the_script.sh


##check for the folder of files
echo "Folder of files:"
if [ -d "${folder}" ]; then
	echo "Good $folder is OK";
elif [ -f "${folder}" ]; then
	echo "Error ${folder} is a file"; 
	exit 1
else
	echo "Error ${folder} is not valid file or folder";
	exit 1
fi
echo List of files $folder/*

##get the file from the list
file=$(ls $folder/*|sed -n -e "$SGE_TASK_ID p")
	echo $file file



exist=$(which epost)

if [ $(echo $? != 0) ]

then

echo "Entrez Direct not in \$PATH"

exit

fi




if [ -n "$file" ]

then

split -l 30 $file input.



for f in input.*

do

ids=$(cat $f | tr "\n" ",")

epost -db protein -id $ids | efetch -format gpc|xtract -pattern INSDSeq -element INSDSeq_accession-version INSDSeq_definition INSDSeq_taxonomy INSDSeqid > $f.output

paste $f.output > $f.result

rm $f.output

sleep 1
done



cat *.result > ./annot_out/$file.output

rm *.result

rm input.*
sleep 10
else

echo "Usage: bash the_script.sh <$1 input, the file containing a column of prot ids>"

fi

