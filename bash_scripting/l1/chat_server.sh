#!/bin/bash

chatlog='chat.log'

while [[ true ]]
do
	nc -l 4444 >> $chatlog
	tail -n 1 $chatlog
done
