#! /bin/bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 -m venv venv
. venv/bin/activate

cd app1
pytest --cov ./application
cd ..

cd app2
pytest --cov ./application
cd ..

cd app3
pytest --cov ./application 
cd ..

cd app4
pytest --cov ./application
cd ..