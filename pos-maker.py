import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re

df = read_ods("original-sources/frequent-words.ods")
df.fillna("", inplace=True)

# sort by frequency
df = df.sort_values(by=['count'], ascending = False)

#adv of time
test1 = df['POS'] == "ind"
test2 = df['Grammar'] == "time"
filter = test1 & test2
df_time = df.loc[filter]

# save time csv
df_time[['Pāli1', 'count']].to_csv("frequent-words/time.csv", sep="\t", index=None)

#adv of place
test1 = df['POS'] == "ind"
test2 = df['Grammar'] == "place"
filter = test1 & test2
df_place = df.loc[filter]

# save place csv
df_place[['Pāli1', 'count']].to_csv("frequent-words/place.csv", sep="\t", index=None)

#adv of interr
test1 = df['POS'] == "ind"
test2 = df['Grammar'] == "interr"
filter = test1 & test2
df_interr = df.loc[filter]

# save interr csv
df_interr[['Pāli1', 'count']].to_csv("frequent-words/interr.csv", sep="\t", index=None)


# filter what is done
df = df.head(650)

# filter not comp | comp vb | name
test1 = df['Grammar'] != "comp"
test2 = df['Grammar'] != "comp vb"
test3 = df['Grammar'] != "name"
filter = test1 & test2 & test3
df = df.loc[filter]

# save first 1000
df.head(1000)[['Pāli1', 'count']].to_csv("curated-sources/1000-words.csv", sep="\t", index=None)

# filter a masc
test1 = df['POS'] == "masc"
test2 = df['Pattern'] == "a masc"
filter = test1 & test2
df_a_masc = df.loc[filter]

# save first 50 a masc csv
df_a_masc.head(300)[['Pāli1', 'count']].to_csv("frequent-words/a-masc.csv", sep="\t", index=None)

# filter i masc
test1 = df['POS'] == "masc"
test2 = df['Pattern'] == "i masc"
filter = test1 & test2
df_i_masc = df.loc[filter]

# save first 50 i masc csv
df_i_masc.head(50)[['Pāli1', 'count']].to_csv("frequent-words/i-masc.csv", sep="\t", index=None)

# filter ī masc
test1 = df['POS'] == "masc"
test2 = df['Pattern'] == "ī masc"
filter = test1 & test2
df_ii_masc = df.loc[filter]

# save first 50 ī masc csv
df_ii_masc.head(50)[['Pāli1', 'count']].to_csv("frequent-words/ī-masc.csv", sep="\t", index=None)

# filter u masc
test1 = df['POS'] == "masc"
test2 = df['Pattern'] == "u masc"
filter = test1 & test2
df_u_masc = df.loc[filter]

# save first 50 u masc csv
df_u_masc.head(50)[['Pāli1', 'count']].to_csv("frequent-words/u-masc.csv", sep="\t", index=None)

# filter ant adj
test1 = df['POS'] == "adj"
test2 = df['Pattern'] == "ant adj"
filter = test1 & test2
df_ant_adj = df.loc[filter]

# filter ant masc
test1 = df['POS'] == "masc"
test2 = df['Pattern'] == "ant masc"
filter = test1 & test2
df_ant_masc = df.loc[filter]

#combine ant
df_ant = pd.concat([df_ant_adj, df_ant_masc])
df_ant = df_ant.sort_values(by=['count'], ascending = False)

# save first 50 ant adj csv
df_ant.head(50)[['Pāli1', 'count']].to_csv("frequent-words/ant.csv", sep="\t", index=None)

# filter ar masc
test1 = df['POS'] == "masc"
test2 = df['Pattern'] == "ar masc"
filter = test1 & test2
df_ar_masc = df.loc[filter]

# save first 50 ar masc csv
df_ar_masc.head(50)[['Pāli1', 'count']].to_csv("frequent-words/ar-masc.csv", sep="\t", index=None)

# filter ati pr
test1 = df['POS'] == "pr"
test2 = df['Pattern'] == "ati pr"
filter = test1 & test2
df_ati_pr = df.loc[filter]

# save first 50 ati pr csv
df_ati_pr.head(100)[['Pāli1', 'count']].to_csv("frequent-words/ati-pr.csv", sep="\t", index=None)

# filter eti pr
test1 = df['POS'] == "pr"
test2 = df['Pattern'] == "eti pr"
filter = test1 & test2
df_eti_pr = df.loc[filter]

# save first 50 eti pr csv
df_eti_pr.head(50)[['Pāli1', 'count']].to_csv("frequent-words/eti-pr.csv", sep="\t", index=None)

# filter āti pr
test1 = df['POS'] == "pr"
test2 = df['Pattern'] == "āti pr"
filter = test1 & test2
df_aati_pr = df.loc[filter]

# save first 50 āti pr csv
df_aati_pr.head(50)[['Pāli1', 'count']].to_csv("frequent-words/āti-pr.csv", sep="\t", index=None)

# filter other pr
test1 = df['POS'] == "pr"
test2 = df['Pattern'] != "āti pr"
test3 = df['Pattern'] != "eti pr"
test4 = df['Pattern'] != "ati pr"
filter = test1 & test2 & test3 & test4
df_other_pr = df.loc[filter]

# save first 50 other pr csv
df_other_pr.head(50)[['Pāli1', 'count']].to_csv("frequent-words/other-pr.csv", sep="\t", index=None)


# filter i aor
test1 = df['POS'] == "aor"
test2 = df['Pattern'] == "i aor"
filter = test1 & test2
df_i_aor = df.loc[filter]

# save first 50 i aor csv
df_i_aor.head(50)[['Pāli1', 'count']].to_csv("frequent-words/i-aor.csv", sep="\t", index=None)

# filter esi aor
test1 = df['POS'] == "aor"
test2 = df['Pattern'] == "esi aor"
filter = test1 & test2
df_esi_aor = df.loc[filter]

# save first 50 esi aor csv
df_esi_aor.head(50)[['Pāli1', 'count']].to_csv("frequent-words/esi-aor.csv", sep="\t", index=None)

# filter other aor
test1 = df['POS'] == "aor"
test2 = df['Pattern'] != "esi aor"
test2 = df['Pattern'] != "i aor"
filter = test1 & test2 & test3
df_other_aor = df.loc[filter]

# save first 50 other aor csv
df_other_aor.head(50)[['Pāli1', 'count']].to_csv("frequent-words/other-aor.csv", sep="\t", index=None)


# filter fut
test1 = df['POS'] == "fut"
filter = test1
df_fut = df.loc[filter]

# save first 50 fut csv
df_fut.head(50)[['Pāli1', 'count']].to_csv("frequent-words/fut.csv", sep="\t", index=None)

# save summary csv
df_comb = pd.concat([df_a_masc, df_aati_pr, df_ant, df_ar_masc, df_ati_pr, df_esi_aor, df_eti_pr, df_fut, df_i_aor, df_i_masc, df_ii_masc, df_other_aor, df_other_pr, df_u_masc, df_time])

df_comb = df_comb.sort_values(by=['count'], ascending = False)


df_comb[['Pāli1', 'Pattern', 'count']].to_csv("frequent-words/comb.csv", sep="\t", index=None)
