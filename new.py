import os
import pymongo
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MONGODB_URL_KEY
mongo_db_url = os.getenv(MONGODB_URL_KEY)
print(mongo_db_url)
#print (os.environ)