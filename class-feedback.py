import pandas as pd
import random
import numpy as np
from pandas_ods_reader import read_ods 
import re
import csv
from natsort import index_natsorted
import random
import markdown

df = pd.read_csv("../spreadsheets/dps-test.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# adding feedback
# df.reset_index(drop=True, inplace=True)
df['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df['Pāli1'] + """&entry.644913945=Anki Deck Vocab Beginner Pāli Course">Fix it here</a>."""

df_anki = df.drop(['class', 'count'], axis=1)

df_anki.to_csv("../csv-for-anki/dps-feedback.csv", sep="\t", index=None)

# change Meaning in native language
test2 = df['Pāli1'] != ""
filter = test2
df.loc[filter, ['Meaning in native language']] = ""

# sort by
df.sort_values(by='Example3', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df['Example3'])))

# filter 0 classes words
test2 = df['ex'] == "-"
filter = test2
df_0 = df.loc[filter]

# filter 1 classes words
test2 = df['ex'] == "1"
filter = test2
df_1 = df.loc[filter]

# filter 2
test2 = df['class'] == "2"
filter = test2
df_2_cl = df.loc[filter]

test2 = df['ex'] == "2"
filter = test2
df_2 = df.loc[filter]

df_comb_2 = pd.concat([df_0, df_1, df_2])

# keep only unique 2
logix = df_2_cl['Pāli1'].isin(df_comb_2['Pāli1'])
df_2_cl_u = df_2_cl.drop(df_2_cl[logix].index)

df_comb_2_f = pd.concat([df_comb_2, df_2_cl_u])

# print("2 done")

# filter 3
test3 = df['class'] == "3"
filter = test3
df_3_cl = df.loc[filter]
df_3_cl_comb = pd.concat([df_2_cl, df_3_cl])

test3 = df['ex'] == "3"
filter = test3
df_3 = df.loc[filter]

df_comb_3 = pd.concat([df_0, df_1, df_2, df_3])

# keep only unique 3
logix = df_3_cl_comb['Pāli1'].isin(df_comb_3['Pāli1'])
df_3_cl_u = df_3_cl_comb.drop(df_3_cl_comb[logix].index)

df_comb_3_f = pd.concat([df_comb_3, df_3_cl_u])

# print("3 done")

# filter 4
test4 = df['class'] == "4"
filter = test4
df_4_cl = df.loc[filter]
df_4_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl])

test4 = df['ex'] == "4"
filter = test4
df_4 = df.loc[filter]

df_comb_4 = pd.concat([df_0, df_1, df_2, df_3, df_4])

# keep only unique 4
logix = df_4_cl_comb['Pāli1'].isin(df_comb_4['Pāli1'])
df_4_cl_u = df_4_cl_comb.drop(df_4_cl_comb[logix].index)

df_comb_4_f = pd.concat([df_comb_4, df_4_cl_u])

# print("4 done")

# filter 5
test5 = df['class'] == "5"
filter = test5
df_5_cl = df.loc[filter]
df_5_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl])

test5 = df['ex'] == "5"
filter = test5
df_5 = df.loc[filter]

df_comb_5 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5])

# keep only unique 5
logix = df_5_cl_comb['Pāli1'].isin(df_comb_5['Pāli1'])
df_5_cl_u = df_5_cl_comb.drop(df_5_cl_comb[logix].index)

df_comb_5_f = pd.concat([df_comb_5, df_5_cl_u])

# print("5 done")

# filter 6
test6 = df['class'] == "6"
filter = test6
df_6_cl = df.loc[filter]
df_6_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl])

test6 = df['ex'] == "6"
filter = test6
df_6 = df.loc[filter]

df_comb_6 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6])

# keep only unique 6
logix = df_6_cl_comb['Pāli1'].isin(df_comb_6['Pāli1'])
df_6_cl_u = df_6_cl_comb.drop(df_6_cl_comb[logix].index)

df_comb_6_f = pd.concat([df_comb_6, df_6_cl_u])

# print("6 done")

# filter 7
test7 = df['class'] == "7"
filter = test7
df_7_cl = df.loc[filter]
df_7_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl])

test7 = df['ex'] == "7"
filter = test7
df_7 = df.loc[filter]

df_comb_7 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7])

# keep only unique 7
logix = df_7_cl_comb['Pāli1'].isin(df_comb_7['Pāli1'])
df_7_cl_u = df_7_cl_comb.drop(df_7_cl_comb[logix].index)

