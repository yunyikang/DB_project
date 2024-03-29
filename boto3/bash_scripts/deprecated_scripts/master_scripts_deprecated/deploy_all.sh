#!/bin/bash

if [ "$EUID" -eq 0 ] # Root has $EUID = 0
  then echo "Please run this script as non-root (no sudo)."
  exit
fi

# sequential deployment of servers on EC2. (Next step: aim to parallelize)
if [ $# -eq 0 ]
    then
    echo "No url specified. Using default dropbox url"
    dropbox_url=https://www.dropbox.com/s/6g4zfii8f0d7yny/bookreviews.zip?dl=0
else
    dropbox_url=$1
fi

# deployment of MongoDB server
echo "************ Deploying MongoDB server **************"
# ./../mongodb/ec2_setup_mongodb.sh ${dropbox_url}

# deployment of MySQL server
echo "************ Deploying MySQL server **************"
./../mysql/ec2_setup_mysql.sh ${dropbox_url}

# deployment of Flask server
# echo "************ Deploying Flask server **************"
# ./../flask/ec2_setup_flask.sh ${dropbox_url}
wait
echo "deployment of Servers completed"