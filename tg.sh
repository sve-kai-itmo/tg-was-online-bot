#!/bin/bash
name=$1 #Имя_Фамилия или @username
path_cli="/home/$USER/bin/telegram-cli"
path_key="/home/$USER/tg/tg-server.pub"
# LOGFILE="/home/$USER/Bot/tg.log"
# $path_cli $path_key -W -e "user_info $name" | grep -E "(^User ${name/_/ }|	phone|was online)" | sed "s,\x1B[[0-9;]*[a-zA-Z],,g" # find user by his name
$path_cli $path_key -W -e "user_info $name" | grep -E "(\(#[0-9]|	phone|line \(was online)" | sed "s,\x1B[[0-9;]*[a-zA-Z],,g" # find user by his id
# sed necessary to remove ANSI characters using Bash
exit 0