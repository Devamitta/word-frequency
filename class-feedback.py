import pandas as pd
import random
import numpy as np
from pandas_ods_reader import read_ods 
import re
from natsort import index_natsorted

df = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# change Meaning in native language
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Meaning in native language']] = ""

# filter all classes words
# test2 = df['class'] != ""
# filter = test2
# df = df.loc[filter]

# adding feedback
df.reset_index(drop=True, inplace=True)
df['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df.Pāli1 + """&entry.1433863141=Pāli Class Vocab">Fix it here</a>."""


# choosing order of columns
df = df[['Pāli1', 'POS', 'Grammar', 'Derived from', 'Neg', 'Verb', 'Trans', 'Case', 'Meaning IN CONTEXT', 'Meaning in native language', 'Pāli Root', 'Base', 'Construction', 'Sanskrit', 'Sk Root', 'Variant', 'Notes', 'Source1', 'Sutta1', 'Example1', 'Source 2', 'Sutta2', 'Example 2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Stem', 'Pattern', 'Test', 'ex', 'class', 'count', 'Feedback']]

# sort by frequency
df.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df['count'])))

# save csv
# df.to_csv("csv-for-examples/all.csv", sep="\t", index=None)

# filter 0 classes words
test1 = df['ex'] == "0"
filter = test1
df_0 = df.loc[filter]

# filter 1
test1 = df['class'] == "1"
filter = test1
df_1_cl = df.loc[filter]

test1 = df['ex'] == "1"
filter = test1
df_1 = df.loc[filter]

df_comb_1 = pd.concat([df_0, df_1])

# keep only unique 1
logix = df_1_cl['Pāli1'].isin(df_comb_1['Pāli1'])
df_1_cl_u = df_1_cl.drop(df_1_cl[logix].index)

df_comb_1_f = pd.concat([df_comb_1, df_1_cl_u])

print("1 done")

# filter 2
test2 = df['class'] == "2"
filter = test2
df_2_cl = df.loc[filter]
df_2_cl_comb = pd.concat([df_1_cl, df_2_cl])

test2 = df['ex'] == "2"
filter = test2
df_2 = df.loc[filter]

df_comb_2 = pd.concat([df_0, df_1, df_2])

# keep only unique 2
logix = df_2_cl_comb['Pāli1'].isin(df_comb_2['Pāli1'])
df_2_cl_u = df_2_cl_comb.drop(df_2_cl_comb[logix].index)

df_comb_2_f = pd.concat([df_comb_2, df_2_cl_u])

print("2 done")

# filter 3
test3 = df['class'] == "3"
filter = test3
df_3_cl = df.loc[filter]
df_3_cl_comb = pd.concat([df_1_cl, df_2_cl, df_3_cl])

test3 = df['ex'] == "3"
filter = test3
df_3 = df.loc[filter]

df_comb_3 = pd.concat([df_0, df_1, df_2, df_3])

# keep only unique 3
logix = df_3_cl_comb['Pāli1'].isin(df_comb_3['Pāli1'])
df_3_cl_u = df_3_cl_comb.drop(df_3_cl_comb[logix].index)

df_comb_3_f = pd.concat([df_comb_3, df_3_cl_u])

print("3 done")

# filter 4
test4 = df['class'] == "4"
filter = test4
df_4_cl = df.loc[filter]
df_4_cl_comb = pd.concat([df_1_cl, df_2_cl, df_3_cl, df_4_cl])

test4 = df['ex'] == "4"
filter = test4
df_4 = df.loc[filter]

df_comb_4 = pd.concat([df_0, df_1, df_2, df_3, df_4])

# keep only unique 4
logix = df_4_cl_comb['Pāli1'].isin(df_comb_4['Pāli1'])
df_4_cl_u = df_4_cl_comb.drop(df_4_cl_comb[logix].index)

df_comb_4_f = pd.concat([df_comb_4, df_4_cl_u])

print("4 done")

# filter 5
test5 = df['class'] == "5"
filter = test5
df_5_cl = df.loc[filter]
df_5_cl_comb = pd.concat([df_1_cl, df_2_cl, df_3_cl, df_4_cl, df_5_cl])

test5 = df['ex'] == "5"
filter = test5
df_5 = df.loc[filter]

df_comb_5 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5])

# keep only unique 5
logix = df_5_cl_comb['Pāli1'].isin(df_comb_5['Pāli1'])
df_5_cl_u = df_5_cl_comb.drop(df_5_cl_comb[logix].index)

df_comb_5_f = pd.concat([df_comb_5, df_5_cl_u])

print("5 done")

# filter 6
test6 = df['class'] == "6"
filter = test6
df_6_cl = df.loc[filter]
df_6_cl_comb = pd.concat([df_1_cl, df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl])

test6 = df['ex'] == "6"
filter = test6
df_6 = df.loc[filter]

df_comb_6 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6])

# keep only unique 6
logix = df_6_cl_comb['Pāli1'].isin(df_comb_6['Pāli1'])
df_6_cl_u = df_6_cl_comb.drop(df_6_cl_comb[logix].index)

