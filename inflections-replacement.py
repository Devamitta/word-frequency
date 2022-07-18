import pandas as pd
import csv
import re


def read_inflections_file() -> dict:
    df = pd.read_csv("curated-sources/all_inflections_modified.csv")
    return df.to_dict(orient="records")


def replace_inflections_file():
    df = pd.read_csv("original-sources/all_inflections.csv", sep="\t")
    data = df.to_dict(orient="records")

    csvheader = ["inflection", "headwords"]
    with open("curated-sources/all_inflections_modified.csv", "w") as csvwriter:
        writer = csv.writer(csvwriter, delimiter=",")
        writer.writerow(csvheader)
        for row in data:
            #process inflections
            row["inflection"] = row["inflection"].replace(" ", "")
            #process headwords
            headwords_non_numeric_str = "".join([i for i in row["headwords"] if not i.isdigit()])
            headwords_non_numeric_str = headwords_non_numeric_str.replace(" ", "").replace("[", "").replace("]", "").replace("'", "")
            headwords_list = list(headwords_non_numeric_str.split(","))
            headwords_list = pd.unique(headwords_list).tolist()
            if(len(headwords_list) == 1):
                row["headwords"] = " ".join(map(str, headwords_list))
                csvrow = [row["inflection"], row["headwords"]]
                writer.writerow(csvrow)


replace_inflections_file()
