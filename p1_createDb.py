import  sqlite3
connect = sqlite3.connect('patients.db')
db = connect.cursor()
db.execute("DROP TABLE IF EXISTS patient_table")
connect.commit()

table = """ CREATE TABLE patient_table(
    mrn VARCHAR(255) NOT NULL, 
    firstname CHAR(25) NOT NULL
    lastname CHAR(25) NOT NULL
    dob CHAR(25) NOT NULL );"""
