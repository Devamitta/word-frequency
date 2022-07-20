import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re

df = read_ods("original-sources/frequent-words.ods")
df.fillna("", inplace=True)

# sort by frequency
df = df.sort_values(by=['count', 'Pāli1'], ascending = False)

#filter adv
test1 = df['POS'] == "ind"
test2 = df['Grammar'] == "time"
test3 = df['Grammar'] == "place"
test4 = df['Grammar'] == "interr"

filter = test1 & test2
df_time = df.loc[filter]

filter = test1 & test3
df_place = df.loc[filter]

filter = test1 & test4
df_interr = df.loc[filter]

# save adv csv
df_time[['Pāli1', 'count']].to_csv("frequent-words/time.csv", sep="\t", index=None)

df_place[['Pāli1', 'count']].to_csv("frequent-words/place.csv", sep="\t", index=None)

df_interr[['Pāli1', 'count']].to_csv("frequent-words/interr.csv", sep="\t", index=None)


# filter what is done
df = df.head(1000)

# filter not comp | comp vb | name
test1 = df['Grammar'] != "comp"
test2 = df['Grammar'] != "comp vb"
# test3 = df['Grammar'] != "name"
filter = test1 & test2
df = df.loc[filter]

# save first 1000
df.head(1000)[['Pāli1', 'count']].to_csv("curated-sources/1000-words.csv", sep="\t", index=None)

# filter masc

test1 = df['POS'] == "masc"
test2 = df['Pattern'] == "a masc"
test3 = df['Pattern'] == "i masc"
test4 = df['Pattern'] == "ī masc"
test5 = df['Pattern'] == "u masc"
test6 = df['Pattern'] == "ar masc"

filter = test1 & test2
df_a_masc = df.loc[filter]

filter = test1 & test3
df_i_masc = df.loc[filter]

filter = test1 & test4
df_ii_masc = df.loc[filter]

filter = test1 & test5
df_u_masc = df.loc[filter]

filter = test1 & test6
df_ar_masc = df.loc[filter]

# save masc csv

df_a_masc.head(300)[['Pāli1', 'count']].to_csv("frequent-words/a-masc.csv", sep="\t", index=None)

df_i_masc.head(50)[['Pāli1', 'count']].to_csv("frequent-words/i-masc.csv", sep="\t", index=None)

df_ii_masc.head(50)[['Pāli1', 'count']].to_csv("frequent-words/ī-masc.csv", sep="\t", index=None)

df_u_masc.head(50)[['Pāli1', 'count']].to_csv("frequent-words/u-masc.csv", sep="\t", index=None)

df_ar_masc.head(50)[['Pāli1', 'count']].to_csv("frequent-words/ar-masc.csv", sep="\t", index=None)

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

# save ant csv
df_ant.head(50)[['Pāli1', 'count']].to_csv("frequent-words/ant.csv", sep="\t", index=None)

# filter pr
test1 = df['POS'] == "pr"
test2 = df['Pattern'] == "ati pr"
test3 = df['Pattern'] == "eti pr"
test4 = df['Pattern'] == "āti pr"
test5 = df['Pattern'] == "oti pr"
filter = test1 & test2
df_ati_pr = df.loc[filter]

filter = test1 & test3
df_eti_pr = df.loc[filter]

filter = test1 & test4
df_aati_pr = df.loc[filter]

filter = test1 & test5
df_oti_pr = df.loc[filter]

# save pr csv

df_ati_pr.head(100)[['Pāli1', 'count']].to_csv("frequent-words/ati-pr.csv", sep="\t", index=None)

df_eti_pr.head(50)[['Pāli1', 'count']].to_csv("frequent-words/eti-pr.csv", sep="\t", index=None)

df_aati_pr.head(50)[['Pāli1', 'count']].to_csv("frequent-words/āti-pr.csv", sep="\t", index=None)

df_oti_pr.head(50)[['Pāli1', 'count']].to_csv("frequent-words/oti-pr.csv", sep="\t", index=None)

# filter other pr
test1 = df['POS'] == "pr"
test2 = df['Pattern'] != "āti pr"
test3 = df['Pattern'] != "eti pr"
test4 = df['Pattern'] != "ati pr"
test5 = df['Pattern'] != "oti pr"
filter = test1 & test2 & test3 & test4 & test5
df_other_pr = df.loc[filter]

# save other pr csv
df_other_pr.head(50)[['Pāli1', 'count']].to_csv("frequent-words/other-pr.csv", sep="\t", index=None)

# filter aor
test1 = df['POS'] == "aor"
test2 = df['Pattern'] == "i aor"
test3 = df['Pattern'] == "esi aor"
test4 = df['Pattern'] == "āsi aor"
test5 = df['Pattern'] == "i aor isuṃ"
test6 = df['Pattern'] == "āsi aor iṃsu"
filter = test1 & test2
df_i_aor = df.loc[filter]

filter = test1 & test5
df_i_aor_is = df.loc[filter]
df_i_aor = pd.concat([df_i_aor, df_i_aor_is])
df_i_aor = df_i_aor.sort_values(by=['count', 'Pāli1'], ascending = False)

filter = test1 & test3
df_esi_aor = df.loc[filter]

filter = test1 & test4
df_aasi_aor = df.loc[filter]

filter = test1 & test6
df_aasi_im_aor = df.loc[filter]
df_aasi_aor = pd.concat([df_aasi_aor, df_aasi_im_aor])
df_aasi_aor = df_aasi_aor.sort_values(by=['count', 'Pāli1'], ascending = False)

# save aor
df_i_aor.head(50)[['Pāli1', 'count']].to_csv("frequent-words/i-aor.csv", sep="\t", index=None)

df_esi_aor.head(50)[['Pāli1', 'count']].to_csv("frequent-words/esi-aor.csv", sep="\t", index=None)

df_aasi_aor.head(50)[['Pāli1', 'count']].to_csv("frequent-words/āsi-aor.csv", sep="\t", index=None)

# filter other aor
test1 = df['POS'] == "aor"
test2 = df['Pattern'] != "esi aor"
test3 = df['Pattern'] != "i aor"
test4 = df['Pattern'] != "āsi aor"
test5 = df['Pattern'] != "i aor isuṃ"
test6 = df['Pattern'] != "āsi aor iṃsu"
filter = test1 & test2 & test3 & test4 & test5 & test6
df_other_aor = df.loc[filter]

# save other aor csv
df_other_aor.head(50)[['Pāli1', 'count']].to_csv("frequent-words/other-aor.csv", sep="\t", index=None)

# filter fut
test1 = df['POS'] == "fut"
filter = test1
df_fut = df.loc[filter]

# save fut csv
df_fut.head(50)[['Pāli1', 'count']].to_csv("frequent-words/fut.csv", sep="\t", index=None)

# save summary csv
df_comb = pd.concat([df_a_masc, df_aati_pr, df_ant, df_ar_masc, df_ati_pr, df_esi_aor, df_eti_pr, df_fut, df_i_aor, df_i_masc, df_ii_masc, df_aasi_aor, df_oti_pr, df_u_masc, df_time])

df_comb = df_comb.sort_values(by=['count'], ascending = False)


df_comb[['Pāli1', 'Pattern', 'count']].to_csv("frequent-words/comb.csv", sep="\t", index=None)
