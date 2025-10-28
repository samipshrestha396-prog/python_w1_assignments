
# Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport,
# fetch the information of an existing airport or quit. If the user chooses to enter a new airport,
# the program asks the user to enter the ICAO code and name of the airport.
# If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport and
# prints out the corresponding name. If the user chooses to quit,
# the program execution ends. The user can choose a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK.
# You can easily find the ICAO codes of different airports online.)
#
airports={
    "abcd":"imadol airport",
    "efgh":"sanagaun  airport",
    "ijkl":" balkumari airport"

}
print("Store airports: YES OR NO ")
print("Fetch airport: YES OR NO ")
print("Exit : Press enter OR type Yes")

while True:
    new_airport=input("Do you want to store new airport:")
    if new_airport == "yes":
        input_icao = input("Enter the ICAO code: ")
        input_name = input("Enter the air port name : ")
        airports.update({input_icao: input_name})
        print("Stored successfully!")
    if new_airport=="no":
        continue


    fetch_airport = input("Do you want to fetch the airport:")
    if  fetch_airport=="yes":
        input_icao = input("Enter the ICAO code: ")
        print(airports[input_icao])





    if new_airport=="" and fetch_airport=="":
        print(airports)
