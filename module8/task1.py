# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and
# -location (town) from the airport database used on this course.
#  ICAO codes are stored in the ident column of the airport table.


import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="flight_game"
)
def search_for_airport(user_input):
    cursor=connection.cursor()
    cursor.execute(f" select name,municipality, wikipedia_link,type  from airport where ident='{user_input}';")  #i have added extra wiki..link and type which is not mentioned in the question
    result=cursor.fetchall()

    for  data in result:
        print(data)
        cursor.close()

icao_code=input("Enter the ICAO code: ")
search_for_airport(icao_code)