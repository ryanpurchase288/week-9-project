#! /bin/bash
mkdir -p ~/.local/bin
echo 'PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
sudo pip3 install --user ansible
sudo ansible-playbook -i inventory playbook.yaml
