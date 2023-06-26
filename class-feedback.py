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
df['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df['pali_1'] + """&entry.644913945=Anki Deck Vocab Pāli Course">Fix it here</a>."""

df_anki = df.drop(['sbs_category', 'sbs_class', 'count', 'sbs_source_5', 'sbs_sutta_5', 'sbs_example_5', 'move', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_notes', 'ru_notes'], axis=1)
# print("columns 'sbs_category' 'sbs_class', 'count', 'sbs_source_5', 'sbs_sutta_5', 'sbs_example_5', 'move', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_notes', 'ru_notes' has been dropped for anki")

df_anki.to_csv("../csv-for-anki/dps-feedback.csv", sep="\t", index=None)

# change ru_meaning
test2 = df['pali_1'] != ""
filter = test2
df.loc[filter, ['ru_meaning']] = ""

# sort by
df.sort_values(by='sbs_example_3', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df['sbs_example_3'])))

# filter 0 classes words
test2 = df['sbs_class_anki'] == "-"
filter = test2
df_0 = df.loc[filter]

# filter 1 classes words
test2 = df['sbs_class_anki'] == "1"
filter = test2
df_1 = df.loc[filter]

# filter 2
test2 = df['sbs_class'] == "2"
filter = test2
df_2_cl = df.loc[filter]

test2 = df['sbs_class_anki'] == "2"
filter = test2
df_2 = df.loc[filter]

df_comb_2 = pd.concat([df_0, df_1, df_2])

# keep only unique 2
logix = df_2_cl['pali_1'].isin(df_comb_2['pali_1'])
df_2_cl_u = df_2_cl.drop(df_2_cl[logix].index)

df_comb_2_f = pd.concat([df_comb_2, df_2_cl_u])

# print("2 done")

# filter 3
test3 = df['sbs_class'] == "3"
filter = test3
df_3_cl = df.loc[filter]
df_3_cl_comb = pd.concat([df_2_cl, df_3_cl])

test3 = df['sbs_class_anki'] == "3"
filter = test3
df_3 = df.loc[filter]

df_comb_3 = pd.concat([df_0, df_1, df_2, df_3])

# keep only unique 3
logix = df_3_cl_comb['pali_1'].isin(df_comb_3['pali_1'])
df_3_cl_u = df_3_cl_comb.drop(df_3_cl_comb[logix].index)

df_comb_3_f = pd.concat([df_comb_3, df_3_cl_u])

# print("3 done")

# filter 4
test4 = df['sbs_class'] == "4"
filter = test4
df_4_cl = df.loc[filter]
df_4_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl])

test4 = df['sbs_class_anki'] == "4"
filter = test4
df_4 = df.loc[filter]

df_comb_4 = pd.concat([df_0, df_1, df_2, df_3, df_4])

# keep only unique 4
logix = df_4_cl_comb['pali_1'].isin(df_comb_4['pali_1'])
df_4_cl_u = df_4_cl_comb.drop(df_4_cl_comb[logix].index)

df_comb_4_f = pd.concat([df_comb_4, df_4_cl_u])

# print("4 done")

# filter 5
test5 = df['sbs_class'] == "5"
filter = test5
df_5_cl = df.loc[filter]
df_5_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl])

test5 = df['sbs_class_anki'] == "5"
filter = test5
df_5 = df.loc[filter]

df_comb_5 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5])

# keep only unique 5
logix = df_5_cl_comb['pali_1'].isin(df_comb_5['pali_1'])
df_5_cl_u = df_5_cl_comb.drop(df_5_cl_comb[logix].index)

df_comb_5_f = pd.concat([df_comb_5, df_5_cl_u])

# print("5 done")

# filter 6
test6 = df['sbs_class'] == "6"
filter = test6
df_6_cl = df.loc[filter]
df_6_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl])

test6 = df['sbs_class_anki'] == "6"
filter = test6
df_6 = df.loc[filter]

df_comb_6 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6])

# keep only unique 6
logix = df_6_cl_comb['pali_1'].isin(df_comb_6['pali_1'])
df_6_cl_u = df_6_cl_comb.drop(df_6_cl_comb[logix].index)

df_comb_6_f = pd.concat([df_comb_6, df_6_cl_u])

# print("6 done")

# filter 7
test7 = df['sbs_class'] == "7"
filter = test7
df_7_cl = df.loc[filter]
df_7_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl])

test7 = df['sbs_class_anki'] == "7"
filter = test7
df_7 = df.loc[filter]

df_comb_7 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7])

# keep only unique 7
logix = df_7_cl_comb['pali_1'].isin(df_comb_7['pali_1'])
df_7_cl_u = df_7_cl_comb.drop(df_7_cl_comb[logix].index)

df_comb_7_f = pd.concat([df_comb_7, df_7_cl_u])

# print("7 done")

# filter 8
test8 = df['sbs_class'] == "8"
filter = test8
df_8_cl = df.loc[filter]
df_8_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl])

test8 = df['sbs_class_anki'] == "8"
filter = test8
df_8 = df.loc[filter]

df_comb_8 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8])

# keep only unique 8
logix = df_8_cl_comb['pali_1'].isin(df_comb_8['pali_1'])
df_8_cl_u = df_8_cl_comb.drop(df_8_cl_comb[logix].index)

df_comb_8_f = pd.concat([df_comb_8, df_8_cl_u])

# print("8 done")

# filter 9
test9 = df['sbs_class'] == "9"
filter = test9
df_9_cl = df.loc[filter]
df_9_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl])

test9 = df['sbs_class_anki'] == "9"
filter = test9
df_9 = df.loc[filter]

df_comb_9 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9])

# keep only unique 9
logix = df_9_cl_comb['pali_1'].isin(df_comb_9['pali_1'])
df_9_cl_u = df_9_cl_comb.drop(df_9_cl_comb[logix].index)

df_comb_9_f = pd.concat([df_comb_9, df_9_cl_u])

# print("9 done")

# filter 10
test10 = df['sbs_class'] == "10"
filter = test10
df_10_cl = df.loc[filter]
df_10_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl])

test10 = df['sbs_class_anki'] == "10"
filter = test10
df_10 = df.loc[filter]

