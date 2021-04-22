
import json
f = open('model-s.txt', 'r')
content = f.readlines()

values = []
number = []
numb = []
sens = 1

for line in content:
    if sens < 70:
        for i in line:
            if i == "[":
                number = ''

            if i == "]":
                values.append(number)
                break
            if i.isdigit() == True:
                number += i
    else:
        if "ACCELEROMETER" in line:
            number = ''
        if "DEVICE_ORIENTATION" in line:
            number = ''
        for i in line:
            if i == ",":
                values.append(number)
                number = ''
            if i == "]":
                values.append(number)
                break
            if i.isdigit() == True:
                number += i

    sens+=1
f.close()

Save = {}
Dataset = []
Sensor = ''
Data = 0
Flag = 0

for Data in values:
    if Flag < 5:
        if Flag == 0:
            Sensor = "LIGHT"
        Save[Sensor] = Data
        Dataset.append(Save)
        Save = {}
    if Flag < 10 and Flag >= 5:
        if Flag == 5:
            Sensor = "PROXIMITY"
        Save[Sensor] = Data
        Dataset.append(Save)
        Save = {}
    if Flag < 25 and Flag >= 10:
        if Flag == 10:
            Sensor = "ACCELEROMETERX"
            i = 0
        if i%3 == 0:
            Save[Sensor] = Data
            Dataset.append(Save)
            Save = {}
        i+=1
    if Flag < 40 and Flag >= 25:
        if Flag == 25:
            i = 0        
        if i%3 == 0:
            Sensor = "ORIENTATIONX"
            Save[Sensor] = Data
            Dataset.append(Save)
            Save = {}
        elif (i-1)%3 == 0:
            Sensor = "ORIENTATIONY"
            Save[Sensor] = Data
            Dataset.append(Save)
            Save = {}
        i+=1
    Flag += 1

JsonData = open("model-s.json", "w")
json.dump(Dataset, JsonData, indent=4, sort_keys=False)
JsonData.close()