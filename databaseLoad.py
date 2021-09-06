

#````````ADDING DATA TO SERVER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import psycopg2
from ACS_data import data



#changing the variable types from object to string
new_data = [list(map(str, lst)) for lst in data]

#change first 7 variables to intergers
for ls in new_data:
    for k in range(0,8):
        ls[k] = int(ls[k] )
      
    
    
#connect to the db
connection = psycopg2.connect(
    host = "acs-db.mlpolicylab.dssg.io",
    port = "5432",
    database = "acs_data_loading",
    user = "mlpp_student",
    password = "CARE-horse-most" )


#cursor
cursor = connection.cursor()

#create table 
table="""CREATE TABLE IF NOT EXISTS mortizza_acs_data (
totalpop               int,
whitepop               int,
income12months         int,
transport3544          int,
transport4559          int,
transport60more        int,
transpmode             int,
medianincome           int,
state                  varchar(2) NOT NULL,
county                 varchar(3) NOT NULL,
tract                  varchar(6) NOT NULL,
blockgroup             varchar(1) NOT NULL,
key                    varchar(10) PRIMARY KEY);"""
    
    
cursor.execute(table)


#add data into table
query = 'INSERT INTO mortizza_acs_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
cursor.executemany(query, new_data)


connection.commit( )
connection.close()
