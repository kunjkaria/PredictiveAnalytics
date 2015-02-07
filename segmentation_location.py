import csv
import sys

f = open("Customer_data.csv") #Open the original data CSV file 

csv_input_file = csv.reader(f)
city = []
for row in csv_input_file:
	city.append(row[4])

city_set = set(city) #Creates a set of all the different cities
distinct_city = list(city_set) #Creates a list of all the different cities
distinct_city.pop(0)


no_of_files = len(distinct_city) #Finds the count of total number of different cities

citycsv = []

#Create a file with filename as "city.csv"
for cities in distinct_city:
	edited_city_filename = cities + '.csv'
	citycsv.append(edited_city_filename)

#A function to return all the rows with a particular city name
def insert_rows(cities):
	g = open("Customer_data.csv")
	csv_input_file1 = csv.reader(g)
	city_file_list = []
	for rowdy in csv_input_file1:
		if cities in rowdy:
			city_file_list.append(rowdy)
	return city_file_list
		
#Inserts all the rows in a particular city.csv file
for i in range(0,no_of_files):
	k = open(citycsv[i], 'w')
	a = csv.writer(k)
	a.writerows(insert_rows(distinct_city[i])) #insert_rows() is a function that takes city name as input and returns a list all rows related to that city 
	k.close()

f.close()
