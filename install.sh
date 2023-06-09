#!/bin/bash

clear

echo 'Installing Needed Files... Please Wait A Several Minutes While Installing Files! Dont Exit or Abort The Program, It Will Damage The Script
'

pkg install python-pip -y >/dev/null 2>&1 && pip install halo >/dev/null 2>&1

echo -e '\033[1m\033[33mInstalling Required Files!\033[0m'
pkg install tur-repo -y >/dev/null 2>&1 && pkg install x11-repo -y >/dev/null 2>&1 && pkg install root-repo -y >/dev/null 2>&1 && pkg install python -y >/dev/null 2>&1 && pip install Cython pip >/dev/null 2>&1 && pkg install termux-api >/dev/null 2>&1 && pip install tqdm >/dev/null 2>&1 && pip install termux-api >/dev/null 2>&1 && pkg install openssh -y >/dev/null 2>&1 && pkg install figlet >/dev/null 2>&1 && pkg install toilet -y >/dev/null 2>&1 && pkg install grep -y >/dev/null 2>&1 && pkg install termux-am -y >/dev/null 2>&1 && pkg install termux-tools -y >/dev/null 2>&1 && pkg install wireless-tools -y >/dev/null 2>&1 && pkg install unzip -y >/dev/null 2>&1 && pkg install python3 -y >/dev/null 2>&1 && pip install netifaces >/dev/null 2>&1

echo 'Packages Successfully Installed!
'

sleep 1

echo -e '\033[1m\033[33mUnpacking Client SSH!\033[0m'
spinner='...'
printf ' '
sleep 5

echo 'Successfully Unpacked!
'

alias_name='client'
command='python /data/data/com.termux/files/usr/Client/ClientSSH'

echo -e '\033[1m\033[33mInstalling Client SSH!\033[0m'
unzip Client.zip >/dev/null 2>&1
cd Client && chmod +x ClientSSH && chmod +x install
echo -e "\nalias $alias_name='$command'\n" >> ~/.bashrc
cd $Home && ssh-keygen -A
cd $Home && cd ClientSSH && mv Client /data/data/com.termux/files/usr && cd $Home && rm -rf ClientSSH

echo 'Client SSH Installation Successfully!
'

echo -e '\033[1m\033[33mRunning Setup!\033[0m'
spinner='...'
printf ' '
sleep 5

echo 'Setup Finish!
'

sleep 1

echo 'Close or Exit the Termux App by running command "exit" to be applied successfully and Open or Launch again the Termux App and Execute the Client SSH Script by running the command "client"
'

echo "Enjoy The Script Created By Tech'Yle"

source ~/.bashrc
