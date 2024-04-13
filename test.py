import pandas as pd
import os
import platform

def import_csv():
    OS = platform.system()
    
    if OS == "Linux":
        df = pd.read_csv(os.getcwd() + "/tweets/tweets_labelled_09042020_16072020.csv", sep=";")
    elif OS == "Windows":
        pass
    else:
        print("nope")
    
    return df



df = import_csv()
