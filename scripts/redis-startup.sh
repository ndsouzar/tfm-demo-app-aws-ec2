#!/bin/bash
sudo apt update
sudo apt install python3-pip -y
sudo apt install wget
sudo pip install Flask

git clone https://github.com/amansin0504/csw-vm-demo.git
cd csw-vm-demo/source/
python3 redis.py &
