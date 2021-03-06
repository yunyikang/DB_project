import datetime
import os
from util.getIP import getIP

FLASK_APP = "manage.py"
FLASK_ENV = "development"

f = open("/home/ubuntu/config_mysql_ip.txt","r")
MYSQL_HOST = f.read()
# MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
DBNAME = "50043_DB"
SECRET_KEY = os.environ.get("SECRET_KEY", default="secret")
MYSQL_USERNAME = os.environ.get("MYSQL_USER", default="50043_DB")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", default="password")
MYSQL_URI = "mysql+pymysql://%s:%s@%s:3306/%s" % (DBNAME, MYSQL_PASSWORD, MYSQL_HOST, DBNAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = MYSQL_URI
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=30)