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

def dateRangeDist(sYear,sMonth,sDay, eYear, eMonth, eDay):
  start = datetime.date(sYear, sMonth, sDay)
  end = datetime.date(eYear, eMonth, eDay)
  date_list = [f"{date.year}-{date.month}-{date.day}" for date in (start + datetime.timedelta(days=x) for x in range((end-start).days + 1))]
  return date_list

def filter_by_dates(df, dates):
    df['created_at'] = pd.to_datetime(df['created_at'])
    mask = df['created_at'].isin(dates)
    return df[mask]

def searchDate(date, dateList):
    if any(date in str(date) for date in dateList):
        return True
    else:
        return False

def datetimeTOdate(df):
    df['created_at'] = pd.to_datetime(df['created_at']).dt.date
    return df

df = import_csv()

sentences = df['full_text'].tolist()

amazonTweets = searchDF(df, sentences, ['$AMZN', 'amazon']).sort_values(by='created_at', ascending=True, na_position='first')

newDF = searchDF(df, sentences, ['$AMZN'])

dates = (dateRangeDist(2020, 4, 15, 2020, 4, 30))

#print(filterByDate(newDF, dates, ['$AMZN']))
print(dates)
print(datetimeTOdate(newDF))

print(amazonTweets)
amazonText = amazonTweets['full_text'].tolist()

analyzer = SentimentIntensityAnalyzer()

sentimentList = []

for sentence in amazonText:
    vs = analyzer.polarity_scores(sentence)
    sentimentList.append(vs)
    
sentimentDF = pd.DataFrame(sentimentList)

print(sentimentDF)

amazonTweets['neg'] = sentimentDF['neg'].values
amazonTweets['neu'] = sentimentDF['neu'].values
amazonTweets['pos'] = sentimentDF['pos'].values
amazonTweets['compound'] = sentimentDF['compound'].values

amazonTweets = (datetimeTOdate(amazonTweets))
print(amazonTweets)

negativeSentiment = (sentiment['compound'] for sentiment in sentimentList if sentiment['compound'] < 0)
positiveSentiment = (sentiment['compound'] for sentiment in sentimentList if sentiment['compound'] > 0)

values = amazonTweets.groupby(['created_at'], as_index=False).mean('compound')

positiveSentimentList = values['compound'].tolist()
negativeSentimentList = values['compound'].tolist()

for x in range(0, len(positiveSentimentList)): 
    if positiveSentimentList[x] < 0: 
        positiveSentimentList[x] = 0

for x in range(0, len(negativeSentimentList)): 
    if negativeSentimentList[x] > 0: 
        negativeSentimentList[x] = 0

print(*positiveSentimentList)
print()
print(*negativeSentimentList)

values.drop(columns=['id'], inplace=True)

print(values.iloc[:, 0])

print(values.columns[0])

plt.figure(figsize=(10, 6))
plt.bar(values['created_at'], values['compound'], color=['green' if v > 0 else 'red' for v in values['compound']])
plt.xlabel('Row Index')
plt.ylabel('Sentiment')
plt.title('Bar Graph with Sentiment analysis of amazon tweets over time')
plt.grid(True)
plt.show()

