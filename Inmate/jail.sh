#!/bin/bash
function filter {
	if [[ $1 =~ [a-zA-Z0-9] ]];then
    	return 0
    fi
		return 1
}

while :
do
	echo -n "$ "
    read input
    if filter "$input";then
    	echo -e "\033[0;31m$input: Illegal character\033[0m"
    else
    	bash -c "$input"
    fi
done
