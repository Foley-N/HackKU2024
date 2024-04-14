import pandas as pd
import os
import platform
import vaderSentiment as vs
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def import_csv():
    OS = platform.system()

    if OS == "Linux":
        df = pd.read_csv(os.getcwd() + "/tweets/tweets_labelled_09042020_16072020.csv", sep=";")
    elif OS == "Windows":
        df = pd.read_csv(os.getcwd() + "\\tweets\\tweets_labelled_09042020_16072020.csv", sep=";")
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

def filterByDate(df, dateList):
    df.sort_values(by='created_at', inplace=True)
    mask = map((lambda x : search(x, dateList)), list)
    bools = pd.Series(mask)
    return df[bool.values]

import datetime

def dateRangeDist(sYear,sMonth,sDay, eYear, eMonth, eDay):
  start = datetime.date(sYear, sMonth, sDay)
  end = datetime.date(eYear, eMonth, eDay)
  date_list = [f"{date.year}-{date.month}-{date.day}" for date in (start + datetime.timedelta(days=x) for x in range((end-start).days + 1))]
  return date_list

df = import_csv()

sentences = df['text'].tolist()

newDF = searchDF(df, sentences, ['$AMZN'])

print(dateRangeDist(2020, 4, 15, 2020, 7, 15))

print(filterByDate(newDF, 4))

"""print(df.head())

sentences = df['text'].tolist()

analyzer = SentimentIntensityAnalyzer()

sentence = analyzer.polarity_scores(sentences[115])
print(sentences[115])
print(sentence)

for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs))) """