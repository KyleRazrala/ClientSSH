#!/usr/bin/env python

import os
import sys
import time
import subprocess

os.system('clear')

print('Installing Needed Files... Please Wait A Several Minutes While Installing Files! Dont Exit or Abort The Program, It Will Damage The Script\n')

subprocess.call('pkg install python-pip -y >/dev/null 2>&1 && pip install halo >/dev/null 2>&1', shell=True)

from halo import Halo

with Halo(text='\033[1m\033[33mInstalling Required Files!\033[0m', spinner='dots'):
    subprocess.call('pkg install tur-repo -y >/dev/null 2>&1 && pkg install x11-repo -y >/dev/null 2>&1 && pkg install root-repo -y >/dev/null 2>&1 && pkg install python -y >/dev/null 2>&1 && pip install Cython pip >/dev/null 2>&1 && pkg install termux-api -y >/dev/null 2>&1 && pip install tqdm >/dev/null 2>&1 && pip install termux-api >/dev/null 2>&1 && pkg install openssh -y >/dev/null 2>&1 && pkg install figlet >/dev/null 2>&1 && pkg install toilet -y >/dev/null 2>&1 && pkg install grep -y >/dev/null 2>&1 && pkg install termux-am -y >/dev/null 2>&1 && pkg install termux-tools -y >/dev/null 2>&1 && pkg install wireless-tools -y >/dev/null 2>&1 && pkg install unzip -y >/dev/null 2>&1 && pkg install python3 -y >dev/null 2>&1 && pip install netifaces >dev/null 2>&1', shell=True)

print('Packages Successfully Installed!\n')

time.sleep(1)

spinner = Halo(text='\033[1m\033[33mUnpacking Server SSH!\033[0m', spinner='dots')
spinner.start()
time.sleep(5)
spinner.stop()

print('Successfully Unpacked!\n')

alias_name = 'client'
command = 'python /data/data/com.termux/files/usr/Client/ClientSSH'

with Halo(text='\033[1m\033[33mInstalling Client SSH!\033[0m', spinner='dots'):
    subprocess.call('unzip Client.zip >/dev/null 2>&1', shell=True)
    os.system('cd Client && chmod +x ClientSSH && chmod +x install')
    with open(os.path.expanduser("~/.bashrc"), "a") as bashrc:
        bashrc.write(f"\nalias {alias_name}='{command}'\n")
    os.system('cd $Home && ssh-keygen -A')
    os.system('cd $Home && cd ClientSSH && mv Client /data/data/com.termux/files/usr && cd $Home && rm -rf ClientSSH')

print('Client SSH Installation Successfully!\n')

spinner = Halo(text='\033[1m\033[33mRunning Setup!\033[0m', spinner='dots')
spinner.start()
time.sleep(5)
spinner.stop()

print('Setup Finish!\n')

time.sleep(1)

print('Close or Exit the Termux App by running command "exit" to be applied successfully and Open or Launch again the Termux App and Execute the Client SSH Script by running the command "client"\n')

print("Enjoy The Script Created By Tech'Yle")

os.system('source ~/.bashrc')
