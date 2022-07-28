
import pandas as pd
import random

df = pd.read_csv("../spreadsheets/dps-full.csv", sep="\t", dtype= str)
df.fillna("", inplace=True)

# change Meaning in native language
test1 = df['Pāli1'] != ""
filter = test1
df.loc[filter, ['Meaning in native language']] = ""

# filter all SBS words
test2 = df['class'] != ""
filter = test2
df = df.loc[filter]

# make Feedback
# df.insert(39, 'Feedback', "<a href=\"https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500="+df['Pāli1']+"\">feedback</a>")

# adding feedback
df.reset_index(drop=True, inplace=True)
df['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df.Pāli1 + """&entry.1433863141=Pāli Class Vocab">Fix it here</a>."""

# make double tags
# df.insert(40, 'Tags', None)

# df["Tags"] = df["Pali chant 2"]

# test3 = df['Pali chant 3'] != ""
# filter = test3
# df.loc[filter, ['Tags']] = df['Pali chant 2'] + " " + df['Pali chant 3']

# replace all Pattern with '_'
df['Pattern'] = df['Pattern'].str.replace(' ', '-')
# df['Pattern 2'] = df['Pattern 2'].str.replace(' ', '_')


# choosing order of columns
df = df[['Pāli1', 'POS', 'Grammar', 'Derived from', 'Neg', 'Verb', 'Trans', 'Case', 'Meaning IN CONTEXT', 'Meaning in native language', 'Pāli Root', 'Base', 'Construction', 'Sanskrit', 'Sk Root', 'Source1', 'Sutta1', 'Example1', 'Source 2', 'Sutta2', 'Example 2', 'Pali chant 2', 'English chant 2', 'Chapter 2', 'Stem', 'Pattern', 'Test', 'class', 'count', 'Feedback']]

# sort by frequency
# df = df.sort_values(by=['count'], ascending = False)
# df.sort_values(["count"], ascending=False, inplace=True)
df.sort_values(by = ['count'], ignore_index=True, ascending=False, inplace=True)

# save csv
df.to_csv("../spreadsheets/for-anki-class.csv", sep="\t", index=None)

