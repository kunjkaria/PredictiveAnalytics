import csv
import sys

f = open("Customer_data.csv") #Open the original data CSV file 

csv_input_file = csv.reader(f)
policy = []
for row in csv_input_file:
	policy.append(row[11])

policy_set = set(policy) #Creates a set of all the different policies
distinct_policy = list(policy_set) #Creates a list of all the different policies
#distinct_policy.pop(0)


no_of_files = len(distinct_policy) #Finds the count of total number of different policies

policycsv = []

#Create a file with filename as "policy.csv"
for policies in distinct_policy:
	edited_policy_filename = policies + '.csv'
	policycsv.append(edited_policy_filename)

#A function to return all the rows with a particular policy name
def insert_rows(policies):
	g = open("Customer_data.csv")
	csv_input_file1 = csv.reader(g)
	policy_file_list = []
	for policyname in csv_input_file1: #here, policyname = row
		if policies == policyname[11]:
			policy_file_list.append(policyname)
	return policy_file_list
		
#Inserts all the rows in a particular policy.csv file
for i in range(0,no_of_files):
	k = open(policycsv[i], 'w')
	a = csv.writer(k)
	a.writerows(insert_rows(distinct_policy[i])) #insert_rows() is a function that takes policy name as input and returns a list all rows related to that policy 
	k.close()

f.close()