df_comb_10 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10])

# keep only unique 10
logix = df_10_cl_comb['pali_1'].isin(df_comb_10['pali_1'])
df_10_cl_u = df_10_cl_comb.drop(df_10_cl_comb[logix].index)

df_comb_10_f = pd.concat([df_comb_10, df_10_cl_u])

# print("10 done")

# filter 11
test11 = df['sbs_class'] == "11"
filter = test11
df_11_cl = df.loc[filter]
df_11_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl])

test11 = df['sbs_class_anki'] == "11"
filter = test11
df_11 = df.loc[filter]

df_comb_11 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11])

# keep only unique 11
logix = df_11_cl_comb['pali_1'].isin(df_comb_11['pali_1'])
df_11_cl_u = df_11_cl_comb.drop(df_11_cl_comb[logix].index)

df_comb_11_f = pd.concat([df_comb_11, df_11_cl_u])

# print("11 done")

# filter 12
test12 = df['sbs_class'] == "12"
filter = test12
df_12_cl = df.loc[filter]
df_12_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl])

test12 = df['sbs_class_anki'] == "12"
filter = test12
df_12 = df.loc[filter]

df_comb_12 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12])

# keep only unique 12
logix = df_12_cl_comb['pali_1'].isin(df_comb_12['pali_1'])
df_12_cl_u = df_12_cl_comb.drop(df_12_cl_comb[logix].index)

df_comb_12_f = pd.concat([df_comb_12, df_12_cl_u])

# print("12 done")

# filter 13
test13 = df['sbs_class'] == "13"
filter = test13
df_13_cl = df.loc[filter]
df_13_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl])

test13 = df['sbs_class_anki'] == "13"
filter = test13
df_13 = df.loc[filter]

df_comb_13 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13])

# keep only unique 13
logix = df_13_cl_comb['pali_1'].isin(df_comb_13['pali_1'])
df_13_cl_u = df_13_cl_comb.drop(df_13_cl_comb[logix].index)

df_comb_13_f = pd.concat([df_comb_13, df_13_cl_u])

# print("13 done")

# filter 14
test14 = df['sbs_class'] == "14"
filter = test14
df_14_cl = df.loc[filter]
df_14_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl])

test14 = df['sbs_class_anki'] == "14"
filter = test14
df_14 = df.loc[filter]

df_comb_14 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14])

# keep only unique 14
logix = df_14_cl_comb['pali_1'].isin(df_comb_14['pali_1'])
df_14_cl_u = df_14_cl_comb.drop(df_14_cl_comb[logix].index)

df_comb_14_f = pd.concat([df_comb_14, df_14_cl_u])

# print("14 done")

# filter 15
test15 = df['sbs_class'] == "15"
filter = test15
df_15_cl = df.loc[filter]
df_15_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl, df_15_cl])

test15 = df['sbs_class_anki'] == "15"
filter = test15
df_15 = df.loc[filter]

df_comb_15 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15])

# keep only unique 15
logix = df_15_cl_comb['pali_1'].isin(df_comb_15['pali_1'])
df_15_cl_u = df_15_cl_comb.drop(df_15_cl_comb[logix].index)

df_comb_15_f = pd.concat([df_comb_15, df_15_cl_u])

# print("15 done")

# filter 16
test16 = df['sbs_class'] == "16"
filter = test16
df_16_cl = df.loc[filter]
df_16_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl, df_15_cl, df_16_cl])

test16 = df['sbs_class_anki'] == "16"
filter = test16
df_16 = df.loc[filter]

df_comb_16 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16])

# keep only unique 16
logix = df_16_cl_comb['pali_1'].isin(df_comb_16['pali_1'])
df_16_cl_u = df_16_cl_comb.drop(df_16_cl_comb[logix].index)

df_comb_16_f = pd.concat([df_comb_16, df_16_cl_u])

# print("16 done")

# filter 17
test17 = df['sbs_class'] == "17"
filter = test17
df_17_cl = df.loc[filter]
df_17_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl, df_15_cl, df_16_cl, df_17_cl])

test17 = df['sbs_class_anki'] == "17"
filter = test17
df_17 = df.loc[filter]

df_comb_17 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17])

# keep only unique 17
logix = df_17_cl_comb['pali_1'].isin(df_comb_17['pali_1'])
df_17_cl_u = df_17_cl_comb.drop(df_17_cl_comb[logix].index)

df_comb_17_f = pd.concat([df_comb_17, df_17_cl_u])

# print("17 done")

# filter 18
test18 = df['sbs_class'] == "18"
filter = test18
df_18_cl = df.loc[filter]
df_18_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl, df_15_cl, df_16_cl, df_17_cl, df_18_cl])

test18 = df['sbs_class_anki'] == "18"
filter = test18
df_18 = df.loc[filter]

df_comb_18 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17, df_18])

# keep only unique 18
logix = df_18_cl_comb['pali_1'].isin(df_comb_18['pali_1'])
df_18_cl_u = df_18_cl_comb.drop(df_18_cl_comb[logix].index)

df_comb_18_f = pd.concat([df_comb_18, df_18_cl_u])

# print("18 done")

# filter 19
test19 = df['sbs_class'] == "19"
filter = test19
df_19_cl = df.loc[filter]
df_19_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl, df_15_cl, df_16_cl, df_17_cl, df_18_cl, df_19_cl])

test19 = df['sbs_class_anki'] == "19"
filter = test19
df_19 = df.loc[filter]

df_comb_19 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17, df_18, df_19])

# keep only unique 19
logix = df_19_cl_comb['pali_1'].isin(df_comb_19['pali_1'])
df_19_cl_u = df_19_cl_comb.drop(df_19_cl_comb[logix].index)

df_comb_19_f = pd.concat([df_comb_19, df_19_cl_u])

# print("19 done")

# filter 20
test20 = df['sbs_class'] == "20"
filter = test20
df_20_cl = df.loc[filter]
df_20_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl, df_15_cl, df_16_cl, df_17_cl, df_18_cl, df_19_cl, df_20_cl])

