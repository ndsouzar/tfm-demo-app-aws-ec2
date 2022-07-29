#!/bin/bash
sudo apt update
sudo apt install python3-pip -y
sudo apt install wget
sudo apt install apache2 -y

git clone https://github.com/amansin0504/csw-vm-demo.git
cd csw-vm-demo/source/
sudo cp templates/index.html /var/www/html/
sudo systemctl restart apache2
