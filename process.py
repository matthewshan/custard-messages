import json, random, re
import tensorflow as tf
from tensorflow import keras 


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

# Message Data is in the format of [String: msg, int: user]

random.shuffle(message_data)
training_data = message_data[0:int(len(message_data)*.8)]
test_data = message_data[int(len(message_data)*.8):-1]

word_freq = {}

# Create word index
word_set = {training_data[0][0]}
for msg, user in training_data:
    msg_words = msg.split(" ") 
    msg_words = map(lambda word: re.sub(r'\W+', '', word), msg_words)
    print(msg_words)
    for word in msg_words:
        word_set.add(word) 

# TODO: sory works by frequency
    
word_index = {}
word_index_reverse = {} 
i = 0
for word in word_set:
    word_index[word] = i
    word_index_reverse[i] = word
    i += 1

print(word_index)

model = keras.Sequential([

])

# all_text = ''
# for data in message_data:
#     all_text += data[0] + ' '

# words_matrix = keras.preprocessing.text.Tokenizer(50000)
# Tokenizor: https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer
# https://towardsdatascience.com/text-classification-in-keras-part-2-how-to-use-the-keras-tokenizer-word-representations-fd571674df23

