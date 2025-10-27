# Write a program that asks the user to enter the area code
# (for example FI) and prints out the airports located in that country ordered by airport type.
# For example, Finland has 65 small airports, 15 helicopter airports and so on.
#

import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="flight_game"
)
def search_for_airport(icao_input):
    cursor=connection.cursor()
    cursor.execute(f"select type,count(*) from airport where iso_country='FI'group by type order by type; ")
    result=cursor.fetchall()
    for data in result:
        print(data)
        cursor.close()


user_input=input("Enter the AREA code: ")
search_for_airport(user_input)
connection.close()

