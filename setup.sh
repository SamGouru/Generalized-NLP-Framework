#!/bin/bash

# get root permission
#if [ $EUID != 0 ]; then
#    sudo "$0" "$@"
#    exit $?
#fi

f_install_server() {
    echo "Installing webserver and other binaries"
    sudo apt update -qq
    sudo apt install -y git htop nginx ufw
    
    # install php7.1
    sudo apt-get install software-properties-common
    sudo add-apt-repository -y ppa:ondrej/php
    sudo apt-get update -qq
    sudo apt install -y php7.1 php7.1-fpm php7.1-mysql
    
    echo "Downloading adminer"
    wget "https://www.adminer.org/latest.php"
    mv -v latest.php adminer.php
    
    echo "Setting up firewall"
    ufw default deny incomming
    ufw default allow outgoing
    ufw allow ssh
    ufw allow http
    ufw allow https
    ufw allow mysql
    ufw enable
    ufw status
}


f_install_pythonApp() {
    echo "Installing python and dependancies"
    sudo apt update -qq
    sudo apt install -y python3 python3-pip python3-tk
    pip3 install --upgrade nltk numpy pymysql
    pip3 install git+https://github.com/emilmont/pyStatParser.git
    
    echo "Configuring python nltk"
    #python3 -m nltk.downloader all
    python -m nltk.downloader punkt
    python -m nltk.downloader averaged_perceptron_tagger
    python -m nltk.downloader treebank
}


echo "Choose setup option
1 - Run server setup
2 - Run python application setup
3 - Run both"

while true; do
  read -p "> " input
  case $input in
      [1]* ) 
        f_install_server
        break;;
      [2]* ) 
        f_install_pythonApp
        break;;
      [3]* ) 
        f_install_server
        f_install_pythonApp
        break;;
      * ) echo "Please chose 1, 2 or 3.";;
  esac
done