test20 = df['sbs_class_anki'] == "20"
filter = test20
df_20 = df.loc[filter]

df_comb_20 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17, df_18, df_19, df_20])

# keep only unique 20
logix = df_20_cl_comb['pali_1'].isin(df_comb_20['pali_1'])
df_20_cl_u = df_20_cl_comb.drop(df_20_cl_comb[logix].index)

df_comb_20_f = pd.concat([df_comb_20, df_20_cl_u])

# print("20 done")

# filter 21
test21 = df['sbs_class'] == "21"
filter = test21
df_21_cl = df.loc[filter]
df_21_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl, df_15_cl, df_16_cl, df_17_cl, df_18_cl, df_19_cl, df_20_cl, df_21_cl])

test21 = df['sbs_class_anki'] == "21"
filter = test21
df_21 = df.loc[filter]

df_comb_21 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17, df_18, df_19, df_20, df_21])

# keep only unique 21
logix = df_21_cl_comb['pali_1'].isin(df_comb_21['pali_1'])
df_21_cl_u = df_21_cl_comb.drop(df_21_cl_comb[logix].index)

df_comb_21_f = pd.concat([df_comb_21, df_21_cl_u])

# print("21 done")

# filter 22
test22 = df['sbs_class'] == "22"
filter = test22
df_22_cl = df.loc[filter]
df_22_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl, df_15_cl, df_16_cl, df_17_cl, df_18_cl, df_19_cl, df_20_cl, df_21_cl, df_22_cl])

test22 = df['sbs_class_anki'] == "22"
filter = test22
df_22 = df.loc[filter]

df_comb_22 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17, df_18, df_19, df_20, df_21, df_22])

# keep only unique 22
logix = df_22_cl_comb['pali_1'].isin(df_comb_22['pali_1'])
df_22_cl_u = df_22_cl_comb.drop(df_22_cl_comb[logix].index)

df_comb_22_f = pd.concat([df_comb_22, df_22_cl_u])

# print("22 done")

# filter 23
test23 = df['sbs_class'] == "23"
filter = test23
df_23_cl = df.loc[filter]
df_23_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl, df_15_cl, df_16_cl, df_17_cl, df_18_cl, df_19_cl, df_20_cl, df_21_cl, df_22_cl, df_23_cl])

test23 = df['sbs_class_anki'] == "23"
filter = test23
df_23 = df.loc[filter]

df_comb_23 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17, df_18, df_19, df_20, df_21, df_22, df_23])

# keep only unique 23
logix = df_23_cl_comb['pali_1'].isin(df_comb_23['pali_1'])
df_23_cl_u = df_23_cl_comb.drop(df_23_cl_comb[logix].index)

df_comb_23_f = pd.concat([df_comb_23, df_23_cl_u])

# print("23 done")

# filter 24
test24 = df['sbs_class'] == "24"
filter = test24
df_24_cl = df.loc[filter]
df_24_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl, df_15_cl, df_16_cl, df_17_cl, df_18_cl, df_19_cl, df_20_cl, df_21_cl, df_22_cl, df_23_cl, df_24_cl])

test24 = df['sbs_class_anki'] == "24"
filter = test24
df_24 = df.loc[filter]

df_comb_24 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17, df_18, df_19, df_20, df_21, df_22, df_23, df_24])

# keep only unique 24
logix = df_24_cl_comb['pali_1'].isin(df_comb_24['pali_1'])
df_24_cl_u = df_24_cl_comb.drop(df_24_cl_comb[logix].index)

df_comb_24_f = pd.concat([df_comb_24, df_24_cl_u])

# print("24 done")

# filter 25
test25 = df['sbs_class'] == "25"
filter = test25
df_25_cl = df.loc[filter]
df_25_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl, df_15_cl, df_16_cl, df_17_cl, df_18_cl, df_19_cl, df_20_cl, df_21_cl, df_22_cl, df_23_cl, df_24_cl, df_25_cl])

test25 = df['sbs_class_anki'] == "25"
filter = test25
df_25 = df.loc[filter]

df_comb_25 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17, df_18, df_19, df_20, df_21, df_22, df_23, df_24, df_25])

# keep only unique 25
logix = df_25_cl_comb['pali_1'].isin(df_comb_25['pali_1'])
df_25_cl_u = df_25_cl_comb.drop(df_25_cl_comb[logix].index)

df_comb_25_f = pd.concat([df_comb_25, df_25_cl_u])

# print("25 done")

# filter 26
test26 = df['sbs_class'] == "26"
filter = test26
df_26_cl = df.loc[filter]
df_26_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl, df_15_cl, df_16_cl, df_17_cl, df_18_cl, df_19_cl, df_20_cl, df_21_cl, df_22_cl, df_23_cl, df_24_cl, df_25_cl, df_26_cl])

test26 = df['sbs_class_anki'] == "26"
filter = test26
df_26 = df.loc[filter]

df_comb_26 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17, df_18, df_19, df_20, df_21, df_22, df_23, df_24, df_25, df_26])

# keep only unique 26
logix = df_26_cl_comb['pali_1'].isin(df_comb_26['pali_1'])
df_26_cl_u = df_26_cl_comb.drop(df_26_cl_comb[logix].index)

df_comb_26_f = pd.concat([df_comb_26, df_26_cl_u])

# print("26 done")

# filter 27
test27 = df['sbs_class'] == "27"
filter = test27
df_27_cl = df.loc[filter]
df_27_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl, df_15_cl, df_16_cl, df_17_cl, df_18_cl, df_19_cl, df_20_cl, df_21_cl, df_22_cl, df_23_cl, df_24_cl, df_25_cl, df_26_cl, df_27_cl])

test27 = df['sbs_class_anki'] == "27"
filter = test27
df_27 = df.loc[filter]

df_comb_27 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17, df_18, df_19, df_20, df_21, df_22, df_23, df_24, df_25, df_26, df_27])

# keep only unique 27
logix = df_27_cl_comb['pali_1'].isin(df_comb_27['pali_1'])
df_27_cl_u = df_27_cl_comb.drop(df_27_cl_comb[logix].index)

df_comb_27_f = pd.concat([df_comb_27, df_27_cl_u])

