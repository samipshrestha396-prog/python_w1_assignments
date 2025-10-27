# Write a program that asks the user to enter the ICAO codes of two airports.
# The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE,
# write geopy into the search field and finish the installation.

from geopy import distance
import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="flight_game"
)



def search_for_distance(icao1_value,icao2_value):
    cursor=connection.cursor()
    cursor.execute( F"select latitude_deg,longitude_deg from airport where ident='{icao1_value}';")
    result1 = cursor.fetchone() #fechall retrieve all the data but fetchon retrieve one row
    cursor.execute(F"select latitude_deg,longitude_deg from airport where ident='{icao2_value}';")
    result2=cursor.fetchone()
    if len(result1) and len(result2)==2:
        deg1=(result1[0],result1[1])
        deg2 = (result2[0], result2[1])
        total_dis=distance.distance(deg1,deg2).km
        print("Total distanck between two airport is=" ,total_dis,"km")



input_icao1 = input("Enter the ICAO code of 1st port: ").upper()
input_icao2=  input("Enter the ICAO code of 2st port: ").upper()
search_for_distance(input_icao1,input_icao2)