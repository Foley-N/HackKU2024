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

df = import_csv()

sentences = df['text'].tolist()

print(searchDF(df, sentences, ['$AMZN']))

"""print(df.head())

sentences = df['text'].tolist()

analyzer = SentimentIntensityAnalyzer()

sentence = analyzer.polarity_scores(sentences[115])
print(sentences[115])
print(sentence)

for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs))) """