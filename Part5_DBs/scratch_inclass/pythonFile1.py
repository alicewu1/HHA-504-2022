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


### 
string_createPatientsTable = """
create table patients_details_test (
    id int,
    mrn varchar(255),
    first_name varchar(255),
    last_name varchar(255),
    zip_code varchar(255),
    dob varchar(255),
    gender varchar(255),
    contact_mobile varchar(255),
    contact_home varchar(255),
    PRIMARY KEY (id) 
); 
"""


drop_table = """
drop table patients_details_test;
"""

db.execute(drop_table)


db.execute(string_createPatientsTable)
