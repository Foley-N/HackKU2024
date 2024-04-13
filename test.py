import pandas as pd
import os

df = pd.read_csv(os.getcwd() + "\\tweets\\tweets_labelled_09042020_16072020.csv", sep=";")

print(df.head())