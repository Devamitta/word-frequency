import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re

df = read_ods("original-sources/frequent-words.ods")
df.fillna("", inplace=True)

# sort by frequency
df = df.sort_values(by=['count'], ascending = False)

# save first 1000
df.head(1000)[['headword', 'count']].to_csv("curated-sources/1000-words.csv", sep="\t", index=None)

# filter a masc
test1 = df['pos'] == "masc"
test2 = df['pattern'] == "a masc"
filter = test1 & test2
df_a_masc = df.loc[filter]

# save first 50 a masc csv
df_a_masc.head(50)[['headword', 'count']].to_csv("frequent-words/a-masc.csv", sep="\t", index=None)

# filter i masc
test1 = df['pos'] == "masc"
test2 = df['pattern'] == "i masc"
filter = test1 & test2
df_i_masc = df.loc[filter]

# save first 50 i masc csv
df_i_masc.head(50)[['headword', 'count']].to_csv("frequent-words/i-masc.csv", sep="\t", index=None)

# filter ī masc
test1 = df['pos'] == "masc"
test2 = df['pattern'] == "ī masc"
filter = test1 & test2
df_ii_masc = df.loc[filter]

# save first 50 ī masc csv
df_ii_masc.head(50)[['headword', 'count']].to_csv("frequent-words/ī-masc.csv", sep="\t", index=None)

# filter u masc
test1 = df['pos'] == "masc"
test2 = df['pattern'] == "u masc"
filter = test1 & test2
df_u_masc = df.loc[filter]

# save first 50 u masc csv
df_u_masc.head(50)[['headword', 'count']].to_csv("frequent-words/u-masc.csv", sep="\t", index=None)

# filter ant masc
test1 = df['pos'] == "masc"
test2 = df['pattern'] == "ant masc"
filter = test1 & test2
df_ant_masc = df.loc[filter]

# save first 50 ant masc csv
df_ant_masc.head(50)[['headword', 'count']].to_csv("frequent-words/ant-masc.csv", sep="\t", index=None)

# filter pr
test1 = df['pos'] == "pr"
filter = test1
df_pr = df.loc[filter]

# save first 50 pr csv
df_pr.head(50)[['headword', 'count']].to_csv("frequent-words/pr.csv", sep="\t", index=None)

# filter aor
test1 = df['pos'] == "aor"
filter = test1
df_aor = df.loc[filter]

# save first 50 aor csv
df_aor.head(50)[['headword', 'count']].to_csv("frequent-words/aor.csv", sep="\t", index=None)

# filter fut
test1 = df['pos'] == "fut"
filter = test1
df_fut = df.loc[filter]

# save first 50 fut csv
df_fut.head(50)[['headword', 'count']].to_csv("frequent-words/fut.csv", sep="\t", index=None)