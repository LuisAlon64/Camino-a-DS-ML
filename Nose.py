import csv
import pandas as pd

with open("train.csv", "r") as t:
    df = pd.read_csv(t)
    print(df)