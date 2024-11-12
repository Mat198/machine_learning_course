#!/usr/bin/python3

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import joblib
import math

enron_data = joblib.load(open("../final_project/final_project_dataset.pkl", "rb"))

print(len(enron_data))

poi_count = 0
show_info_size = True

# To identify how won most money.
lay_pays = 0
skilling_pays = 0
fastow_pays = 0

# Checking for available data
salary_available = 0
email_available = 0

for [key, value] in enron_data.items():
    if show_info_size:
        print("Info of each person:", len(value))
        show_info_size = False
    if value["poi"]:
        poi_count += 1
    
    if value["salary"] != 'NaN':
        salary_available += 1

    if value["email_address"] != 'NaN':
        email_available += 1

    if key == "PRENTICE JAMES":
        print(key, "total stock value is",value['total_stock_value'])

    if key == "COLWELL WESLEY":
        print(key, "emails to poi", value["from_this_person_to_poi"])

    if key == "SKILLING JEFFREY K":
        print(key, "total stock value is",value["exercised_stock_options"])
        print(key, "total payments value is",value["total_payments"])
        skilling_pays_pays = value["total_payments"]
        
    
    if key == "FASTOW ANDREW S":
        print(key, "total payments value is",value["total_payments"])
        fastow_pays = value["total_payments"]

    if key == "LAY KENNETH L":
        print(key, "total payments value is",value["total_payments"])
        lay_pays = value["total_payments"]

if lay_pays > fastow_pays and lay_pays > skilling_pays:
    print("Lay received most money -> $", lay_pays)

if fastow_pays > lay_pays and fastow_pays > skilling_pays:
    print("Fastow received most money -> $", fastow_pays)

if skilling_pays > fastow_pays and skilling_pays > lay_pays:
    print("Skilling received most money -> $", skilling_pays)

print("There are",salary_available,"salaries availables!")
print("There are",email_available,"emails availables!")

print("Number of PoIs:", poi_count)