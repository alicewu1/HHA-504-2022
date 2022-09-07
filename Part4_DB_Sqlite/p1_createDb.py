import sqlite3 # note, sqlite3 comes with python3


##### Note, this is just an example script, to create a database, you need to do this manually.
## otherwise you just need to run this once and then you can use the database in your flask app

# Connecting to sqlite
# connection object
connect = sqlite3.connect('./Part4_DB_Sqlite/patients.db')
 
# db object
db = connect.cursor()

# delete table patient_table if it exists
db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit()


# Creating table, 
table = """ CREATE TABLE patient_table (
            mrn VARCHAR(255) NOT NULL,
            firstname CHAR(25) NOT NULL,
            lastname CHAR(25) NOT NULL,
            dob CHAR(25) NOT NULL
        ); """

db.execute(table)
connect.commit() # commit the changes, this is annoying but necessary


## note, you may see a .db-journal file, that is a temporary file that is created when you create a database.
## insert data into the table
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob) values('12345', 'John', 'Smith', '01/01/2000')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob) values('23456', 'Jane', 'Doe', '02/02/2001')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob) values('34567', 'Mary', 'Smith', '03/03/2002')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob) values('45678', 'Bob', 'Smith', '04/04/2003')")
db.execute("INSERT INTO patient_table(mrn, firstname, lastname, dob) values('56789', 'Jane', 'Doe', '05/05/2004')")
connect.commit()


# close the connection
connect.close()