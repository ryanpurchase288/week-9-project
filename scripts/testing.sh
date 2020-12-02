#!/bin/bash
sudo apt-get update
sudo apt update && sudo apt install -y python3 python3-pip python3-venv
pip3 install -r service1/requirements.txt



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