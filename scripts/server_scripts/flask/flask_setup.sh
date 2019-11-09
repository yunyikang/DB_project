#!/bin/bash

# dropbox url is the first command line argument
dropbox_url=$1

# install dependencies and updates
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y python3-pip
sudo apt-get install -y build-essential libssl-dev libffi-dev python-dev
sudo apt-get install -y python3-venv

# download the bookreviews repository
# wget -c https://www.dropbox.com/s/6g4zfii8f0d7yny/bookreviews.zip?dl=0 -O bookreviews.zip
wget -c $dropbox_url -O bookreviews.zip
sudo apt-get install -y unzip

# unzip the bookreviews repository
unzip bookreviews.zip -d "/home/ubuntu/bookreviews"
cd bookreviews

# create and update virtual environment requirements
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# launch flask server
source ../env_setup.sh
flask run

''' CAUTION: pressing Ctrl+C ends the local ssh connection, not the flask server
To end the flask server, ssh into the server and find its process id. by running ps -ef | grep flask, then run sudo kill -9 <process_id>
Instructions here https://superuser.com/questions/446808/how-to-manually-stop-a-python-script-that-runs-continuously-on-linux
'''
