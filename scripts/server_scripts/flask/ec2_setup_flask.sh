#!/bin/bash

source ../config/config_flask.sh

if [ $# -eq 0 ]
    then
    echo "No url specified. Using default dropbox url"
    dropbox_url=https://www.dropbox.com/s/6g4zfii8f0d7yny/bookreviews.zip?dl=0
else
    dropbox_url=$1
fi

echo "adding flask server ($server_ip) to known_hosts"
ssh-keygen -R $server_ip
ssh-keyscan -t ecdsa -H $server_ip >> ~/.ssh/known_hosts

scp -i ~/.ssh/$public_key ../flask/flask_setup.sh $username@$server_ip:/home/$username
scp -i ~/.ssh/$public_key ../flask/env_setup.sh $username@$server_ip:/home/$username
ssh -i ~/.ssh/$public_key $username@$server_ip "sudo ./flask_setup.sh ${dropbox_url}"

