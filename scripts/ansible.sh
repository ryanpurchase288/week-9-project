#!/bin/bash
mkdir -p ~/.local/bin
echo 'PATH=$PATH:home/jenkins/.local/bin' >> ~/.bashrc
source ~/.bashrc
pip3 install --user ansible
ansible-playbook -i inventory playbook.yaml
