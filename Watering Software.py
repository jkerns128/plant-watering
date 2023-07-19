import datetime
from datetime import timedelta
from win10toast_click import ToastNotifier

import csv
import os
import time

#plant object:
#name (string)
#last watered (date)
#frequency for watering (days)


#Load csv
path = r'INSERT PATH OF CSV'
filename = 'list_of_plants.csv'

notify = ToastNotifier()

fields = ['name', 'watered', 'frequency']

if os.path.isfile(path):
    with open(filename, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        plants = list(reader)
else:
    print("No csv detected! run csv software to generate")
    time.sleep(5000)
    exit()

def water_plant():
    dict["watered"] = datetime.date.today()
    print("Worked! {}".format(dict["watered"]))

#decide if plants needs to be watered
for dict in plants:
    if datetime.datetime.strptime(str(dict["watered"]), '%Y-%m-%d').date() + timedelta(days=int(dict['frequency'])) < datetime.date.today():
        #send windows notification and update on click
        notify.show_toast("Water {} today!".format(dict['name']),
                    "Plant Supervisor",
                   duration=30,
                   threaded=False,
                   callback_on_click=water_plant)
        
#write csv
with open(filename,'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fields)
    writer.writeheader()
    writer.writerows(plants)







