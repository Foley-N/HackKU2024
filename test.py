import pandas as pd
import os
import platform
import datetime
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

def filterByDate(df, list, dateList):
    df.sort_values(by='created_at', inplace=True)
    mask = map((lambda x : search(x, dateList)), list)
    bools = pd.Series(mask)
    return df[bool.values]

def dateRangeDist(sYear,sMonth,sDay, eYear, eMonth, eDay):
  start = datetime.date(sYear, sMonth, sDay)
  end = datetime.date(eYear, eMonth, eDay)
  date_list = [f"{date.year}-{date.month}-{date.day}" for date in (start + datetime.timedelta(days=x) for x in range((end-start).days + 1))]
  return date_list


df = import_csv()

sentences = df['text'].tolist()

amazonTweets = searchDF(df, sentences, ['$AMZN']).sort_values(by='created_at', ascending=True, na_position='first')

newDF = searchDF(df, sentences, ['$AMZN'])

dates = (dateRangeDist(2020, 4, 15, 2020, 4, 30))

print(filterByDate(newDF, dates, ['$AMZN']))

#amazonText = amazonTweets['text'].tolist()

#analyzer = SentimentIntensityAnalyzer()

"""sentence = analyzer.polarity_scores(sentences[115])
print(sentences[115])
print(sentence)"""

sentimentList = []

for sentence in amazonText:
    vs = analyzer.polarity_scores(sentence)
    sentimentList.append(vs)
    
print(sentimentList)
    

