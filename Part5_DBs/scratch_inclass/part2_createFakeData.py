#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbm
import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


load_dotenv()

AZURE_MYSQL_HOSTNAME = os.getenv("AZURE_MYSQL_HOSTNAME")
AZURE_MYSQL_USER = os.getenv("AZURE_MYSQL_USERNAME")
AZURE_MYSQL_PASSWORD = os.getenv("AZURE_MYSQL_PASSWORD")
AZURE_MYSQL_DATABASE = os.getenv("AZURE_MYSQL_DATABASE")


########

connection_string = f'mysql+pymysql://{AZURE_MYSQL_USER}:{AZURE_MYSQL_PASSWORD}@{AZURE_MYSQL_HOSTNAME}:3306/{AZURE_MYSQL_DATABASE}'
db = create_engine(connection_string)


#### note to self, need to ensure server_paremters => require_secure_transport is OFF in Azure 

### show databases
print(db.table_names())


###### create fake data for patients_details table 

#     id int,
#     mrn varchar(255),
#     first_name varchar(255),
#     last_name varchar(255),
#     zip_code varchar(255),
#     dob varchar(255),
#     gender varchar(255),
#     contact_mobile varchar(255),
#     contact_home varchar(255),
#     PRIMARY KEY (id) 


fakeDataCommand = """
insert into patients_details (id, mrn, first_name, last_name, zip_code, dob, gender, contact_mobile,  contact_home) values (1, '0001', 'john', 'smith', '10012', '01/01/1990', 'male', '621-555-5555', '212-555-5555');
"""

fakeDataCommand2 = """
insert into patients_details values (2222, '0001', 'john', 'smith', '10012', '01/01/1990', 'male', '621-555-5555', '212-555-5555');
"""

fakeDataCommand3 = """
insert into patients_details values 
(3, '0001', 'john', 'smith', '10012', '01/01/1990', 'male', '621-555-5555', '212-555-5555'), 
(4, '0001', 'john', 'smith', '10012', '01/01/1990', 'male', '621-555-5555', '212-555-5555'), 
(5, '0001', 'john', 'smith', '10012', '01/01/1990', 'male', '621-555-5555', '212-555-5555')
;
"""

testSql = """
insert into patients_details_2 (last_name, first_name) values 
('trump', 'donald')
;
"""
db.execute(testSql)

db.execute(fakeDataCommand)
db.execute(fakeDataCommand2)
db.execute(fakeDataCommand3)