df_comb_6_f = pd.concat([df_comb_6, df_6_cl_u])

print("6 done")

# filter 7
test7 = df['class'] == "7"
filter = test7
df_7_cl = df.loc[filter]
df_7_cl_comb = pd.concat([df_1_cl, df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl])

test7 = df['ex'] == "7"
filter = test7
df_7 = df.loc[filter]

df_comb_7 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7])

# keep only unique 7
logix = df_7_cl_comb['Pāli1'].isin(df_comb_7['Pāli1'])
df_7_cl_u = df_7_cl_comb.drop(df_7_cl_comb[logix].index)

df_comb_7_f = pd.concat([df_comb_7, df_7_cl_u])

print("7 done")

# filter 8
test8 = df['class'] == "8"
filter = test8
df_8_cl = df.loc[filter]
df_8_cl_comb = pd.concat([df_1_cl, df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl])

test8 = df['ex'] == "8"
filter = test8
df_8 = df.loc[filter]

df_comb_8 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8])

# keep only unique 8
logix = df_8_cl_comb['Pāli1'].isin(df_comb_8['Pāli1'])
df_8_cl_u = df_8_cl_comb.drop(df_8_cl_comb[logix].index)

df_comb_8_f = pd.concat([df_comb_8, df_8_cl_u])

print("8 done")

# filter 9
test9 = df['class'] == "9"
filter = test9
df_9_cl = df.loc[filter]
df_9_cl_comb = pd.concat([df_1_cl, df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl])

test9 = df['ex'] == "9"
filter = test9
df_9 = df.loc[filter]

df_comb_9 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9])

# keep only unique 9
logix = df_9_cl_comb['Pāli1'].isin(df_comb_9['Pāli1'])
df_9_cl_u = df_9_cl_comb.drop(df_9_cl_comb[logix].index)

df_comb_9_f = pd.concat([df_comb_9, df_9_cl_u])

print("9 done")

# filter 10
test10 = df['class'] == "10"
filter = test10
df_10_cl = df.loc[filter]
df_10_cl_comb = pd.concat([df_1_cl, df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl])

test10 = df['ex'] == "10"
filter = test10
df_10 = df.loc[filter]

df_comb_10 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10])

# keep only unique 10
logix = df_10_cl_comb['Pāli1'].isin(df_comb_10['Pāli1'])
df_10_cl_u = df_10_cl_comb.drop(df_10_cl_comb[logix].index)

df_comb_10_f = pd.concat([df_comb_10, df_10_cl_u])

print("10 done")

# filter 11
test11 = df['class'] == "11"
filter = test11
df_11_cl = df.loc[filter]
df_11_cl_comb = pd.concat([df_1_cl, df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl])

test11 = df['ex'] == "11"
filter = test11
df_11 = df.loc[filter]

df_comb_11 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11])

# keep only unique 11
logix = df_11_cl_comb['Pāli1'].isin(df_comb_11['Pāli1'])
df_11_cl_u = df_11_cl_comb.drop(df_11_cl_comb[logix].index)

df_comb_11_f = pd.concat([df_comb_11, df_11_cl_u])

print("11 done")

# filter 12
test12 = df['class'] == "12"
filter = test12
df_12_cl = df.loc[filter]
df_12_cl_comb = pd.concat([df_1_cl, df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl])

test12 = df['ex'] == "12"
filter = test12
df_12 = df.loc[filter]

df_comb_12 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12])

# keep only unique 12
logix = df_12_cl_comb['Pāli1'].isin(df_comb_12['Pāli1'])
df_12_cl_u = df_12_cl_comb.drop(df_12_cl_comb[logix].index)

df_comb_12_f = pd.concat([df_comb_12, df_12_cl_u])

print("12 done")

# filter 13
test13 = df['class'] == "13"
filter = test13
df_13_cl = df.loc[filter]
df_13_cl_comb = pd.concat([df_1_cl, df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl])

test13 = df['ex'] == "13"
filter = test13
df_13 = df.loc[filter]

df_comb_13 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13])

# keep only unique 13
logix = df_13_cl_comb['Pāli1'].isin(df_comb_13['Pāli1'])
df_13_cl_u = df_13_cl_comb.drop(df_13_cl_comb[logix].index)

df_comb_13_f = pd.concat([df_comb_13, df_13_cl_u])

print("13 done")

# save classes csv
df_0.to_csv("csv-for-examples/0-class.csv", sep="\t", index=None)
df_comb_1_f.to_csv("csv-for-examples/1-class.csv", sep="\t", index=None)
df_comb_2_f.to_csv("csv-for-examples/2-class.csv", sep="\t", index=None)
df_comb_3_f.to_csv("csv-for-examples/3-class.csv", sep="\t", index=None)
df_comb_4_f.to_csv("csv-for-examples/4-class.csv", sep="\t", index=None)
df_comb_5_f.to_csv("csv-for-examples/5-class.csv", sep="\t", index=None)
df_comb_6_f.to_csv("csv-for-examples/6-class.csv", sep="\t", index=None)
df_comb_7_f.to_csv("csv-for-examples/7-class.csv", sep="\t", index=None)
df_comb_8_f.to_csv("csv-for-examples/8-class.csv", sep="\t", index=None)
df_comb_9_f.to_csv("csv-for-examples/9-class.csv", sep="\t", index=None)
df_comb_10_f.to_csv("csv-for-examples/10-class.csv", sep="\t", index=None)
df_comb_11_f.to_csv("csv-for-examples/11-class.csv", sep="\t", index=None)
df_comb_12_f.to_csv("csv-for-examples/12-class.csv", sep="\t", index=None)
df_comb_13_f.to_csv("csv-for-examples/13-class.csv", sep="\t", index=None)

