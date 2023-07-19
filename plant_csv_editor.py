import datetime
from datetime import timedelta

import csv
import os

#Insert path of .csv file
path = r'INSERT PATH OF CSV'
filename = 'list_of_plants.csv'

fields = ['name', 'watered', 'frequency']

#Reading csv
if os.path.isfile(path):
    with open(filename, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        plants = list(reader)
else:
        plants = [
        {
            "name":'plant',
            "watered":datetime.date.today(),
            "frequency":5
        }
    ]

#Main Loop
while(1):
    for i in range(len(plants)):
        print("{}: {}\n".format(i + 1, plants[i]["name"]))

    print("Input number for plant to edit or \'n\' for a new plant, \'d\' to delete, or \'e\' to exit")
    userin = input()

    #New plant
    if userin == "n":
        print("Input name for plant, \'c\' to cancel creation")
        plantname = input()
        if plantname == "c":
            continue
        print("Input days since watered, \'c\' to cancel creation")
        watereddays = input()
        if watereddays == "c":
            continue
        print("Input frequency for watering in days, \'c\' to cancel creation")
        wateringfreq = input()
        if wateringfreq == "c":
            continue
        plants.append({'name': plantname,'watered': datetime.date.today() - timedelta(days=int(watereddays)) , 'frequency': int(wateringfreq)})
        continue

    #Delete plant
    if userin == "d":
        print("Input number for plant deletion, \'c\' to cancel")
        userin = input()
        if userin == "c":
            continue
        plants.pop(int(userin) - 1)
        continue

    #Exit        
    if userin == "e":
        break

    #Edit plant
    if int(userin) in range(len(plants)):
        #Field input
        print("Choose from fields: (or \'c\' for cancel)\n")
        for field in fields:
            print("{} ".format(field))
        print("\n")

        userfield = input()
        if userfield == "c":
            continue

        #New value
        print("Editing {}. (\'c\' to cancel)".format(userfield))
        newkey = input()

        if userfield == "c":
            continue

        if userfield in fields:
            plants[int(userin)][userfield] = newkey
        else:
            print("Failed ({} is not a field)".format(userfield))
        

#Writing csv
with open(filename,'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fields)
    writer.writeheader()
    writer.writerows(plants)