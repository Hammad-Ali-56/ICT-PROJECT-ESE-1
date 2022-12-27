import pandas as pd
import pickle
import csv


files = "info.pkl"
filesobj = open(files, 'rb')  # reading the file
info = pickle.load(filesobj)  # storing content of file in
print(info)

ab = pd.read_pickle("info.pkl")
df=pd.DataFrame(ab)
df.to_csv("display.csv",index =False)
print(df)