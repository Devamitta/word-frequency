import pandas as pd
import re

df_nid = pd.read_csv("../spreadsheets/nidh_bold.csv", sep="\t", dtype= str)
df_nid.fillna("", inplace=True)

# df_sbs = pd.read_csv("../spreadsheets/sbs-pd.csv", sep="\t", dtype= str)
# df_sbs.fillna("", inplace=True)

df_class_1 = pd.read_csv("csv-for-classes/class-1.csv", sep="\t", dtype= str)
df_class_1.fillna("", inplace=True)

df_class_2 = pd.read_csv("csv-for-classes/class-2.csv", sep="\t", dtype= str)
df_class_2.fillna("", inplace=True)

df_class_3 = pd.read_csv("csv-for-classes/class-3.csv", sep="\t", dtype= str)
df_class_3.fillna("", inplace=True)

df_class_4 = pd.read_csv("csv-for-classes/class-4.csv", sep="\t", dtype= str)
df_class_4.fillna("", inplace=True)

df_class_5 = pd.read_csv("csv-for-classes/class-5.csv", sep="\t", dtype= str)
df_class_5.fillna("", inplace=True)

# filter
# test2 = df_nid['Meaning IN CONTEXT'] != ""
# test3 = df_nid['Source1'] != ""
# filter = test2 & test3
# df_nid = df_nid.loc[filter]

# removing numbers nid
df_nid['Pāli2'] = df_nid['Pāli1']
df_nid['Pāli1'] = df_nid['Pāli1'].str.replace('\d+', '')
df_nid['Pāli1'] = df_nid['Pāli1'].str.replace(' ', '')

# # removing numbers sbs
# df_sbs['Pāli2'] = df_sbs['Pāli1']
# df_sbs['Pāli1'] = df_sbs['Pāli1'].str.replace('\d+', '')
# df_sbs['Pāli1'] = df_sbs['Pāli1'].str.replace(' ', '')

# find words in niddhi

test1 = df_nid['Pāli1'].isin(df_class_1['Pāli1'])
test2 = df_nid['Pattern'].isin(df_class_1['Pattern'])

logix = test1 & test2

df_nid_frequent = df_nid[logix]

# find if not

test1 = ~df_class_1['Pāli1'].isin(df_nid['Pāli1'])
# test2 = ~df_class_1['Pattern'].isin(df_nid['Pattern'])

logix = test1

df_absent = pd.DataFrame()

df_absent = df_absent.append([df_class_1[logix]])
# df_absent = df_absent df_class_1[logix]

# adding feedback ?
# df_absent.reset_index(drop=True, inplace=True)
df_absent['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform">Fix it here</a>."""


df_absent.to_csv(f"../spreadsheets/absent.csv", sep="\t", index=None)

# find words in sbs

# test1 = df_sbs['Pāli1'].isin(df_class_1['Pāli1'])
# test2 = df_sbs['Pattern'].isin(df_class_1['Pattern'])

# logix = test1 & test2

# df_sbs_frequent = df_sbs[logix]

# merge frequency column
df_final_nid = pd.merge(df_nid_frequent, df_class_1, how='left')

# df_final_sbs = pd.merge(df_sbs_frequent, df_class_1, how='left')

# retern numbers
# df_final_nid['Pāli1']=df_final_nid['Pāli2']
# df_final_sbs['Pāli1']=df_final_sbs['Pāli2']

# cleaning ex2
df_final_nid['Source 2'] = ""
df_final_nid['Sutta2'] = ""
df_final_nid['Example 2'] = ""

# adding feedback
df_final_nid.reset_index(drop=True, inplace=True)
df_final_nid['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df_final_nid.Pāli1 + """&entry.1433863141=Pāli Class Vocab">Fix it here</a>."""

# adding tag
df_final_nid['Tag'] = df_final_nid['Pattern']
df_final_nid['Tag'] = df_final_nid['Tag'].str.replace(' ', '-')


# sort by frequency
df_final_nid = df_final_nid.sort_values(by=['count'], ascending = False)

# choosing order of columns
df_final_nid = df_final_nid[['Pāli1', 'POS', 'Grammar', 'Derived from', 'Neg', 'Verb', 'Trans', 'Case', 'Meaning IN CONTEXT', 'Meaning in native language', 'Pāli Root', 'Base', 'Construction', 'Sanskrit', 'Sk Root', 'Source1', 'Sutta1', 'Example1', 'Source 2', 'Sutta2', 'Example 2', 'Stem', 'Pattern', 'count', 'Feedback', 'Tag', 'marks']]

# save csv
df_final_nid.to_csv(f"../spreadsheets/nid-most-common.csv", sep="\t", index=None)

# df_final_sbs.to_csv(f"../spreadsheets/sbs-most-common.csv", sep="\t", index=None)