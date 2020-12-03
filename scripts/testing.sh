#! /bin/bash
sudo apt update
yes | sudo apt install python3 python3-pip python3-venv
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
cd app1
python3 -m pytest --cov ./application
cd ..

cd app2
python3 -m pytest --cov ./application
cd ..

cd app3
python3 -m pytest --cov ./application
cd ..

cd app4
python3 -m pytest --cov ./application
cd ..