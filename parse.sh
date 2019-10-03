# !/usr/bin/env bash

runPythonScript() {
	python3 parseCoordinates.py $1
}

counter=1
for file in ./geocoding/*; do
	echo "${counter} ${file}";
	let "counter++"
	runPythonScript ${file}
done 
