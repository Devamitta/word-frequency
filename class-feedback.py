
import pandas as pd
import random

df = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# change Meaning in native language
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Meaning in native language']] = ""

# filter all classes words
test2 = df['class'] != ""
filter = test2
df = df.loc[filter]

# adding feedback
df.reset_index(drop=True, inplace=True)
df['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df.Pāli1 + """&entry.1433863141=Pāli Class Vocab">Fix it here</a>."""

# replace all Pattern with '_'
# df['Pattern'] = df['Pattern'].str.replace(' ', '-')


# choosing order of columns
df = df[['Pāli1', 'POS', 'Grammar', 'Derived from', 'Neg', 'Verb', 'Trans', 'Case', 'Meaning IN CONTEXT', 'Meaning in native language', 'Pāli Root', 'Base', 'Construction', 'Sanskrit', 'Sk Root', 'Variant', 'Notes', 'Source1', 'Sutta1', 'Example1', 'Source 2', 'Sutta2', 'Example 2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Stem', 'Pattern', 'Test', 'class', 'count', 'Feedback']]

# sort by frequency
# df = df.sort_values(by=['count'], ascending = False)
# df.sort_values(["count"], ascending=False, inplace=True)
df.sort_values(by = ['count'], ignore_index=True, ascending=False, inplace=True)

# save csv
df.to_csv("csv-for-examples/all.csv", sep="\t", index=None)

# filter 1 classes words
test1 = df['class'] == "1"
filter = test1
df_1 = df.loc[filter]

# filter 2 classes words
test2 = df['class'] == "2"
filter = test2
df_2 = df.loc[filter]

# filter 3 classes words
test3 = df['class'] == "3"
filter = test3
df_3 = df.loc[filter]

# filter 4 classes words
test4 = df['class'] == "4"
filter = test4
df_4 = df.loc[filter]

# filter 5 classes words
test5 = df['class'] == "5"
filter = test5
df_5 = df.loc[filter]

# filter 6 classes words
test6 = df['class'] == "6"
filter = test6
df_6 = df.loc[filter]

# filter 7 classes words
test7 = df['class'] == "7"
filter = test7
df_7 = df.loc[filter]

# filter 8 classes words
test8 = df['class'] == "8"
filter = test8
df_8 = df.loc[filter]

# filter 9 classes words
test9 = df['class'] == "9"
filter = test9
df_9 = df.loc[filter]

# filter 10 classes words
test10 = df['class'] == "10"
filter = test10
df_10 = df.loc[filter]

# filter 11 classes words
test11 = df['class'] == "11"
filter = test11
df_11 = df.loc[filter]

# filter 12 classes words
test12 = df['class'] == "12"
filter = test12
df_12 = df.loc[filter]

# filter 13 classes words
test13 = df['class'] == "13"
filter = test13
df_13 = df.loc[filter]

# combine classes
df_comb_2 = pd.concat([df_1, df_2])
df_comb_3 = pd.concat([df_1, df_2, df_3])
df_comb_4 = pd.concat([df_1, df_2, df_3, df_4])
df_comb_5 = pd.concat([df_1, df_2, df_3, df_4, df_5])
df_comb_6 = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6])
df_comb_7 = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7])
df_comb_8 = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8])
df_comb_9 = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9])
df_comb_10 = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10])
df_comb_11 = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11])
df_comb_12 = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12])
df_comb_13 = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13])


# save classes csv
df_1.to_csv("csv-for-examples/1-class.csv", sep="\t", index=None)
df_comb_2.to_csv("csv-for-examples/2-class.csv", sep="\t", index=None)
df_comb_3.to_csv("csv-for-examples/3-class.csv", sep="\t", index=None)
df_comb_4.to_csv("csv-for-examples/4-class.csv", sep="\t", index=None)
df_comb_5.to_csv("csv-for-examples/5-class.csv", sep="\t", index=None)
df_comb_6.to_csv("csv-for-examples/6-class.csv", sep="\t", index=None)
df_comb_7.to_csv("csv-for-examples/7-class.csv", sep="\t", index=None)
df_comb_8.to_csv("csv-for-examples/8-class.csv", sep="\t", index=None)
df_comb_9.to_csv("csv-for-examples/9-class.csv", sep="\t", index=None)
df_comb_10.to_csv("csv-for-examples/10-class.csv", sep="\t", index=None)
df_comb_11.to_csv("csv-for-examples/11-class.csv", sep="\t", index=None)
df_comb_12.to_csv("csv-for-examples/12-class.csv", sep="\t", index=None)
df_comb_13.to_csv("csv-for-examples/13-class.csv", sep="\t", index=None)

