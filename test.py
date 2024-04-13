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
    if any(word in str(data).lower() for word in wordList):
        return True

print(search('the quick', ['quick']))

df = import_csv()

mask = df.apply(lambda x: x.map(lambda s: search(s, ['$AMZN', 'cnn', 'dinosaur'])))

"""testString = "the quick brown fox"
print(search(testString, ['fox']))"""

"""print(df.head())

sentences = df['text'].tolist()

analyzer = SentimentIntensityAnalyzer()

sentence = analyzer.polarity_scores(sentences[115])
print(sentences[115])
print(sentence)"""

filtered_df = df.loc[mask.any(axis=1)]
print(filtered_df)

"""for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))"""
