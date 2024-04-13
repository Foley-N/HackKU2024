import pandas as pd
import os
import platform
import vaderSentiment as vs

def import_csv():
    OS = platform.system()
    
    if OS == "Linux":
        df = pd.read_csv(os.getcwd() + "/tweets/tweets_labelled_09042020_16072020.csv", sep=";")
    elif OS == "Windows":
        df = pd.read_csv(os.getcwd() + "\\tweets\\tweets_labelled_09042020_16072020.csv", sep=";")
    else:
        print("nope")
    
    return df


df = import_csv()

# print(df.head())

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentences = df['text'].tolist()

analyzer = SentimentIntensityAnalyzer()

sentence = analyzer.polarity_scores(sentences[115])
print(sentences[115])
print(sentence)

"""for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))"""
