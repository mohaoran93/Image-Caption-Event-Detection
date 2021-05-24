import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

# pip install --upgrade gensim
# from gensim.models import Word2Vec
# import nltk
# nltk.download('punkt')
import numpy as np

oscar_words = "src/comparison_nt2_oscar/oscar_words.json"
nt2_words = "src/comparison_nt2_oscar/nt2_words.json"


with open(oscar_words,'r') as f1, open(nt2_words,'r') as f2:
    oscar_json = json.load(f1)
    nt2_json = json.load(f2)

# for w,c in oscar_json.items():
#     print(w,c)

df1 = pd.DataFrame(nt2_json.items(),columns=["words","count"])
df1 = df1.sort_values(by="count",ascending=False)
print(df1.head())

df2 = pd.DataFrame(oscar_json.items(),columns=["words","count"])
df2 = df2.sort_values(by="count",ascending=False)
print(df2.head())

top = 1000000
x1 = list(range(len(df1['words'][0:top])))
y1 = np.log(df1['count'][0:top])
# y1 = df1['count'][0:top]
x2 = list(range(len(df2['words'][0:top])))
y2 = np.log(df2['count'][0:top])
# y2 = df2['count'][0:top]


# fig, ax = plt.subplots()
# ax.plot(x1,y1)
# ax.plot(x2,y2)

fig, ax = plt.subplots()
plt.plot(x1,y1,"r^",x2,y2,"bs")

ax.set(xlabel='top words', ylabel='len(word_frequency)',
       title='words frequency of Oscar(Blue) and NeuralTalk(Red) on flickr30k')
# print("y1: ", list(y1))
# print("y2: ", list(y2))
plt.show()