# print("27 done")

# filter 28
test28 = df['sbs_class'] == "28"
filter = test28
df_28_cl = df.loc[filter]
df_28_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl, df_15_cl, df_16_cl, df_17_cl, df_18_cl, df_19_cl, df_20_cl, df_21_cl, df_22_cl, df_23_cl, df_24_cl, df_25_cl, df_26_cl, df_27_cl, df_28_cl])

test28 = df['sbs_class_anki'] == "28"
filter = test28
df_28 = df.loc[filter]

df_comb_28 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17, df_18, df_19, df_20, df_21, df_22, df_23, df_24, df_25, df_26, df_27, df_28])

# keep only unique 28
logix = df_28_cl_comb['pali_1'].isin(df_comb_28['pali_1'])
df_28_cl_u = df_28_cl_comb.drop(df_28_cl_comb[logix].index)

df_comb_28_f = pd.concat([df_comb_28, df_28_cl_u])

# print("28 done")

# filter 29
test29 = df['sbs_class'] == "29"
filter = test29
df_29_cl = df.loc[filter]
df_29_cl_comb = pd.concat([df_2_cl, df_3_cl, df_4_cl, df_5_cl, df_6_cl, df_7_cl, df_8_cl, df_9_cl, df_10_cl, df_11_cl, df_12_cl, df_13_cl, df_14_cl, df_15_cl, df_16_cl, df_17_cl, df_18_cl, df_19_cl, df_20_cl, df_21_cl, df_22_cl, df_23_cl, df_24_cl, df_25_cl, df_26_cl, df_27_cl, df_28_cl, df_29_cl])

test29 = df['sbs_class_anki'] == "29"
filter = test29
df_29 = df.loc[filter]

df_comb_29 = pd.concat([df_0, df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9, df_10, df_11, df_12, df_13, df_14, df_15, df_16, df_17, df_18, df_19, df_20, df_21, df_22, df_23, df_24, df_25, df_26, df_27, df_28, df_29])

# keep only unique 29
logix = df_29_cl_comb['pali_1'].isin(df_comb_29['pali_1'])
df_29_cl_u = df_29_cl_comb.drop(df_29_cl_comb[logix].index)

df_comb_29_f = pd.concat([df_comb_29, df_29_cl_u])

# print("29 done")

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
df_comb_15_f.to_csv("csv-for-examples/15-class.csv", sep="\t", index=None)
df_comb_16_f.to_csv("csv-for-examples/16-class.csv", sep="\t", index=None)
df_comb_17_f.to_csv("csv-for-examples/17-class.csv", sep="\t", index=None)
df_comb_18_f.to_csv("csv-for-examples/18-class.csv", sep="\t", index=None)
df_comb_19_f.to_csv("csv-for-examples/19-class.csv", sep="\t", index=None)
df_comb_20_f.to_csv("csv-for-examples/20-class.csv", sep="\t", index=None)
df_comb_21_f.to_csv("csv-for-examples/21-class.csv", sep="\t", index=None)
df_comb_22_f.to_csv("csv-for-examples/22-class.csv", sep="\t", index=None)
df_comb_23_f.to_csv("csv-for-examples/23-class.csv", sep="\t", index=None)
df_comb_24_f.to_csv("csv-for-examples/24-class.csv", sep="\t", index=None)
df_comb_25_f.to_csv("csv-for-examples/25-class.csv", sep="\t", index=None)
df_comb_26_f.to_csv("csv-for-examples/26-class.csv", sep="\t", index=None)
df_comb_27_f.to_csv("csv-for-examples/27-class.csv", sep="\t", index=None)
df_comb_28_f.to_csv("csv-for-examples/28-class.csv", sep="\t", index=None)
df_comb_29_f.to_csv("csv-for-examples/29-class.csv", sep="\t", index=None)


print("csv-for-examples saved")


# change Test
# test2 = df['pali_1'] != ""
# filter = test2
# df.loc[filter, ['Test']] = ""

# replace all pattern with '_'
df['pattern'] = df['pattern'].str.replace(' ', '-')

# change pattern of ind
test2 = df['pattern'] == ""
filter = test2
df.loc[filter, ['pattern']] = df['pos']

# df = df[['pali_1', 'pos', 'grammar', 'derived_from', 'neg', 'verb', 'trans', 'plus_case', 'meaning_1', 'ru_meaning', 'root_pali', 'root_base', 'construction', 'sanskrit', 'root_sk', 'variant', 'commentary', 'notes', 'source_1', 'sutta_1', 'example_1', 'source_2', 'sutta_2', 'example_2', 'sbs_chant_pali_2', 'sbs_chant_eng_2', 'sbs_chapter_2', 'sbs_source_3', 'sbs_sutta_3', 'sbs_example_3', 'sbs_chant_pali_3', 'sbs_chant_eng_3', 'sbs_chapter_3', 'pattern', 'Test', 'sbs_class_anki', 'count',  'sbs_audio','Feedback']]

df.sort_values(by='sbs_example_3', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df['sbs_example_3'])))

# replace ṁ
# df['pali_1'] = df['pali_1'].str.replace('ṃ', 'ṁ')
# df['derived_from'] = df['derived_from'].str.replace('ṃ', 'ṁ')
# df['meaning_1'] = df['meaning_1'].str.replace('ṃ', 'ṁ')
# df['root_pali'] = df['root_pali'].str.replace('ṃ', 'ṁ')
# df['root_base'] = df['root_base'].str.replace('ṃ', 'ṁ')
# df['construction'] = df['construction'].str.replace('ṃ', 'ṁ')
# df['sanskrit'] = df['sanskrit'].str.replace('ṃ', 'ṁ')
# df['root_sk'] = df['root_sk'].str.replace('ṃ', 'ṁ')
# df['variant'] = df['variant'].str.replace('ṃ', 'ṁ')
# df['commentary'] = df['commentary'].str.replace('ṃ', 'ṁ')
# df['notes'] = df['notes'].str.replace('ṃ', 'ṁ')
# df['sutta_2'] = df['sutta_2'].str.replace('ṃ', 'ṁ')
# df['example_2'] = df['example_2'].str.replace('ṃ', 'ṁ')
# df['sbs_sutta_3'] = df['sbs_sutta_3'].str.replace('ṃ', 'ṁ')
# df['sbs_example_3'] = df['sbs_example_3'].str.replace('ṃ', 'ṁ')
# df['sbs_chant_pali_3'] = df['sbs_chant_pali_3'].str.replace('ṃ', 'ṁ')
# df['Sutta 4'] = df['Sutta 4'].str.replace('ṃ', 'ṁ')
# df['Example 4'] = df['Example 4'].str.replace('ṃ', 'ṁ')
# df['sbs_chant_pali_4'] = df['sbs_chant_pali_4'].str.replace('ṃ', 'ṁ')
# df['pattern'] = df['pattern'].str.replace('ṃ', 'ṁ')

