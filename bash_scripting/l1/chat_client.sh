#!/bin/bash

cdef='\e[0m' #color default
cred='\e[0;31m' #color green
cgreen='\e[0;32m' #color green
usr=$(whoami)

while [[ true ]]
do
	echo -n "> "
	read i

	if [[ $i == "?" || $i == "help" ]]
	then
		echo -e "\nCOMMANDS\n\tusername: change username\n\tsend: send message\n\texit: quit chat\n"
	fi

	if [[ $i == "username" ]]
	then
		echo -ne "${cred}new username: $cdef"
		read usr
	fi

	if [[ $i == "send" ]]
	then
		echo -ne "${cgreen}message: $cdef"
		read mex
		echo "[$(date +%r)] $usr: $mex" | nc -N 127.0.0.1 4444
	fi

	if [[ $i == "exit" ]]
	then
		exit
	fi
done
