import pandas as pd
import os
import platform
import datetime
import vaderSentiment as vs
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def import_csv():
    OS = platform.system()

    if OS == "Linux":
        df = pd.read_csv(os.getcwd() + "/tweets/tweets_remaining_09042020_16072020.csv", sep=";")
    elif OS == "Windows":
        df = pd.read_csv(os.getcwd() + "\\tweets\\tweets_remaining_09042020_16072020.csv", sep=";")
    else:
        print("nope")

    return df

def search(data, wordList):
    if any(word.lower() in str(data).lower() for word in wordList):
        return True
    else:
        return False

def searchDF(df, list, wordList):
    mask = map((lambda x : search(x, wordList)), list)
    bools = pd.Series(mask)
    return df[bools.values]

def datetimeTOdate(df):
    df['created_at'] = pd.to_datetime(df['created_at']).dt.date
    return df

df = import_csv()

sentences = df['full_text'].tolist()

user_inputs = []

while True:
    user_input = input("Enter a value (type 'done' when finished): ")
    if user_input.lower() == 'done':
        break
    user_inputs.append(user_input)
    
amazonTweets = searchDF(df, sentences, user_inputs).sort_values(by='created_at', ascending=True, na_position='first')
amazonText = amazonTweets['full_text'].tolist()

analyzer = SentimentIntensityAnalyzer()
sentimentList = []

for sentence in amazonText:
    vs = analyzer.polarity_scores(sentence)
    sentimentList.append(vs)
    
sentimentDF = pd.DataFrame(sentimentList)

amazonTweets['neg'] = sentimentDF['neg'].values
amazonTweets['neu'] = sentimentDF['neu'].values
amazonTweets['pos'] = sentimentDF['pos'].values
amazonTweets['compound'] = sentimentDF['compound'].values
amazonTweets = (datetimeTOdate(amazonTweets))

values = amazonTweets.groupby(['created_at'], as_index=False).mean('compound')
plt.figure(figsize=(10, 6))
plt.bar(values['created_at'], values['compound'], color=['green' if v > 0 else 'red' for v in values['compound']])
plt.xlabel('Row Index')
plt.ylabel('Sentiment')
plt.title('Bar Graph with Sentiment analysis of amazon tweets over time')
plt.grid(True)
plt.show()

