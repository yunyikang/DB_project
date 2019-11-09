#!/bin/bash

server_ip="3.17.13.75"
public_key="experimental_instance.pem"
username="ubuntu"

# add ip address of server to list of known hosts. should remove the need to manually add to trusted hosts
ssh-keygen -R $server_ip # remove host from host file if it exists
# ssh-keyscan -t ecdsa $server_ip >> /root/.ssh/known_hosts # add ecdsa encrypted fingerprint of server into known hosts
ssh-keyscan -H $server_ip >> /root/.ssh/known_hosts # add ecdsa encrypted fingerprint of server into known hosts

if [ $# -eq 0 ]
    then
    echo "No url specified. Using default dropbox url"
    dropbox_url=https://www.dropbox.com/s/6g4zfii8f0d7yny/bookreviews.zip?dl=0
else
    dropbox_url=$1
fi


# scp datasets to folder in ec2 instance
scp -i ~/.ssh/$public_key ../../get_data.sh $username@$server_ip:/home/$username
ssh -i ~/.ssh/$public_key $username@$server_ip 'sudo apt-get -y install unzip'
ssh -i ~/.ssh/$public_key $username@$server_ip './get_data.sh'

# scp scripts to folder in ec2 instance
scp -i ~/.ssh/$public_key ../mongodb/mongodb_setup.sh $username@$server_ip:/home/$username
ssh -i ~/.ssh/$public_key $username@$server_ip "./mongodb_setup.sh ${dropbox_url}"
