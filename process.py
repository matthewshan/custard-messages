import json
import tensorflow as tf

with open("custard.json", "r", encoding="utf-8") as file:
    data = json.load(file)

names = []
message_data = []

# Generates the user name list
for i in data["meta"]["users"].keys():
    names.append(tuple((i, data["meta"]["users"][i]["name"])))

# Generates the messages data list
for channels in data["data"].keys():
    #print(data["data"][channels])
    for messages in data["data"][channels]:
        mes = data["data"][channels][messages]
        if (not ('e' in mes or 'a' in mes) and 'u' in mes and 'm' in mes 
            and not ((mes['u'] >= 7 and mes['u'] <= 11) or mes['u'] == 16)):
            message_data.append(tuple((mes['m'], mes['u'])))
        # {'u': 0, 't': 1579732817225, 'm': 'Nahh coke is good, esp Mexican coke', 'te': 1579732849600}

print(message_data)
        





