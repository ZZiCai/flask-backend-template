####################
# database config
HOST = '127.0.0.1 or other ip' # TODO: change to your host
PORT = '3306' # TODO: change to your port, default is 3306
DATABASE = 'your_db'   # TODO: change to your db name
USERNAME = 'root or your_username' # TODO: change to your username    
PASSWORD = 'your_password' # TODO: change to your password
####################

# DB_URL: mysql
DB_URL = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True  # print sql, debug mode