#!/bin/bash

echo "Filters stuff running"

#remove already existent direcotry because I do not want to create two thousand directories in testing the script
if test -d bandpass_excercise/; then
	echo "removing already existing bandpass_excercise directory"
	rm -r bandpass_excercise/
fi

#create a new directory and move all bandpass_original files to it, moving to the directory
cp -r bandpasses_original/ bandpass_excercise/
cd bandpass_excercise/
current_dir=$(pwd)
echo $current_dir

#printing the occurency of the .somestuff files
echo -n ".dat "   && ls | cat | grep -c ".dat"
echo -n ".asc "   && ls | cat | grep -c ".asc"
echo -n ".ASCII " && ls | cat | grep -c ".ASCII"
echo -n "total "  && ls | cat | grep -c "." 

#checking for the presence of "photons" or "energy" and rename the file as consequence
directory="bandpass_excercise"

#Loop through each file in the directory
#check if contains energy or photon in the first lines, the ones which contain the info about the bandpass
#
for file_name in "$current_dir"/*; do
	if [ $(head -10 $file_name | grep -c "photon") != 0 ]; then
		mv $file_name ${file_name%.*}.photons.filt
	elif [ $(head -10 $file_name | grep -c "energy") != 0 ]; then
		mv $file_name ${file_name%.*}.energy.filt
	else
		mv $file_name ${file_name%.*}.none.filt
	fi
done
