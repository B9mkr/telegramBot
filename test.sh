#! /bin/bash

green="\e[1;32m"
end="\e[0m"
file="testBackupDate"
currentDate=`date`
echo "\"$currentDate\"" >> $file
# sed -i '/^$/d' $file
# xclip -selection clipboard $file
echo -e "Current date \"$currentDate\" ${green} Copied ${end}"
