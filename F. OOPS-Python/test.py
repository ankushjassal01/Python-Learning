import pymysql
import encodings



endpoint  = "mysql-learningdb.csxdcbioem3r.ap-south-1.rds.amazonaws.com"
username = "admin"
passwrd = "Masterdb1234" # RDS Mysql password
database_name = "banks" # RDS MySQL DB name

connection = pymysql.connect(host=endpoint, user=username, port=3306, password=passwrd, database=database_name )


def lambda_handler():
    cursor = connection.cursor()
    cursor.execute('Select * from accounts')


    rows = cursor.fetchall()

    for row in rows:
        print('{0} | {1} | {2} | {3} | {4}'.format(row[0],row[1],row[2],row[3],row[4]))


lambda_handler()
