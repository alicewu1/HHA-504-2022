import sqlite3
import pandas as pd

def get_db_connection():
    conn = sqlite3.connect('Part4_DB_Sqlite/patients.db')
    conn.row_factory = sqlite3.Row
    return conn

conn = get_db_connection()
patientListSql = conn.execute('SELECT * FROM patient_table').fetchall()
patientListSql

# save the data to a dataframe
df = pd.DataFrame(patientListSql)

# rename the columns
df.columns = ['mrn', 'firstname', 'lastname', 'dob']
df