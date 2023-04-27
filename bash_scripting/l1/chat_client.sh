#!/bin/bash

cdef='\e[0m' #color default
cred='\e[0;31m' #color green
cgreen='\e[0;32m' #color green
usr=$(whoami)
chatlog='chat.log'

#tail -f $chatlog &
#pidtail="$!"

while [[ true ]]
do
	echo -n "> "
	read i

	if [[ $i == "help" ]]
	then
		echo "[$(date +%r)] $usr: -help" | nc -N 127.0.0.1 4444
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
		#sudo kill -9 $pidtail
		exit
	fi
done
