import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re

df = read_ods("original-sources/frequent-words.ods")
df.fillna("", inplace=True)

df_nid = pd.read_csv("../spreadsheets/nidh_bold.csv", sep="\t", dtype= str)
df_nid.fillna("", inplace=True)

# removing numbers nid
# df_nid['Pāli2'] = df_nid['Pāli1']
df_nid['Pāli1'] = df_nid['Pāli1'].str.replace('\d+', '')
df_nid['Pāli1'] = df_nid['Pāli1'].str.replace(' ', '')

# sort by frequency
df = df.sort_values(by=['count'], ascending = False)

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
df_time = df_time[['Pāli1', 'POS', 'Pattern', 'count']]
df_time.to_csv("frequent-words/adv_time.csv", sep="\t", index=None)

# find words in niddhi

test1 = df_nid['Pāli1'].isin(df_time['Pāli1'])
test2 = df_nid['POS'].isin(df_time['POS'])

logix = test1 & test2

df_time_dpd = df_nid[logix]

# merge frequency column
df_time_dpd = pd.merge(df_time_dpd, df_time, how='left')

# cleaning ex2
df_time_dpd['Source 2'] = ""
df_time_dpd['Sutta2'] = ""
df_time_dpd['Example 2'] = ""

# adding feedback
df_time_dpd.reset_index(drop=True, inplace=True)
df_time_dpd['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df_time_dpd.Pāli1 + """&entry.1433863141=Pāli Class Vocab">Fix it here</a>."""
df_time_dpd['marks'] = ""

# adding tag
df_time_dpd['Tag'] = df_time_dpd['Pattern']
df_time_dpd['Tag'] = df_time_dpd['Tag'].str.replace(' ', '-')

# choosing order of columns
df_time_dpd = df_time_dpd[['Pāli1', 'POS', 'Grammar', 'Derived from', 'Neg', 'Verb', 'Trans', 'Case', 'Meaning IN CONTEXT', 'Meaning in native language', 'Pāli Root', 'Base', 'Construction', 'Sanskrit', 'Sk Root', 'Source1', 'Sutta1', 'Example1', 'Source 2', 'Sutta2', 'Example 2', 'Stem', 'Pattern', 'count', 'Feedback', 'Tag', 'marks']]

df_time_dpd.to_csv("frequent-words/adv_time_dpd.csv", sep="\t", index=None)

# find if not

test1 = ~df_time['Pāli1'].isin(df_nid['Pāli1'])
# test2 = ~df_time['Pattern'].isin(df_nid['Pattern'])

logix = test1

df_absent = pd.DataFrame()

df_absent = pd.concat([df_absent, df_time[logix]])
# df_absent = df_absent df_class_1[logix]

# adding feedback ?
# df_absent.reset_index(drop=True, inplace=True)
df_absent['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform">Fix it here</a>."""


df_absent.to_csv(f"../spreadsheets/absent.csv", sep="\t", index=None)



df_place[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/adv_place.csv", sep="\t", index=None)

df_interr[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/adv_interr.csv", sep="\t", index=None)

# save friquent names
test3 = df['Grammar'] == "name"
filter = test3
df_name = df.loc[filter]

df_name[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/names.csv", sep="\t", index=None)

# keep original
df_orig = df

# filter not comp | comp vb | name
test1 = df_orig['Grammar'] != "comp"
test2 = df_orig['Grammar'] != "comp vb"
# test3 = df_orig['Grammar'] != "name"
filter = test1 & test2
df_orig = df_orig.loc[filter]

# filter what is done
df = df.head(1200)

# filter not comp | comp vb | name
test1 = df['Grammar'] != "comp"
test2 = df['Grammar'] != "comp vb"
# test3 = df['Grammar'] != "name"
filter = test1 & test2
df = df.loc[filter]

# save all done
df[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("curated-sources/frequent-words.csv", sep="\t", index=None)

# filter masc

test1 = df['POS'] == "masc"
test2 = df['Pattern'] == "a masc"
test3 = df['Pattern'] == "i masc"
test4 = df['Pattern'] == "ī masc"
test5 = df['Pattern'] == "u masc"
test6 = df['Pattern'] == "ar masc"
test7 = df['Pattern'] == "a masc east"
test8 = df['Pattern'] == "ū masc"

filter = test1 & test2
df_a_masc = df.loc[filter]

filter = test1 & test7
df_a_east_masc = df.loc[filter]

df_a_masc = pd.concat([df_a_masc, df_a_east_masc])
df_a_masc = df_a_masc.sort_values(by=['count'], ascending = False)
df_a_masc = df_a_masc.head(200)

filter = test1 & test3
df_i_masc = df.loc[filter]

test1 = df_orig['POS'] == "masc"
test4 = df_orig['Pattern'] == "ī masc"
filter = test1 & test4
df_ii_masc = df_orig.loc[filter]
df_ii_masc = df_ii_masc.head(10)

test1 = df_orig['POS'] == "masc"
test5 = df_orig['Pattern'] == "u masc"
filter = test1 & test5
df_u_masc = df_orig.loc[filter]
df_u_masc = df_u_masc.head(12)


test1 = df_orig['POS'] == "masc"
test6 = df_orig['Pattern'] == "ar masc"
filter = test1 & test6
df_ar_masc = df_orig.loc[filter]
df_ar_masc = df_ar_masc.head(10)

test1 = df_orig['POS'] == "masc"
test8 = df_orig['Pattern'] == "ū masc"

filter = test1 & test8
df_uu_masc = df_orig.loc[filter]
df_uu_masc = df_uu_masc.head(6)

# save masc csv

df_a_masc[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/masc-a.csv", sep="\t", index=None)

df_i_masc[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/masc-i.csv", sep="\t", index=None)

df_ii_masc[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/masc-ī.csv", sep="\t", index=None)

df_u_masc[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/masc-u.csv", sep="\t", index=None)

df_uu_masc[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/masc-ū.csv", sep="\t", index=None)

df_ar_masc[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/masc-ar.csv", sep="\t", index=None)

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
df_ant[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/masc-ant.csv", sep="\t", index=None)

# filter pr
test1 = df['POS'] == "pr"
test2 = df['Pattern'] == "ati pr"
test3 = df['Pattern'] == "eti pr"
test4 = df['Pattern'] == "āti pr"
test5 = df['Pattern'] == "oti pr"
test6 = df['Pattern'] == "karoti pr"
test7 = df['Pattern'] == "hoti pr"
test8 = df['Pattern'] == "atthi pr"
test9 = df['Pattern'] == "natthi pr"
# irreg pr
test10 = df['Pattern'] == "eti pr 2"
test11 = df['Pattern'] == "brūti pr"
test12 = df['Pattern'] == "dakkhati pr"
test13 = df['Pattern'] == "hanati pr"
test14 = df['Pattern'] == "kubbati pr"

filter = test1 & test2
df_ati_pr = df.loc[filter]
df_ati_pr = df_ati_pr.head(100)

filter = test1 & test3
df_eti_pr = df.loc[filter]

filter = test1 & test4
df_aati_pr = df.loc[filter]

filter = test1 & test5
df_oti_pr = df.loc[filter]

filter = test1 & test6
df_karoti = df.loc[filter]

df_oti_pr = pd.concat([df_oti_pr, df_karoti])
df_oti_pr = df_oti_pr.sort_values(by=['count'], ascending = False)

filter = test1 & test7
df_hoti = df.loc[filter]

filter = test1 & test8
df_atthi = df.loc[filter]

filter = test1 & test9
df_natthi = df.loc[filter]

df_be_pr = pd.concat([df_hoti, df_atthi, df_natthi])
df_be_pr = df_be_pr.sort_values(by=['count'], ascending = False)

# save pr csv

df_ati_pr[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/pr-ati.csv", sep="\t", index=None)

df_eti_pr[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/pr-eti.csv", sep="\t", index=None)

df_aati_pr[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/pr-āti.csv", sep="\t", index=None)

df_oti_pr[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/pr-oti.csv", sep="\t", index=None)

df_be_pr[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/pr-be.csv", sep="\t", index=None)

# filter other pr
test1 = df['POS'] == "pr"
test2 = df['Pattern'] != "āti pr"
test3 = df['Pattern'] != "eti pr"
test4 = df['Pattern'] != "ati pr"
test5 = df['Pattern'] != "oti pr"
test6 = df['Pattern'] != "karoti pr"
test7 = df['Pattern'] != "hoti pr"
test8 = df['Pattern'] != "atthi pr"
test9 = df['Pattern'] != "natthi pr"

filter = test1 & test2 & test3 & test4 & test5 & test6 & test7 & test8 & test9
df_other_pr = df.loc[filter]

# save other pr csv
df_other_pr[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/pr-other.csv", sep="\t", index=None)

# filter aor
test1 = df['POS'] == "aor"
test2 = df['Pattern'] == "i aor"
test3 = df['Pattern'] == "esi aor"
test4 = df['Pattern'] == "āsi aor"
test5 = df['Pattern'] == "i aor isuṃ"
test6 = df['Pattern'] == "āsi aor iṃsu"
test7 = df['Pattern'] == "ahosi aor"
test8 = df['Pattern'] == "āsi aor irreg"
test9 = df['Pattern'] == "hari aor"
# irreg aor
test10 = df['Pattern'] == "avoca aor"
test11 = df['Pattern'] == "assosi aor"
test12 = df['Pattern'] == "ddasa aor"

filter = test1 & test2
df_i_aor = df.loc[filter]

filter = test1 & test9
df_hari = df.loc[filter]

filter = test1 & test5
df_i_aor_is = df.loc[filter]

df_i_aor = pd.concat([df_i_aor, df_i_aor_is, df_hari])
df_i_aor = df_i_aor.sort_values(by=['count'], ascending = False)

test1 = df_orig['POS'] == "aor"
test3 = df_orig['Pattern'] == "esi aor"
filter = test1 & test3
df_esi_aor = df_orig.loc[filter]
df_esi_aor = df_esi_aor.head(10)

filter = test1 & test4
df_aasi_aor = df.loc[filter]

filter = test1 & test6
df_aasi_im_aor = df.loc[filter]

df_aasi_aor = pd.concat([df_aasi_aor, df_aasi_im_aor])
df_aasi_aor = df_aasi_aor.sort_values(by=['count'], ascending = False)

filter = test1 & test7
df_ahosi = df.loc[filter]

filter = test1 & test8
df_aasi = df.loc[filter]

df_be_aor = pd.concat([df_aasi, df_ahosi])
df_be_aor = df_be_aor.sort_values(by=['count'], ascending = False)

# save aor
df_i_aor[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/aor-i.csv", sep="\t", index=None)

df_esi_aor[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/aor-esi.csv", sep="\t", index=None)

df_aasi_aor[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/aor-āsi.csv", sep="\t", index=None)

df_be_aor[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/aor-be.csv", sep="\t", index=None)

# filter other aor
test1 = df['POS'] == "aor"
test2 = df['Pattern'] != "i aor"
test3 = df['Pattern'] != "esi aor"
test4 = df['Pattern'] != "āsi aor"
test5 = df['Pattern'] != "i aor isuṃ"
test6 = df['Pattern'] != "āsi aor iṃsu"
test7 = df['Pattern'] != "ahosi aor"
test8 = df['Pattern'] != "āsi aor irreg"
test9 = df['Pattern'] != "hari aor"

filter = test1 & test2 & test3 & test4 & test5 & test6 & test7 & test8 & test9
df_other_aor = df.loc[filter]

# save other aor csv
df_other_aor[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/aor-other.csv", sep="\t", index=None)

# filter pers pron
test1 = df['POS'] == "pron"
test2 = df['Pattern'] == "ahaṃ pron"
test3 = df['Pattern'] == "tvaṃ pron"

filter = test1 & test2
df_1_pron = df.loc[filter]

filter = test1 & test3
df_2_pron = df.loc[filter]

df_pers_pron = pd.concat([df_1_pron, df_2_pron])

# save 1&2 pron
df_pers_pron[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/pron_pers.csv", sep="\t", index=None)

# filter other aor
test1 = df['POS'] == "pron"
test2 = df['Pattern'] != "ahaṃ pron"
test3 = df['Pattern'] != "tvaṃ pron"

filter = test1 & test2 & test3
df_other_pron = df.loc[filter]

# save other aor csv
df_other_pron[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/other-pron.csv", sep="\t", index=None)

# filter fut
test1 = df_orig['POS'] == "fut"
test2 = df_orig['Grammar'] != "irreg"
filter = test1
df_fut = df_orig.loc[filter]
df_fut = df_fut.head(25)

# save fut csv
df_fut[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/fut.csv", sep="\t", index=None)

# save summary csv
df_summary = pd.concat([df_a_masc, df_ati_pr, df_eti_pr, df_aati_pr, df_oti_pr, df_be_pr, df_i_masc, df_i_aor, df_be_aor, df_esi_aor, df_pers_pron, df_fut, df_ii_masc, df_u_masc, df_ar_masc, df_ant, df_uu_masc, df_time])
df_summary = df_summary.sort_values(by=['count'], ascending = False)


df_summary[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/summary.csv", sep="\t", index=None)

# print lenght

a_masc_l = len(df_a_masc)
print(f"lenght a_masc {a_masc_l}")

ati_pr_l = len(df_ati_pr)
print(f"lenght ati_pr {ati_pr_l}")

eti_pr_l = len(df_eti_pr)
print(f"lenght eti_pr {eti_pr_l}")

aati_pr_l = len(df_aati_pr)
print(f"lenght āti_pr {aati_pr_l}")

oti_pr_l = len(df_oti_pr)
print(f"lenght oti_pr {oti_pr_l}")

be_pr_l = len(df_be_pr)
print(f"lenght be_pr {be_pr_l}")

i_masc_l = len(df_i_masc)
print(f"lenght i_masc {i_masc_l}")

i_aor_l = len(df_i_aor)
print(f"lenght i_aor {i_aor_l}")

be_aor_l = len(df_be_aor)
print(f"lenght be_aor {be_aor_l}")

esi_aor_l = len(df_esi_aor)
print(f"lenght esi_aor {esi_aor_l}")

pers_pron_l = len(df_pers_pron)
print(f"lenght pers_pron {pers_pron_l}")

fut_l = len(df_fut)
print(f"lenght fut {fut_l}")

ii_masc_l = len(df_ii_masc)
print(f"lenght ī_masc {ii_masc_l}")

u_masc_l = len(df_u_masc)
print(f"lenght u_masc {u_masc_l}")

ar_masc_l = len(df_ar_masc)
print(f"lenght ar_masc {ar_masc_l}")

ant_l = len(df_ant)
print(f"lenght ant {ant_l}")

uu_masc_l = len(df_uu_masc)
print(f"lenght ū_masc {uu_masc_l}")

adv_time_l = len(df_time)
print(f"lenght adv_time {adv_time_l}")

# save comp for 1 class
df_comb_1 = pd.concat([df_a_masc])
df_comb_1 = df_comb_1.sort_values(by=['count'], ascending = False)

df_comb_1[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("csv-for-classes/class-1.csv", sep="\t", index=None)

# save comp for 2 class
df_comb_2 = pd.concat([df_ati_pr, df_eti_pr, df_aati_pr, df_oti_pr])
df_comb_2 = df_comb_2.sort_values(by=['count'], ascending = False)

df_comb_2[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("csv-for-classes/class-2.csv", sep="\t", index=None)

# save comp for 3 class
df_comb_3 = pd.concat([df_be_pr, df_i_masc, df_i_aor, df_be_aor, df_esi_aor])
df_comb_3 = df_comb_3.sort_values(by=['count'], ascending = False)

df_comb_3[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("csv-for-classes/class-3.csv", sep="\t", index=None)

# save comp for 4 class
df_comb_4 = pd.concat([df_pers_pron, df_fut, df_ii_masc])
df_comb_4 = df_comb_4.sort_values(by=['count'], ascending = False)

df_comb_4[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("csv-for-classes/class-4.csv", sep="\t", index=None)

# save comp for 5 class
df_comb_5 = pd.concat([df_u_masc, df_ar_masc, df_ant, df_uu_masc, df_time])
df_comb_5 = df_comb_5.sort_values(by=['count'], ascending = False)

df_comb_5[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("csv-for-classes/class-5.csv", sep="\t", index=None)