# filter all classes words
# test15 = df['sbs_class_anki'] != ""
# filter = test15
# df_all = df.loc[filter]

# options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29']


# make words for class 2

options = ['1', '2']

df_words_cl2 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

# df_words_cl2 = df.loc[(df['sbs_class'] < 3) & (df['sbs_class_anki'] < 3)]

df_words_cl2 = df_words_cl2[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl2 = df_words_cl2.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl2.to_csv("vocab/vocab-class2.csv", sep="\t", index=None)
df_words_cl2.to_excel("vocab/vocab-class2.xlsx", index=None)

# make words for class 3

options = ['1', '2', '3']

df_words_cl3 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl3 = df_words_cl3[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl3 = df_words_cl3.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl3.to_csv("vocab/vocab-class3.csv", sep="\t", index=None)
df_words_cl3.to_excel("vocab/vocab-class3.xlsx", index=None)

# make words for class 4

options = ['1', '2', '3', '4']

df_words_cl4 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl4 = df_words_cl4[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl4 = df_words_cl4.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl4.to_csv("vocab/vocab-class4.csv", sep="\t", index=None)
df_words_cl4.to_excel("vocab/vocab-class4.xlsx", index=None)

# make words for class 5

options = ['1', '2', '3', '4', '5']

df_words_cl5 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl5 = df_words_cl5[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl5 = df_words_cl5.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl5.to_csv("vocab/vocab-class5.csv", sep="\t", index=None)
df_words_cl5.to_excel("vocab/vocab-class5.xlsx", index=None)

# make words for class 6

options = ['1', '2', '3', '4', '5', '6']

df_words_cl6 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl6 = df_words_cl6[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl6 = df_words_cl6.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl6.to_csv("vocab/vocab-class6.csv", sep="\t", index=None)
df_words_cl6.to_excel("vocab/vocab-class6.xlsx", index=None)

# make words for class 7

options = ['1', '2', '3', '4', '5', '6', '7']

df_words_cl7 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl7 = df_words_cl7[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl7 = df_words_cl7.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl7.to_csv("vocab/vocab-class7.csv", sep="\t", index=None)
df_words_cl7.to_excel("vocab/vocab-class7.xlsx", index=None)

# make words for class 8

options = ['1', '2', '3', '4', '5', '6', '7', '8']

df_words_cl8 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl8 = df_words_cl8[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl8 = df_words_cl8.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl8.to_csv("vocab/vocab-class8.csv", sep="\t", index=None)
df_words_cl8.to_excel("vocab/vocab-class8.xlsx", index=None)

# make words for class 9

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

df_words_cl9 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl9 = df_words_cl9[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl9 = df_words_cl9.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl9.to_csv("vocab/vocab-class9.csv", sep="\t", index=None)
df_words_cl9.to_excel("vocab/vocab-class9.xlsx", index=None)

# make words for class 10

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

df_words_cl10 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl10 = df_words_cl10[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl10 = df_words_cl10.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl10.to_csv("vocab/vocab-class10.csv", sep="\t", index=None)
df_words_cl10.to_excel("vocab/vocab-class10.xlsx", index=None)

# make words for class 11

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

df_words_cl11 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl11 = df_words_cl11[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl11 = df_words_cl11.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl11.to_csv("vocab/vocab-class11.csv", sep="\t", index=None)
df_words_cl11.to_excel("vocab/vocab-class11.xlsx", index=None)

# make words for class 12

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

df_words_cl12 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl12 = df_words_cl12[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl12 = df_words_cl12.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl12.to_csv("vocab/vocab-class12.csv", sep="\t", index=None)
df_words_cl12.to_excel("vocab/vocab-class12.xlsx", index=None)

# make words for class 13

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

df_words_cl13 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl13 = df_words_cl13[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl13 = df_words_cl13.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl13.to_csv("vocab/vocab-class13.csv", sep="\t", index=None)
df_words_cl13.to_excel("vocab/vocab-class13.xlsx", index=None)

# make words for class 14

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

df_words_cl14 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl14 = df_words_cl14[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl14 = df_words_cl14.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl14.to_csv("vocab/vocab-class14.csv", sep="\t", index=None)
df_words_cl14.to_excel("vocab/vocab-class14.xlsx", index=None)

# make words for class 15

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

df_words_cl15 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl15 = df_words_cl15[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl15 = df_words_cl15.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl15.to_csv("vocab/vocab-class15.csv", sep="\t", index=None)
df_words_cl15.to_excel("vocab/vocab-class15.xlsx", index=None)

# make words for class 16

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']

df_words_cl16 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl16 = df_words_cl16[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl16 = df_words_cl16.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl16.to_csv("vocab/vocab-class16.csv", sep="\t", index=None)
df_words_cl16.to_excel("vocab/vocab-class16.xlsx", index=None)

# make words for class 17

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']

df_words_cl17 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl17 = df_words_cl17[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl17 = df_words_cl17.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl17.to_csv("vocab/vocab-class17.csv", sep="\t", index=None)
df_words_cl17.to_excel("vocab/vocab-class17.xlsx", index=None)

# make words for class 18

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']

df_words_cl18 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl18 = df_words_cl18[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl18 = df_words_cl18.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl18.to_csv("vocab/vocab-class18.csv", sep="\t", index=None)
df_words_cl18.to_excel("vocab/vocab-class18.xlsx", index=None)

# make words for class 19

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']

df_words_cl19 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl19 = df_words_cl19[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl19 = df_words_cl19.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl19.to_csv("vocab/vocab-class19.csv", sep="\t", index=None)
df_words_cl19.to_excel("vocab/vocab-class19.xlsx", index=None)

# make words for class 20

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

df_words_cl20 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl20 = df_words_cl20[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl20 = df_words_cl20.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl20.to_csv("vocab/vocab-class20.csv", sep="\t", index=None)
df_words_cl20.to_excel("vocab/vocab-class20.xlsx", index=None)

# make words for class 21

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']

df_words_cl21 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl21 = df_words_cl21[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl21 = df_words_cl21.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl21.to_csv("vocab/vocab-class21.csv", sep="\t", index=None)
df_words_cl21.to_excel("vocab/vocab-class21.xlsx", index=None)

# make words for class 22

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']

df_words_cl22 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl22 = df_words_cl22[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl22 = df_words_cl22.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl22.to_csv("vocab/vocab-class22.csv", sep="\t", index=None)
df_words_cl22.to_excel("vocab/vocab-class22.xlsx", index=None)

# make words for class 23

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']

df_words_cl23 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl23 = df_words_cl23[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl23 = df_words_cl23.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl23.to_csv("vocab/vocab-class23.csv", sep="\t", index=None)
df_words_cl23.to_excel("vocab/vocab-class23.xlsx", index=None)

# make words for class 24

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']

df_words_cl24 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl24 = df_words_cl24[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl24 = df_words_cl24.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl24.to_csv("vocab/vocab-class24.csv", sep="\t", index=None)
df_words_cl24.to_excel("vocab/vocab-class24.xlsx", index=None)

# make words for class 25

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']

df_words_cl25 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl25 = df_words_cl25[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl25 = df_words_cl25.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl25.to_csv("vocab/vocab-class25.csv", sep="\t", index=None)
df_words_cl25.to_excel("vocab/vocab-class25.xlsx", index=None)

# make words for class 26

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']

df_words_cl26 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl26 = df_words_cl26[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl26 = df_words_cl26.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl26.to_csv("vocab/vocab-class26.csv", sep="\t", index=None)
df_words_cl26.to_excel("vocab/vocab-class26.xlsx", index=None)

# make words for class 27

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27']

df_words_cl27 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl27 = df_words_cl27[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl27 = df_words_cl27.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl27.to_csv("vocab/vocab-class27.csv", sep="\t", index=None)
df_words_cl27.to_excel("vocab/vocab-class27.xlsx", index=None)

# make words for class 28

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']

df_words_cl28 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl28 = df_words_cl28[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl28 = df_words_cl28.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl28.to_csv("vocab/vocab-class28.csv", sep="\t", index=None)
df_words_cl28.to_excel("vocab/vocab-class28.xlsx", index=None)

# make words for class 29

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29']

df_words_cl29 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(options)] 

df_words_cl29 = df_words_cl29[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl29 = df_words_cl29.sort_values(by=['sbs_class', 'pattern'])

# df_words_cl29.to_csv("vocab/vocab-class29.csv", sep="\t", index=None)
df_words_cl29.to_excel("vocab/vocab-class29.xlsx", index=None)

# make words for pict

# make words for pict class 2

options = ['1', '2']

cl = ['2']

df_words_cl2 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl2 = df_words_cl2[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl2 = df_words_cl2.sort_values(by=['sbs_class', 'pattern'])

df_words_cl2.to_csv("csv-for-pic/class2.csv", sep="\t", index=None)

# make words for pict class 3

options = ['1', '2', '3']

cl = ['3']

df_words_cl3 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl3 = df_words_cl3[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl3 = df_words_cl3.sort_values(by=['sbs_class', 'pattern'])

df_words_cl3.to_csv("csv-for-pic/class3.csv", sep="\t", index=None)

# make words for pict class 4

options = ['1', '2', '3', '4']

cl = ['4']

df_words_cl4 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl4 = df_words_cl4[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl4 = df_words_cl4.sort_values(by=['sbs_class', 'pattern'])

df_words_cl4.to_csv("csv-for-pic/class4.csv", sep="\t", index=None)

# make words for pict class 5

options = ['1', '2', '3', '4', '5']

cl = ['5']

df_words_cl5 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl5 = df_words_cl5[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl5 = df_words_cl5.sort_values(by=['sbs_class', 'pattern'])

df_words_cl5.to_csv("csv-for-pic/class5.csv", sep="\t", index=None)

# make words for pict class 6

options = ['1', '2', '3', '4', '5', '6']

cl = ['6']

df_words_cl6 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl6 = df_words_cl6[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl6 = df_words_cl6.sort_values(by=['sbs_class', 'pattern'])

df_words_cl6.to_csv("csv-for-pic/class6.csv", sep="\t", index=None)

# make words for pict class 7

options = ['1', '2', '3', '4', '5', '6', '7']

cl = ['7']

df_words_cl7 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl7 = df_words_cl7[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl7 = df_words_cl7.sort_values(by=['sbs_class', 'pattern'])

df_words_cl7.to_csv("csv-for-pic/class7.csv", sep="\t", index=None)

# make words for pict class 8

options = ['1', '2', '3', '4', '5', '6', '7', '8']

cl = ['8']

df_words_cl8 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl8 = df_words_cl8[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl8 = df_words_cl8.sort_values(by=['sbs_class', 'pattern'])

df_words_cl8.to_csv("csv-for-pic/class8.csv", sep="\t", index=None)

# make words for pict class 9

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

cl = ['9']

df_words_cl9 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl9 = df_words_cl9[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl9 = df_words_cl9.sort_values(by=['sbs_class', 'pattern'])

df_words_cl9.to_csv("csv-for-pic/class9.csv", sep="\t", index=None)

# make words for pict class 10

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

cl = ['10']

df_words_cl10 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl10 = df_words_cl10[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl10 = df_words_cl10.sort_values(by=['sbs_class', 'pattern'])

df_words_cl10.to_csv("csv-for-pic/class10.csv", sep="\t", index=None)

# make words for pict class 11

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

cl = ['11']

df_words_cl11 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl11 = df_words_cl11[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl11 = df_words_cl11.sort_values(by=['sbs_class', 'pattern'])

df_words_cl11.to_csv("csv-for-pic/class11.csv", sep="\t", index=None)

# make words for pict class 12

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

cl = ['12']

df_words_cl12 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl12 = df_words_cl12[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl12 = df_words_cl12.sort_values(by=['sbs_class', 'pattern'])

df_words_cl12.to_csv("csv-for-pic/class12.csv", sep="\t", index=None)

# make words for pict class 13

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

cl = ['13']

df_words_cl13 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl13 = df_words_cl13[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl13 = df_words_cl13.sort_values(by=['sbs_class', 'pattern'])

df_words_cl13.to_csv("csv-for-pic/class13.csv", sep="\t", index=None)

# make words for pict class 14

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

cl = ['14']

df_words_cl14 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl14 = df_words_cl14[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl14 = df_words_cl14.sort_values(by=['sbs_class', 'pattern'])

df_words_cl14.to_csv("csv-for-pic/class14.csv", sep="\t", index=None)

# make words for pict class 15

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

cl = ['15']

df_words_cl15 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl15 = df_words_cl15[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl15 = df_words_cl15.sort_values(by=['sbs_class', 'pattern'])

df_words_cl15.to_csv("csv-for-pic/class15.csv", sep="\t", index=None)

# make words for pict class 16

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']

cl = ['16']

df_words_cl16 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl16 = df_words_cl16[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl16 = df_words_cl16.sort_values(by=['sbs_class', 'pattern'])

df_words_cl16.to_csv("csv-for-pic/class16.csv", sep="\t", index=None)

# make words for pict class 17

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']

cl = ['17']

df_words_cl17 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl17 = df_words_cl17[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl17 = df_words_cl17.sort_values(by=['sbs_class', 'pattern'])

df_words_cl17.to_csv("csv-for-pic/class17.csv", sep="\t", index=None)

# make words for pict class 18

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']

cl = ['18']

df_words_cl18 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl18 = df_words_cl18[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl18 = df_words_cl18.sort_values(by=['sbs_class', 'pattern'])

df_words_cl18.to_csv("csv-for-pic/class18.csv", sep="\t", index=None)

# make words for pict class 19

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']

cl = ['19']

df_words_cl19 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl19 = df_words_cl19[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl19 = df_words_cl19.sort_values(by=['sbs_class', 'pattern'])

df_words_cl19.to_csv("csv-for-pic/class19.csv", sep="\t", index=None)

# make words for pict class 20

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

cl = ['20']

df_words_cl20 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl20 = df_words_cl20[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl20 = df_words_cl20.sort_values(by=['sbs_class', 'pattern'])

df_words_cl20.to_csv("csv-for-pic/class20.csv", sep="\t", index=None)

# make words for pict class 21

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']

cl = ['21']

df_words_cl21 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl21 = df_words_cl21[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl21 = df_words_cl21.sort_values(by=['sbs_class', 'pattern'])

df_words_cl21.to_csv("csv-for-pic/class21.csv", sep="\t", index=None)

# make words for pict class 22

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']

cl = ['22']

df_words_cl22 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl22 = df_words_cl22[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl22 = df_words_cl22.sort_values(by=['sbs_class', 'pattern'])

df_words_cl22.to_csv("csv-for-pic/class22.csv", sep="\t", index=None)

# make words for pict class 23

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']

cl = ['23']

df_words_cl23 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl23 = df_words_cl23[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl23 = df_words_cl23.sort_values(by=['sbs_class', 'pattern'])

df_words_cl23.to_csv("csv-for-pic/class23.csv", sep="\t", index=None)

# make words for pict class 24

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']

cl = ['24']

df_words_cl24 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl24 = df_words_cl24[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl24 = df_words_cl24.sort_values(by=['sbs_class', 'pattern'])

df_words_cl24.to_csv("csv-for-pic/class24.csv", sep="\t", index=None)

# make words for pict class 25

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']

cl = ['25']

df_words_cl25 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl25 = df_words_cl25[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl25 = df_words_cl25.sort_values(by=['sbs_class', 'pattern'])

df_words_cl25.to_csv("csv-for-pic/class25.csv", sep="\t", index=None)

# make words for pict class 26

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26']

cl = ['26']

df_words_cl26 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl26 = df_words_cl26[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl26 = df_words_cl26.sort_values(by=['sbs_class', 'pattern'])

df_words_cl26.to_csv("csv-for-pic/class26.csv", sep="\t", index=None)

# make words for pict class 27

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27']

cl = ['27']

df_words_cl27 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl27 = df_words_cl27[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl27 = df_words_cl27.sort_values(by=['sbs_class', 'pattern'])

df_words_cl27.to_csv("csv-for-pic/class27.csv", sep="\t", index=None)

# make words for pict class 28

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']

cl = ['28']

df_words_cl28 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl28 = df_words_cl28[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl28 = df_words_cl28.sort_values(by=['sbs_class', 'pattern'])

df_words_cl28.to_csv("csv-for-pic/class28.csv", sep="\t", index=None)

# make words for pict class 29

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29']

cl = ['29']

df_words_cl29 = df.loc[df['sbs_class'].isin(options) & df['sbs_class_anki'].isin(cl)] 

df_words_cl29 = df_words_cl29[['pali_1', 'pos', 'meaning_1', 'pattern', 'sbs_class']]

df_words_cl29 = df_words_cl29.sort_values(by=['sbs_class', 'pattern'])

df_words_cl29.to_csv("csv-for-pic/class29.csv", sep="\t", index=None)


# remove column count from df

df.sort_values(by='sbs_example_3', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df['sbs_example_3'])))

df = df.drop(['sbs_category', 'sbs_class', 'count', 'sbs_source_5', 'sbs_sutta_5', 'sbs_example_5', 'move', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_notes', 'ru_notes'], axis=1)
# print("columns 'sbs_category' 'sbs_class', 'count', 'sbs_source_5', 'sbs_sutta_5', 'sbs_example_5', 'move', 'sbs_chant_pali_5', 'sbs_chant_eng_5', 'sbs_chapter_5', 'sbs_notes', 'ru_notes' has been dropped for df")

# filter 0 classes words
test2 = df['sbs_class_anki'] == "-"
filter = test2
df_0 = df.loc[filter]

# filter 1 classes words
test2 = df['sbs_class_anki'] == "1"
filter = test2
df_1 = df.loc[filter]

# filter 2 classes words
test2 = df['sbs_class_anki'] == "2"
filter = test2
df_2 = df.loc[filter]

# filter 3 classes words
test3 = df['sbs_class_anki'] == "3"
filter = test3
df_3 = df.loc[filter]

# filter 4 classes words
test4 = df['sbs_class_anki'] == "4"
filter = test4
df_4 = df.loc[filter]

# filter 5 classes words
test5 = df['sbs_class_anki'] == "5"
filter = test5
df_5 = df.loc[filter]

# filter 6 classes words
test6 = df['sbs_class_anki'] == "6"
filter = test6
df_6 = df.loc[filter]

# filter 7 classes words
test7 = df['sbs_class_anki'] == "7"
filter = test7
df_7 = df.loc[filter]

# filter 8 classes words
test8 = df['sbs_class_anki'] == "8"
filter = test8
df_8 = df.loc[filter]

# filter 9 classes words
test9 = df['sbs_class_anki'] == "9"
filter = test9
df_9 = df.loc[filter]

# filter 10 classes words
test10 = df['sbs_class_anki'] == "10"
filter = test10
df_10 = df.loc[filter]

# filter 11 classes words
test11 = df['sbs_class_anki'] == "11"
filter = test11
df_11 = df.loc[filter]

# filter 12 classes words
test12 = df['sbs_class_anki'] == "12"
filter = test12
df_12 = df.loc[filter]

# filter 13 classes words
test13 = df['sbs_class_anki'] == "13"
filter = test13
df_13 = df.loc[filter]

# filter 14 classes words
test14 = df['sbs_class_anki'] == "14"
filter = test14
df_14 = df.loc[filter]

# filter 15 classes words
test15 = df['sbs_class_anki'] == "15"
filter = test15
df_15 = df.loc[filter]

# filter 16 classes words
test16 = df['sbs_class_anki'] == "16"
filter = test16
df_16 = df.loc[filter]

# filter 17 classes words
test17 = df['sbs_class_anki'] == "17"
filter = test17
df_17 = df.loc[filter]

# filter 18 classes words
test18 = df['sbs_class_anki'] == "18"
filter = test18
df_18 = df.loc[filter]

# filter 19 classes words
test19 = df['sbs_class_anki'] == "19"
filter = test19
df_19 = df.loc[filter]

# filter 20 classes words
test20 = df['sbs_class_anki'] == "20"
filter = test20
df_20 = df.loc[filter]

# filter 21 classes words
test21 = df['sbs_class_anki'] == "21"
filter = test21
df_21 = df.loc[filter]

# filter 22 classes words
test22 = df['sbs_class_anki'] == "22"
filter = test22
df_22 = df.loc[filter]

# filter 23 classes words
test23 = df['sbs_class_anki'] == "23"
filter = test23
df_23 = df.loc[filter]

# filter 24 classes words
test24 = df['sbs_class_anki'] == "24"
filter = test24
df_24 = df.loc[filter]

# filter 25 classes words
test25 = df['sbs_class_anki'] == "25"
filter = test25
df_25 = df.loc[filter]

# filter 26 classes words
test26 = df['sbs_class_anki'] == "26"
filter = test26
df_26 = df.loc[filter]

# filter 27 classes words
test27 = df['sbs_class_anki'] == "27"
filter = test27
df_27 = df.loc[filter]

# filter 28 classes words
test28 = df['sbs_class_anki'] == "28"
filter = test28
df_28 = df.loc[filter]

# filter 29 classes words
test29 = df['sbs_class_anki'] == "29"
filter = test29
df_29 = df.loc[filter]

# save classes csv

# df_0.to_csv("../csv-for-anki/classes/0-class-anki.csv", sep="\t", index=None)
# df_1 = df_1.drop(['Feedback'], axis=1)
# df_1['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&amp;entry.644913945=Anki Deck Vocab Pāli Course">Fix it here</a>."""
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
df_15.to_csv("../csv-for-anki/classes/15-class-anki.csv", sep="\t", index=None)
df_16.to_csv("../csv-for-anki/classes/16-class-anki.csv", sep="\t", index=None)
df_17.to_csv("../csv-for-anki/classes/17-class-anki.csv", sep="\t", index=None)
df_18.to_csv("../csv-for-anki/classes/18-class-anki.csv", sep="\t", index=None)
df_19.to_csv("../csv-for-anki/classes/19-class-anki.csv", sep="\t", index=None)
df_20.to_csv("../csv-for-anki/classes/20-class-anki.csv", sep="\t", index=None)
df_21.to_csv("../csv-for-anki/classes/21-class-anki.csv", sep="\t", index=None)
df_22.to_csv("../csv-for-anki/classes/22-class-anki.csv", sep="\t", index=None)
df_23.to_csv("../csv-for-anki/classes/23-class-anki.csv", sep="\t", index=None)
df_24.to_csv("../csv-for-anki/classes/24-class-anki.csv", sep="\t", index=None)
df_25.to_csv("../csv-for-anki/classes/25-class-anki.csv", sep="\t", index=None)
df_26.to_csv("../csv-for-anki/classes/26-class-anki.csv", sep="\t", index=None)
df_27.to_csv("../csv-for-anki/classes/27-class-anki.csv", sep="\t", index=None)
df_28.to_csv("../csv-for-anki/classes/28-class-anki.csv", sep="\t", index=None)
df_29.to_csv("../csv-for-anki/classes/29-class-anki.csv", sep="\t", index=None)


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

# save all finished classes

options = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29']

df_all = df.loc[df['sbs_class_anki'].isin(options)] 

df_all.to_csv("../csv-for-anki/classes/all-class.csv", sep="\t", index=None)