df_comb_7_f = pd.concat([df_comb_7, df_7_cl_u])

# print("7 done")

# filter 8
test8 = df['class'] == "8"
filter = test8
df_8_cl = df.loc[filter]
df_8_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl])

test8 = df['ex'] == "8"
filter = test8
df_8 = df.loc[filter]

df_comb_8 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8])

# keep only unique 8
logix = df_8_cl_comb['Pāli1'].isin(df_comb_8['Pāli1'])
df_8_cl_u = df_8_cl_comb.drop(df_8_cl_comb[logix].index)

df_comb_8_f = pd.concat([df_comb_8, df_8_cl_u])

# print("8 done")

# filter 9
test9 = df['class'] == "9"
filter = test9
df_9_cl = df.loc[filter]
df_9_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl])

test9 = df['ex'] == "9"
filter = test9
df_9 = df.loc[filter]

df_comb_9 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9])

# keep only unique 9
logix = df_9_cl_comb['Pāli1'].isin(df_comb_9['Pāli1'])
df_9_cl_u = df_9_cl_comb.drop(df_9_cl_comb[logix].index)

df_comb_9_f = pd.concat([df_comb_9, df_9_cl_u])

# print("9 done")

# filter 10
test10 = df['class'] == "10"
filter = test10
df_10_cl = df.loc[filter]
df_10_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl])

test10 = df['ex'] == "10"
filter = test10
df_10 = df.loc[filter]

df_comb_10 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10])

# keep only unique 10
logix = df_10_cl_comb['Pāli1'].isin(df_comb_10['Pāli1'])
df_10_cl_u = df_10_cl_comb.drop(df_10_cl_comb[logix].index)

df_comb_10_f = pd.concat([df_comb_10, df_10_cl_u])

# print("10 done")

# filter 11
test11 = df['class'] == "11"
filter = test11
df_11_cl = df.loc[filter]
df_11_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl])

test11 = df['ex'] == "11"
filter = test11
df_11 = df.loc[filter]

df_comb_11 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11])

# keep only unique 11
logix = df_11_cl_comb['Pāli1'].isin(df_comb_11['Pāli1'])
df_11_cl_u = df_11_cl_comb.drop(df_11_cl_comb[logix].index)

df_comb_11_f = pd.concat([df_comb_11, df_11_cl_u])

# print("11 done")

# filter 12
test12 = df['class'] == "12"
filter = test12
df_12_cl = df.loc[filter]
df_12_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl])

test12 = df['ex'] == "12"
filter = test12
df_12 = df.loc[filter]

df_comb_12 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12])

# keep only unique 12
logix = df_12_cl_comb['Pāli1'].isin(df_comb_12['Pāli1'])
df_12_cl_u = df_12_cl_comb.drop(df_12_cl_comb[logix].index)

df_comb_12_f = pd.concat([df_comb_12, df_12_cl_u])

# print("12 done")

# filter 13
test13 = df['class'] == "13"
filter = test13
df_13_cl = df.loc[filter]
df_13_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl])

test13 = df['ex'] == "13"
filter = test13
df_13 = df.loc[filter]

df_comb_13 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13])

# keep only unique 13
logix = df_13_cl_comb['Pāli1'].isin(df_comb_13['Pāli1'])
df_13_cl_u = df_13_cl_comb.drop(df_13_cl_comb[logix].index)

df_comb_13_f = pd.concat([df_comb_13, df_13_cl_u])

# print("13 done")

# filter 14
test14 = df['class'] == "14"
filter = test14
df_14_cl = df.loc[filter]
df_14_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl])

test14 = df['ex'] == "14"
filter = test14
df_14 = df.loc[filter]

df_comb_14 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14])

# keep only unique 14
logix = df_14_cl_comb['Pāli1'].isin(df_comb_14['Pāli1'])
df_14_cl_u = df_14_cl_comb.drop(df_14_cl_comb[logix].index)

df_comb_14_f = pd.concat([df_comb_14, df_14_cl_u])

# print("14 done")

# save classes csv
df_1.to_csv("csv-for-examples/1-class.csv", sep="\t", index=None)
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
df_comb_14_f.to_csv("csv-for-examples/14-class.csv", sep="\t", index=None)

print("csv-for-examples saved")


# change Test
# test2 = df['Pāli1'] != ""
# filter = test2
# df.loc[filter, ['Test']] = ""

# replace all Pattern with '_'
df['Pattern'] = df['Pattern'].str.replace(' ', '-')

