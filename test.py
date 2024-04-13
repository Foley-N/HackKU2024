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
    
def searchList(list, wordList): # list is the list your searching through and Word list is the list of words you want to search for
    return map((lambda x : search(x, wordList)), list)

df = import_csv()

sentences = df['text'].tolist()
mask = searchList(sentences, ['fox'])

print(list(mask))



# filtered_df = df.loc[mask.any(axis=1)]

"""testString = "the quick brown fox"
print(search(testString, ['fox']))"""

"""print(df.head())

sentences = df['text'].tolist()

analyzer = SentimentIntensityAnalyzer()

sentence = analyzer.polarity_scores(sentences[115])
print(sentences[115])
print(sentence)"""

"""for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs))) """