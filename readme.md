# Database Project

## Instructions (How to run):
* Download MySQL and create a database with name "50043_DB"
* Create a new user and give it admin permission
* Run `export MYSQL_USER=<USER>` to set environment variables
* Run `export MYSQL_PASSWORD=<PASSWORD>` to set environment variables
* Run `export FLASK_APP=manage.py` to point the entry of "flask run" to manage.py (factory init method)
* Run `flask db init` and then `flask db migrate`. **Important:** if you have issues running these commands, check the following subpoints 
    * make sure to run `pip install -r requirements.txt` to get the `flask-migrate` library which enables the flask db commands.
    * Make sure a database named 50043_DB exists in your local mysql environment, and users defined in the environment variables have full permissions to a database named `50043_DB`.
* Verify the new .py file in the migrations/versions and check if the upgrades are correct.
* Run `flask db upgrade` to apply the migration
* Run `flask run` and go to `127.0.0.1:5000/register`

## Background information
Update 9/10/2019: We have started using sqlalchemy to handle our mysql server. Also, we now use flask-migrate to handle the migration of our sqlalchemy database linked to our flask app.

## Automation scripts
Currently, the script assumes that your local machine **does not** have a database named `50043_DB` and a user named '50043_DB'@'localhost'. The script will generate the afore mentioned database and user with full permissions.

## Quality of life improvements
* [SSH Keys and Github](https://dev.to/maedahbatool/generating-a-new-ssh-key-and-adding-it-to-github-137j)

## MongoDB
* default location to view log files from mongodb: `/var/log/mongodb/mongodb.log`
* start mongod as a background process (allows you to use mongodb command line interface): `sudo service mongodb start`

### Database commands
* create DB: `use <db_name>`
* show databases: `show databases` (database with no collections not shown)

### Collections commands
* show collections for current db: `show collections`
* create collection: 
    * `db.createCollection('<collection_name>')`
    * `db.<collection_name>.insert({<json_object>})`
* list objects in a collection: `db.<collection_name>.find()`

### PyMongo material
* [Introduction to mongodb and python](https://realpython.com/introduction-to-mongodb-and-python/)

### Data analytics with Pandas and Apache Spark
* Amazon Kindle Reviews Dataset
    * Pandas + Scikit-Learn
        * Pearson correlation: price vs review length
        * TF-IDF 
            * Review sentiment analysis
            * Find similar reviews
            * Extract review keywords
    * Apache Spark
        * Install and setup
        * Raw csv/json -> Spark DataFrames
        * Run SQL queries from python
        
* [Colab Notebook](https://colab.research.google.com/drive/1j9WC5OVgnXZ1-h82Yk6B4BRYtKCJxYTp)
