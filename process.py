import json, random, re
import tensorflow as tf
from tensorflow import keras 
from nltk.stem import PorterStemmer

ps = PorterStemmer()

def filter_word(word):
    return ps.stem(re.sub(r'\W+', '', word).lower())

INDEX_SIZE = 10000

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

#TODO: Split the data and the label
training_data = message_data[0:int(len(message_data)*.8)]
test_data = message_data[int(len(message_data)*.8):-1]



# Create word index
word_freq = {}
for msg, user in training_data:
    msg_words = msg.split(" ") 
    msg_words = map(filter_word, msg_words)
    for word in msg_words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
word_index = {}
word_index_reverse = {} 
i = 0
for word, freq in word_freq:
    word_index[word] = i
    word_index_reverse[i] = word
    i += 1
    if(i >= INDEX_SIZE):
        break

print(word_index)

model = keras.Sequential([
    #https://keras.io/layers/embeddings/
    keras.layers.Embedding(len(word_index), 48),
    keras.layers.GlobalAveragePooling1D(),
    keras.layers.Dense(48, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")
])

model.summary()

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