# change Pattern of ind
test2 = df['Pattern'] == ""
filter = test2
df.loc[filter, ['Pattern']] = df['POS']

# df = df[['Pāli1', 'POS', 'Grammar', 'Derived from', 'Neg', 'Verb', 'Trans', 'Case', 'Meaning IN CONTEXT', 'Meaning in native language', 'Pāli Root', 'Base', 'Construction', 'Sanskrit', 'Sk Root', 'Variant', 'Commentary', 'Notes', 'Source1', 'Sutta1', 'Example1', 'Source2', 'Sutta2', 'Example2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Source3', 'Sutta3', 'Example3', 'Pali chant 3', 'English chant 3', 'Chapter 3', 'Pattern', 'Test', 'ex', 'count',  'audio','Feedback']]

df.sort_values(by='Example3', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df['Example3'])))

# replace ṁ
# df['Pāli1'] = df['Pāli1'].str.replace('ṃ', 'ṁ')
# df['Derived from'] = df['Derived from'].str.replace('ṃ', 'ṁ')
# df['Meaning IN CONTEXT'] = df['Meaning IN CONTEXT'].str.replace('ṃ', 'ṁ')
# df['Pāli Root'] = df['Pāli Root'].str.replace('ṃ', 'ṁ')
# df['Base'] = df['Base'].str.replace('ṃ', 'ṁ')
# df['Construction'] = df['Construction'].str.replace('ṃ', 'ṁ')
# df['Sanskrit'] = df['Sanskrit'].str.replace('ṃ', 'ṁ')
# df['Sk Root'] = df['Sk Root'].str.replace('ṃ', 'ṁ')
# df['Variant'] = df['Variant'].str.replace('ṃ', 'ṁ')
# df['Commentary'] = df['Commentary'].str.replace('ṃ', 'ṁ')
# df['Notes'] = df['Notes'].str.replace('ṃ', 'ṁ')
# df['Sutta2'] = df['Sutta2'].str.replace('ṃ', 'ṁ')
# df['Example2'] = df['Example2'].str.replace('ṃ', 'ṁ')
# df['Sutta3'] = df['Sutta3'].str.replace('ṃ', 'ṁ')
# df['Example3'] = df['Example3'].str.replace('ṃ', 'ṁ')
# df['Pali chant 3'] = df['Pali chant 3'].str.replace('ṃ', 'ṁ')
# df['Sutta 4'] = df['Sutta 4'].str.replace('ṃ', 'ṁ')
# df['Example 4'] = df['Example 4'].str.replace('ṃ', 'ṁ')
# df['Pali chant 4'] = df['Pali chant 4'].str.replace('ṃ', 'ṁ')
# df['Pattern'] = df['Pattern'].str.replace('ṃ', 'ṁ')

# filter all classes words
# test15 = df['ex'] != ""
# filter = test15
# df_all = df.loc[filter]

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

df_all = df.loc[df['ex'].isin(options)] 

df_all = df_all.drop(['count', 'class'], axis=1)

df_all.to_csv("../csv-for-anki/classes/all-class.csv", sep="\t", index=None)

# make words for class 2

options = ['1', '2']

df_words_cl2 = df.loc[df['class'].isin(options) & df['ex'].isin(options)] 

# df_words_cl2 = df.loc[(df['class'] < 3) & (df['ex'] < 3)]

