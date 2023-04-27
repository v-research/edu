#!/bin/bash

clear
echo "WELCOME TO THE ITS LAST CHAT!"

chatlog='chat.log'

while [[ true ]]
do
	nc -l 4444 | tee -a $chatlog
	#equivalent to:
	# nc -l 4444 >> $chatlog

	tail -n 1 $chatlog | grep -e "-help" &>/dev/null
	if [[ $? -eq 0 ]]
	then
		echo -e "\nCOMMANDS\n\tusername: change username\n\tsend: send message\n\texit: quit chat\n"
	fi

	# tail -n 1 $chatlog
done
