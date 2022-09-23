import mysql.connector
import json


with open('config.json') as f:
    params = json.load(f)['params']

db = mysql.connector.connect(
    host = params['host'], 
    user = params['user'], 
    passwd = params['passwd'], 
    database = params['database']
)

# my_cursor = db.cursor(dictionary=True)
my_cursor = db.cursor(buffered=True , dictionary=True)


def checking():
    my_cursor.execute('select * from places_and_location_info')
    result = my_cursor.fetchall()
    return result

# def checking():
#     my_cursor.execute('TRUNCATE TABLE places_and_location_info')
#     db.commit()
#     print('sucess')
# checking()


output = checking()
# print(f'output is- {output}')
for t_data in output:
    print(t_data)
# print(output)
