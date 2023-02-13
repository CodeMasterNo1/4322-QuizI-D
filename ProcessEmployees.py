"""
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
"""

import csv

# open the file

in_file = open("employee_data.csv", "r")
reader = csv.reader(in_file, delimiter=",")
next(reader)

# create an empty dictionary
marketing_salary_dict = {}

# use a loop to iterate through the csv file
for row in reader:
    current_salary = row[5]
     # check if the employee fits the search criteria
    if row[3] == "Marketing":
        print(
            "Manager Name: ", row[1] + row[2], "Current Salary: ", "$ " + current_salary
        )
        full_name = row[1] + row[2]
       

print()
print("=========================================")
print()

# iternate through the dictionary and print out the key and value as per printout
for row in reader:
    current_salary = row[5]
     # check if the employee fits the search criteria
    if row[3] == "Marketing":
        print(
            "Manager Name: ", row[1] + row[2], "New Salary: ", "$ " + current_salary
        )
        full_name = row[1] + row[2]
        marketing_salary_dict [full_nam