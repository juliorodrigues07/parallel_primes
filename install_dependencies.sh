#!/bin/bash

sudo apt install build-essential
cd /
cd tmp
wget https://download.open-mpi.org/release/open-mpi/v4.1/openmpi-4.1.5.tar.gz
tar -xf openmpi-4.1.5.tar.gz
cd openmpi-4.1.5
./configure --prefix /home/$(whoami)/openmpi
make
make install

# OPTIONAL - Only for instance and time graphics generation
sudo apt install python3 python3-pip build-essential python3-dev
pip install pycryptodomex
pip install matplotlib
pip install seaborn
