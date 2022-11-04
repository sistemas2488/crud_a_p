from dotenv import load_dotenv
import os

load_dotenv()
'''
user = os.environ["MYSQL_USER"]
password = os.environ["MYSQL_PASSWORD"]
host = os.environ["MYSQL_HOST"]
database = os.environ["MYSQL_DATABASE"]
'''
user = 'root'
password = ''
host = 'localhost'
database = 'contactsdb'


DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'
print(DATABASE_CONNECTION_URI)
