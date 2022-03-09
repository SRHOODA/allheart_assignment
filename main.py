# pip install beautifulsoup4 requests mysql-connector

from bs4 import BeautifulSoup
import requests
import json
import mysql.connector


with open('config.json') as f:
    params = json.load(f)['params']


place_endpoint = params['place_endpoint']

# "query_by_user": "resturants in mumbai",
# query_by_user = params['query_by_user']  
# query_list = query_by_user.split(' ')
# encoded_query = '+'.join(query_list)    

##we can also take this input from user by defining 2 variables keyword and location
keyword = input('enter the place you want to search for: ')
location = input('enter the location you want to search this place: ')

encoded_query = f'{keyword}+in+{location}'

encoded_url = f'{place_endpoint}?q={encoded_query}'
response = requests.get(f'{encoded_url}') 

# response = requests.get(f'https://www.google.com/maps/search/{encoded_query}/@28.6119787,77.1324426,12z') 
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

# search_results = soup.title.get_text()
# search_results = soup.find('div', attrs = {'class':'X7NTVe'}) 
# search_results = soup.select('.X7NTVe')
search_result_1 = soup.find_all('div', attrs = {'class':'BNeawe deIvCb AP7Wnd'}) 

names = []
for item in search_result_1:
    names.append(item.get_text())


search_result_2 = soup.find_all('div', attrs = {'class':'BNeawe tAd8D AP7Wnd'})

rating_review_address_and_other_details = []
for item in search_result_2:
    # rating_review_address_and_other_details.append((item.get_text()).split(' '))  
    
    rating_review_address_and_other_details.append(item.get_text())  
    #or we can use split() method to store each information separately 
    #and then join the address as a string using join() method.


##connecting with database using connection string.

db = mysql.connector.connect(
    host = params['host'], 
    user = params['user'], 
    passwd = params['passwd'], 
    database = params['database']
)

my_cursor = db.cursor() #create cursor object for executing queries

for i in range(len(names)):

    sql = "INSERT INTO places_and_location_info (place_name, rating_review_address_and_other_details) VALUES (%s, %s)"
    val = (names[i], rating_review_address_and_other_details[i])
    my_cursor.execute(sql, val)
    db.commit()

print('saved sucessfully')

##*To deal with latin letters, i have also used this query as well
# ALTER TABLE python.places_and_location_info MODIFY COLUMN rating_review_address_and_other_details MEDIUMTEXT  
# CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL;


##to check if data is saved properly.
def checking():
    my_cursor.execute('select * from places_and_location_info')
    result = my_cursor.fetchall()
    return result

output = checking()
for t_data in output:
    print(t_data)