df_words_cl2 = df_words_cl2[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl2 = df_words_cl2.sort_values(by=['class', 'Pattern'])

# df_words_cl2.to_csv("vocab/vocab-class2.csv", sep="\t", index=None)
df_words_cl2.to_excel("vocab/vocab-class2.xlsx", index=None)

# make words for class 3

options = ['1', '2', '3']

df_words_cl3 = df.loc[df['class'].isin(options) & df['ex'].isin(options)] 

df_words_cl3 = df_words_cl3[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl3 = df_words_cl3.sort_values(by=['class', 'Pattern'])

# df_words_cl3.to_csv("vocab/vocab-class3.csv", sep="\t", index=None)
df_words_cl3.to_excel("vocab/vocab-class3.xlsx", index=None)

# make words for class 4

options = ['1', '2', '3', '4']

df_words_cl4 = df.loc[df['class'].isin(options) & df['ex'].isin(options)] 

df_words_cl4 = df_words_cl4[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl4 = df_words_cl4.sort_values(by=['class', 'Pattern'])

# df_words_cl4.to_csv("vocab/vocab-class4.csv", sep="\t", index=None)
df_words_cl4.to_excel("vocab/vocab-class4.xlsx", index=None)

# make words for class 5

options = ['1', '2', '3', '4', '5']

df_words_cl5 = df.loc[df['class'].isin(options) & df['ex'].isin(options)] 

df_words_cl5 = df_words_cl5[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl5 = df_words_cl5.sort_values(by=['class', 'Pattern'])

# df_words_cl5.to_csv("vocab/vocab-class5.csv", sep="\t", index=None)
df_words_cl5.to_excel("vocab/vocab-class5.xlsx", index=None)

# make words for class 6

options = ['1', '2', '3', '4', '5', '6']

df_words_cl6 = df.loc[df['class'].isin(options) & df['ex'].isin(options)] 

df_words_cl6 = df_words_cl6[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl6 = df_words_cl6.sort_values(by=['class', 'Pattern'])

# df_words_cl6.to_csv("vocab/vocab-class6.csv", sep="\t", index=None)
df_words_cl6.to_excel("vocab/vocab-class6.xlsx", index=None)

# make words for class 7

options = ['1', '2', '3', '4', '5', '6', '7']

df_words_cl7 = df.loc[df['class'].isin(options) & df['ex'].isin(options)] 

df_words_cl7 = df_words_cl7[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl7 = df_words_cl7.sort_values(by=['class', 'Pattern'])

# df_words_cl7.to_csv("vocab/vocab-class7.csv", sep="\t", index=None)
df_words_cl7.to_excel("vocab/vocab-class7.xlsx", index=None)

# make words for class 8

options = ['1', '2', '3', '4', '5', '6', '7', '8']

df_words_cl8 = df.loc[df['class'].isin(options) & df['ex'].isin(options)] 

df_words_cl8 = df_words_cl8[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl8 = df_words_cl8.sort_values(by=['class', 'Pattern'])

# df_words_cl8.to_csv("vocab/vocab-class8.csv", sep="\t", index=None)
df_words_cl8.to_excel("vocab/vocab-class8.xlsx", index=None)

# make words for class 9

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

df_words_cl9 = df.loc[df['class'].isin(options) & df['ex'].isin(options)] 

df_words_cl9 = df_words_cl9[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl9 = df_words_cl9.sort_values(by=['class', 'Pattern'])

# df_words_cl9.to_csv("vocab/vocab-class9.csv", sep="\t", index=None)
df_words_cl9.to_excel("vocab/vocab-class9.xlsx", index=None)

# make words for class 10

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

df_words_cl10 = df.loc[df['class'].isin(options) & df['ex'].isin(options)] 

df_words_cl10 = df_words_cl10[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl10 = df_words_cl10.sort_values(by=['class', 'Pattern'])

# df_words_cl10.to_csv("vocab/vocab-class10.csv", sep="\t", index=None)
df_words_cl10.to_excel("vocab/vocab-class10.xlsx", index=None)

# make words for class 11

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

df_words_cl11 = df.loc[df['class'].isin(options) & df['ex'].isin(options)] 

df_words_cl11 = df_words_cl11[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl11 = df_words_cl11.sort_values(by=['class', 'Pattern'])

# df_words_cl11.to_csv("vocab/vocab-class11.csv", sep="\t", index=None)
df_words_cl11.to_excel("vocab/vocab-class11.xlsx", index=None)

# make words for class 12

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

df_words_cl12 = df.loc[df['class'].isin(options) & df['ex'].isin(options)] 

df_words_cl12 = df_words_cl12[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl12 = df_words_cl12.sort_values(by=['class', 'Pattern'])

# df_words_cl12.to_csv("vocab/vocab-class12.csv", sep="\t", index=None)
df_words_cl12.to_excel("vocab/vocab-class12.xlsx", index=None)

# make words for class 13

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

df_words_cl13 = df.loc[df['class'].isin(options) & df['ex'].isin(options)] 

df_words_cl13 = df_words_cl13[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl13 = df_words_cl13.sort_values(by=['class', 'Pattern'])

# df_words_cl13.to_csv("vocab/vocab-class13.csv", sep="\t", index=None)
df_words_cl13.to_excel("vocab/vocab-class13.xlsx", index=None)

# make words for class 14

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

df_words_cl14 = df.loc[df['class'].isin(options) & df['ex'].isin(options)] 

df_words_cl14 = df_words_cl14[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl14 = df_words_cl14.sort_values(by=['class', 'Pattern'])

# df_words_cl14.to_csv("vocab/vocab-class14.csv", sep="\t", index=None)
df_words_cl14.to_excel("vocab/vocab-class14.xlsx", index=None)




# make words for pict class 2

options = ['1', '2']

cl = ['2']

df_words_cl2 = df.loc[df['class'].isin(options) & df['ex'].isin(cl)] 

df_words_cl2 = df_words_cl2[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl2 = df_words_cl2.sort_values(by=['class', 'Pattern'])

df_words_cl2.to_csv("csv-for-pic/class2.csv", sep="\t", index=None)

# make words for pict class 3

options = ['1', '2', '3']

cl = ['3']

df_words_cl3 = df.loc[df['class'].isin(options) & df['ex'].isin(cl)] 

df_words_cl3 = df_words_cl3[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl3 = df_words_cl3.sort_values(by=['class', 'Pattern'])

df_words_cl3.to_csv("csv-for-pic/class3.csv", sep="\t", index=None)

# make words for pict class 4

options = ['1', '2', '3', '4']

cl = ['4']

df_words_cl4 = df.loc[df['class'].isin(options) & df['ex'].isin(cl)] 

df_words_cl4 = df_words_cl4[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl4 = df_words_cl4.sort_values(by=['class', 'Pattern'])

df_words_cl4.to_csv("csv-for-pic/class4.csv", sep="\t", index=None)

# make words for pict class 5

options = ['1', '2', '3', '4', '5']

cl = ['5']

df_words_cl5 = df.loc[df['class'].isin(options) & df['ex'].isin(cl)] 

df_words_cl5 = df_words_cl5[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl5 = df_words_cl5.sort_values(by=['class', 'Pattern'])

df_words_cl5.to_csv("csv-for-pic/class5.csv", sep="\t", index=None)

# make words for pict class 6

options = ['1', '2', '3', '4', '5', '6']

cl = ['6']

df_words_cl6 = df.loc[df['class'].isin(options) & df['ex'].isin(cl)] 

df_words_cl6 = df_words_cl6[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl6 = df_words_cl6.sort_values(by=['class', 'Pattern'])

df_words_cl6.to_csv("csv-for-pic/class6.csv", sep="\t", index=None)

# make words for pict class 7

options = ['1', '2', '3', '4', '5', '6', '7']

cl = ['7']

df_words_cl7 = df.loc[df['class'].isin(options) & df['ex'].isin(cl)] 

df_words_cl7 = df_words_cl7[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl7 = df_words_cl7.sort_values(by=['class', 'Pattern'])

df_words_cl7.to_csv("csv-for-pic/class7.csv", sep="\t", index=None)

# make words for pict class 8

options = ['1', '2', '3', '4', '5', '6', '7', '8']

cl = ['8']

df_words_cl8 = df.loc[df['class'].isin(options) & df['ex'].isin(cl)] 

df_words_cl8 = df_words_cl8[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl8 = df_words_cl8.sort_values(by=['class', 'Pattern'])

df_words_cl8.to_csv("csv-for-pic/class8.csv", sep="\t", index=None)

# make words for pict class 9

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

cl = ['9']

df_words_cl9 = df.loc[df['class'].isin(options) & df['ex'].isin(cl)] 

df_words_cl9 = df_words_cl9[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl9 = df_words_cl9.sort_values(by=['class', 'Pattern'])

df_words_cl9.to_csv("csv-for-pic/class9.csv", sep="\t", index=None)

# make words for pict class 10

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

cl = ['10']

df_words_cl10 = df.loc[df['class'].isin(options) & df['ex'].isin(cl)] 

df_words_cl10 = df_words_cl10[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl10 = df_words_cl10.sort_values(by=['class', 'Pattern'])

df_words_cl10.to_csv("csv-for-pic/class10.csv", sep="\t", index=None)

# make words for pict class 11

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

cl = ['11']

df_words_cl11 = df.loc[df['class'].isin(options) & df['ex'].isin(cl)] 

df_words_cl11 = df_words_cl11[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl11 = df_words_cl11.sort_values(by=['class', 'Pattern'])

df_words_cl11.to_csv("csv-for-pic/class11.csv", sep="\t", index=None)

# make words for pict class 12

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

cl = ['12']

df_words_cl12 = df.loc[df['class'].isin(options) & df['ex'].isin(cl)] 

df_words_cl12 = df_words_cl12[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl12 = df_words_cl12.sort_values(by=['class', 'Pattern'])

df_words_cl12.to_csv("csv-for-pic/class12.csv", sep="\t", index=None)

# make words for pict class 13

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

cl = ['13']

df_words_cl13 = df.loc[df['class'].isin(options) & df['ex'].isin(cl)] 

df_words_cl13 = df_words_cl13[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl13 = df_words_cl13.sort_values(by=['class', 'Pattern'])

df_words_cl13.to_csv("csv-for-pic/class13.csv", sep="\t", index=None)

# make words for pict class 14

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

cl = ['14']

df_words_cl14 = df.loc[df['class'].isin(options) & df['ex'].isin(cl)] 

df_words_cl14 = df_words_cl14[['Pāli1', 'POS', 'Meaning IN CONTEXT', 'Pattern', 'class']]

df_words_cl14 = df_words_cl14.sort_values(by=['class', 'Pattern'])

df_words_cl14.to_csv("csv-for-pic/class14.csv", sep="\t", index=None)



# remove column count from df

df.sort_values(by='Example3', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df['Example3'])))

df = df.drop(['count', 'class'], axis=1)

# filter 0 classes words
test2 = df['ex'] == "-"
filter = test2
df_0 = df.loc[filter]

# filter 1 classes words
test2 = df['ex'] == "1"
filter = test2
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

# filter 14 classes words
test14 = df['ex'] == "14"
filter = test14
df_14 = df.loc[filter]

# save classes csv

# df_0.to_csv("../csv-for-anki/classes/0-class-anki.csv", sep="\t", index=None)
# df_1 = df_1.drop(['Feedback'], axis=1)
# df_1['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&amp;entry.644913945=Anki Deck Vocab Beginner Pāli Course">Fix it here</a>."""
df_1.to_csv("../csv-for-anki/classes/1-class-anki.csv", sep="\t", index=None)
df_1.to_csv("csv-for-pic/class1.csv", sep="\t", index=None)
df_2.to_csv("../csv-for-anki/classes/2-class-anki.csv", sep="\t", index=None)
df_3.to_csv("../csv-for-anki/classes/3-class-anki.csv", sep="\t", index=None)
df_4.to_csv("../csv-for-anki/classes/4-class-anki.csv", sep="\t", index=None)
df_5.to_csv("../csv-for-anki/classes/5-class-anki.csv", sep="\t", index=None)
df_6.to_csv("../csv-for-anki/classes/6-class-anki.csv", sep="\t", index=None)
df_7.to_csv("../csv-for-anki/classes/7-class-anki.csv", sep="\t", index=None)
df_8.to_csv("../csv-for-anki/classes/8-class-anki.csv", sep="\t", index=None)
df_9.to_csv("../csv-for-anki/classes/9-class-anki.csv", sep="\t", index=None)
df_10.to_csv("../csv-for-anki/classes/10-class-anki.csv", sep="\t", index=None)
df_11.to_csv("../csv-for-anki/classes/11-class-anki.csv", sep="\t", index=None)
df_12.to_csv("../csv-for-anki/classes/12-class-anki.csv", sep="\t", index=None)
df_13.to_csv("../csv-for-anki/classes/13-class-anki.csv", sep="\t", index=None)
df_14.to_csv("../csv-for-anki/classes/14-class-anki.csv", sep="\t", index=None)

# combine classes
# df_comb = pd.concat([df_1, df_2])
# df_comb = pd.concat([df_1, df_2 df_3])
# df_comb = pd.concat([df_1, df_2 df_3, df_4])
# df_comb = pd.concat([df_1, df_2 df_3, df_4, df_5])
# df_comb = pd.concat([df_1, df_2 df_3, df_4, df_5, df_6])
# df_comb = pd.concat([df_1, df_2 df_3, df_4, df_5, df_6, df_7])
# df_comb = pd.concat([df_1, df_2 df_3, df_4, df_5, df_6, df_7, df_8])
# df_comb = pd.concat([df_1, df_2 df_3, df_4, df_5, df_6, df_7, df_8, df_9])
# df_comb = pd.concat([df_1, df_2 df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10])
# df_comb = pd.concat([df_1, df_2 df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11])
# df_comb = pd.concat([df_1, df_2 df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11 df_12])
# df_comb = pd.concat([df_1, df_2 df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11 df_12, df_13])
# df_comb = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14])

# df_comb.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_comb['count'])))

# df_comb.to_csv("csv-for-anki/all-class.csv", sep="\t", index=None)