print("csv-for-examples saved")

# generate random number 1-100
ran = random.sample(range(1, 100), 1)
ran = str(ran[0])

# change Test
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Test']] = ran

print(f"test number : {ran}")

# replace all Pattern with '_'
df['Pattern'] = df['Pattern'].str.replace(' ', '-')

# change Pattern of ind
test1 = df['Pattern'] == ""
filter = test1
df.loc[filter, ['Pattern']] = df['POS']

df = df[['Pāli1', 'POS', 'Grammar', 'Derived from', 'Neg', 'Verb', 'Trans', 'Case', 'Meaning IN CONTEXT', 'Meaning in native language', 'Pāli Root', 'Base', 'Construction', 'Sanskrit', 'Sk Root', 'Notes', 'Source1', 'Sutta1', 'Example1', 'Source 2', 'Sutta2', 'Example 2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Pattern', 'Test', 'ex', 'count', 'Feedback']]

df.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df['count'])))

# filter 0 classes words
test1 = df['ex'] == "0"
filter = test1
df_0 = df.loc[filter]

# filter 1 classes words
test1 = df['ex'] == "1"
filter = test1
df_1 = df.loc[filter]

# filter 2 classes words
test2 = df['ex'] == "2"
filter = test2
df_2 = df.loc[filter]

# filter 3 classes words
test3 = df['ex'] == "3"
filter = test3
df_3 = df.loc[filter]

# filter 4 classes words
test4 = df['ex'] == "4"
filter = test4
df_4 = df.loc[filter]

# filter 5 classes words
test5 = df['ex'] == "5"
filter = test5
df_5 = df.loc[filter]

# filter 6 classes words
test6 = df['ex'] == "6"
filter = test6
df_6 = df.loc[filter]

# filter 7 classes words
test7 = df['ex'] == "7"
filter = test7
df_7 = df.loc[filter]

# filter 8 classes words
test8 = df['ex'] == "8"
filter = test8
df_8 = df.loc[filter]

# filter 9 classes words
test9 = df['ex'] == "9"
filter = test9
df_9 = df.loc[filter]

# filter 10 classes words
test10 = df['ex'] == "10"
filter = test10
df_10 = df.loc[filter]

# filter 11 classes words
test11 = df['ex'] == "11"
filter = test11
df_11 = df.loc[filter]

# filter 12 classes words
test12 = df['ex'] == "12"
filter = test12
df_12 = df.loc[filter]

# filter 13 classes words
test13 = df['ex'] == "13"
filter = test13
df_13 = df.loc[filter]

# save classes csv

df_0.to_csv("csv-for-anki/0-class.csv", sep="\t", index=None)
df_1.to_csv("csv-for-anki/1-class.csv", sep="\t", index=None)
df_2.to_csv("csv-for-anki/2-class.csv", sep="\t", index=None)
df_3.to_csv("csv-for-anki/3-class.csv", sep="\t", index=None)
df_4.to_csv("csv-for-anki/4-class.csv", sep="\t", index=None)
df_5.to_csv("csv-for-anki/5-class.csv", sep="\t", index=None)
df_6.to_csv("csv-for-anki/6-class.csv", sep="\t", index=None)
df_7.to_csv("csv-for-anki/7-class.csv", sep="\t", index=None)
df_8.to_csv("csv-for-anki/8-class.csv", sep="\t", index=None)
df_9.to_csv("csv-for-anki/9-class.csv", sep="\t", index=None)
df_10.to_csv("csv-for-anki/10-class.csv", sep="\t", index=None)
df_11.to_csv("csv-for-anki/11-class.csv", sep="\t", index=None)
df_12.to_csv("csv-for-anki/12-class.csv", sep="\t", index=None)
df_13.to_csv("csv-for-anki/13-class.csv", sep="\t", index=None)

# combine classes
# df_comb = pd.concat([df_0, df_1])
# df_comb = pd.concat([df_0, df_1, df_2])
# df_comb = pd.concat([df_0, df_1, df_2, df_3])
# df_comb = pd.concat([df_0, df_1, df_2, df_3, df_4])
# df_comb = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5])
# df_comb = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6])
# df_comb = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7])
# df_comb = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8])
# df_comb = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9])
# df_comb = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10])
# df_comb = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11])
# df_comb = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12])
df_comb = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13])


df_comb.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_comb['count'])))


df_comb.to_csv("csv-for-anki/all-class.csv", sep="\t", index=None)