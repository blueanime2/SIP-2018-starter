'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below! 
tweet_text = []
tweetstring = ""
for tweet in tweetData:
    tweetstring += tweet['text']
    x = tweet['text']
    tweet_text.append(x)
# print(tweetstring)

# Textblob sample:
polarity = []
subjectivity = []

# print(tweet_text)
for tweet in tweet_text:
    tb = TextBlob(tweet)
    subjectivity.append(tb.subjectivity)
    polarity.append(tb.polarity)
tweetBlob = TextBlob(tweetstring)
word_dict = {}
for word in tweetBlob.words:
    word_dict[word.lower()] = tweetBlob.word_counts[word.lower()]
    print(word_dict)



# print(subjectivity)
# print(polarity)

# y = sum(polarity)/len(polarity)
# w = sum(subjectivity)/len(subjectivity)
# print(y)
# print(w)

# import matplotlib.pyplot as plt

# plt.hist(polarity, bins=[-1, -0.5, 0.0, 0.5, 1])
# plt.hist(subjectivity, bins=[-1, -0.5, 0.0, 0.5, 1])
# plt.xlabel('Values')
# plt.ylabel('Number of Items')
# plt.title('Histogram of Numbers')
# plt.axis([-1.1, 1.1, 0, 100])
# plt.grid(True)
# plt.show()