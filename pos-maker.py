import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
from natsort import index_natsorted

df = pd.read_csv("../pāli-course/frequent-words.ods-words.csv", sep="\t", dtype= str)
df.fillna("")

# df = read_ods("../pāli-course/frequent-words.ods")
# df.fillna("")
# df = df.astype(str)
# df = df.replace(to_replace ="\.0", value = "", regex = True) #removes all flaots .0

# sort by frequency
df.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df['count'])))

# keep original
df_orig = df

# filter what is done
df = df.head(3100)

# save all what is done
df[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/frequent-words.csv", sep="\t", index=None)

#filter adv
test1 = df_orig['pos'] == "ind"
test2 = df_orig['grammar'] == "time"
test3 = df_orig['grammar'] == "place"
test4 = df_orig['grammar'] == "interr"
test5 = df_orig['grammar'] == "neg"
test6 = df_orig['grammar'] == "with"

filter = test1 & test2
df_time = df_orig.loc[filter]

filter = test1 & test3
df_place = df_orig.loc[filter]

filter = test1 & test4
df_interr = df_orig.loc[filter]

filter = test1 & test5
df_neg = df_orig.loc[filter]

filter = test1 & test6
df_with = df_orig.loc[filter]

# save adv csv
df_time = df_time[['pali_1', 'pos', 'pattern', 'count']]
df_time.to_csv("csv-all-pos/adv_time.csv", sep="\t", index=None)

df_place = df_place[['pali_1', 'pos', 'pattern', 'count']]
df_place.to_csv("csv-all-pos/adv_place.csv", sep="\t", index=None)

df_interr = df_interr[['pali_1', 'pos', 'pattern', 'count']]
df_interr.to_csv("csv-all-pos/adv_interr.csv", sep="\t", index=None)

df_neg = df_neg[['pali_1', 'pos', 'pattern', 'count']]
df_neg.to_csv("csv-all-pos/ind_neg.csv", sep="\t", index=None)

df_with = df_with[['pali_1', 'pos', 'pattern', 'count']]
df_with.to_csv("csv-all-pos/ind_with.csv", sep="\t", index=None)

# save friquent names
test3 = df_orig['grammar'] == "name"
filter = test3
df_name = df_orig.loc[filter]

df_name[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/names.csv", sep="\t", index=None)

# filter not comp | comp vb | name
test1 = df_orig['grammar'] != "comp"
test2 = df_orig['grammar'] != "comp vb"
test3 = df_orig['grammar'] != "desid"
# test3 = df_orig['grammar'] != "name"
filter = test1 & test2 & test3
df_orig = df_orig.loc[filter]

# filter not comp | comp vb | name
test1 = df['grammar'] != "comp"
test3 = df_orig['grammar'] != "desid"
# test3 = df_orig['grammar'] != "name"
filter = test1 & test2 & test3
df = df.loc[filter]

# filter masc

test1 = df['pos'] == "masc"
test2 = df['pattern'] == "a masc"
test3 = df['pattern'] == "i masc"
test4 = df['pattern'] == "a masc pl"

test9 = df['pattern'] == "ar2 masc"

test10 = df['grammar'] != "dat"
test11 = df['grammar'] != "neg"
# pass and caus
test15 = df['grammar'] != "pass"
test16 = df['grammar'] != "caus"
test17 = df['grammar'] != "irreg"
test18 = df['grammar'] != "neg"

filter = test1 & test2 & test10 & test11 & test16
df_a_masc = df.loc[filter]

filter = test1 & test4 & test10 & test11 & test16
df_a_masc_pl = df.loc[filter]

df_a_masc = pd.concat([df_a_masc, df_a_masc_pl])
df_a_masc.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_a_masc['count'])))

filter = test1 & test3 & test11
df_i_masc = df.loc[filter]

test1 = df_orig['pos'] == "masc"

test4 = df_orig['pattern'] == "ī masc"
test5 = df_orig['pattern'] == "u masc"
test6 = df_orig['pattern'] == "ar masc"
test7 = df_orig['pattern'] == "ū masc"
test10 = df_orig['pattern'] == "ar2 masc"

filter = test1 & test4
df_ii_masc = df_orig.loc[filter]
# df_ii_masc = df_ii_masc.head(14)


test8 = df_orig['grammar'] == "masc"
test9 = df_orig['pattern'] == "ī adj"
filter = test8 & test9
df_ii_adj = df_orig.loc[filter]

df_ii_masc = pd.concat([df_ii_masc, df_ii_adj])
df_ii_masc.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_ii_masc['count'])))

filter = test1 & test5
df_u_masc = df_orig.loc[filter]

filter = test1 & test6
df_ar_masc = df_orig.loc[filter]

filter = test1 & test10
df_ar2_masc = df_orig.loc[filter]

filter = test1 & test7
df_uu_masc = df_orig.loc[filter]


test8 = df_orig['grammar'] == "masc"
test9 = df_orig['pattern'] == "ū adj"
filter = test8 & test9
df_uu_adj = df_orig.loc[filter]

df_uu_masc = pd.concat([df_uu_masc, df_uu_adj])
df_uu_masc.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_uu_masc['count'])))



# save masc csv

df_a_masc[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/masc-a.csv", sep="\t", index=None)

df_i_masc[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/masc-i.csv", sep="\t", index=None)

df_ii_masc[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/masc-ī.csv", sep="\t", index=None)

df_u_masc[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/masc-u.csv", sep="\t", index=None)

df_uu_masc[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/masc-ū.csv", sep="\t", index=None)

df_ar_masc[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/masc-ar.csv", sep="\t", index=None)

df_ar2_masc[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/masc-ar2.csv", sep="\t", index=None)

# filter ant adj
test1 = df_orig['pos'] == "adj"
test2 = df_orig['pattern'] == "ant adj"
filter = test1 & test2
df_ant_adj = df_orig.loc[filter]

# filter ant masc
test1 = df_orig['pos'] == "masc"
test2 = df_orig['pattern'] == "ant masc"
filter = test1 & test2
df_ant_masc = df_orig.loc[filter]

#combine ant
df_ant = pd.concat([df_ant_adj, df_ant_masc])
df_ant.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_ant['count'])))

df_ant = df_ant.head(25)

# save ant csv
df_ant[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/masc-ant.csv", sep="\t", index=None)

# filter pr
test1 = df['pos'] == "pr"
test2 = df['pattern'] == "ati pr"
test3 = df['pattern'] == "eti pr"
test4 = df['pattern'] == "āti pr"
test5 = df['pattern'] == "oti pr"
test6 = df['pattern'] == "karoti pr"
test7 = df['pattern'] == "hoti pr"
test8 = df['pattern'] == "atthi pr"
# test9 = df['pattern'] == "natthi pr"
# irreg pr
test10 = df['pattern'] == "eti pr 2"
test11 = df['pattern'] == "brūti pr"
test12 = df['pattern'] == "dakkhati pr"
test13 = df['pattern'] == "hanati pr"
test14 = df['pattern'] == "kubbati pr"
# pass and caus pr
test15 = df['grammar'] != "pass"
test16 = df['grammar'] != "caus"
test17 = df['grammar'] != "caus, pass"
test18 = df['grammar'] != "irreg"
test19 = df['grammar'] != "neg"
test20 = df['grammar'] != "4"

filter = test1 & test2 & test15 & test16 & test17 & test18 & test19 & test20
df_ati_pr = df.loc[filter]


filter = test1 & test3 & test15 & test16 & test17 & test18 & test19 & test20
df_eti_pr = df.loc[filter]

test10 = df['pattern'] == "eti pr 2"
filter = test1 & test10 & test20
df_eti_2_pr = df.loc[filter]

df_eti_pr = pd.concat([df_eti_pr, df_eti_2_pr])
df_eti_pr.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_eti_pr['count'])))



filter = test1 & test4 & test15 & test16 & test17 & test18 & test19 & test20
df_aati_pr = df.loc[filter]

filter = test1 & test5 & test15 & test16 & test17 & test18 & test19 & test20
df_oti_pr = df.loc[filter]

filter = test1 & test6 & test15 & test16 & test17 & test18 & test19 & test20
df_karoti = df.loc[filter]

df_oti_pr = pd.concat([df_oti_pr, df_karoti])
df_oti_pr.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_oti_pr['count'])))


df_pr = pd.concat([df_ati_pr, df_eti_pr, df_aati_pr, df_oti_pr])

test2 = df_pr['root_pali'].str.contains('1|4|5|6|8')
test3 = df_pr['root_pali'].str.contains('2|3|7')
filter = test2
df_pr_3 = df_pr.loc[filter]
filter = test3
df_pr_4 = df_pr.loc[filter]

filter = test1 & test7 & test20
df_hoti = df.loc[filter]

filter = test1 & test8 & test20
df_atthi = df.loc[filter]

df_be_pr = pd.concat([df_hoti, df_atthi])
df_be_pr.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_be_pr['count'])))


# save pr csv

df_ati_pr[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/pr-ati.csv", sep="\t", index=None)

df_eti_pr[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/pr-eti.csv", sep="\t", index=None)

df_aati_pr[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/pr-āti.csv", sep="\t", index=None)

df_oti_pr[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/pr-oti.csv", sep="\t", index=None)

df_be_pr[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/pr-be.csv", sep="\t", index=None)

# filter other pr
test1 = df['pos'] == "pr"
test2 = df['pattern'] != "āti pr"
test3 = df['pattern'] != "eti pr"
test4 = df['pattern'] != "ati pr"
test5 = df['pattern'] != "oti pr"
test6 = df['pattern'] != "karoti pr"
test7 = df['pattern'] != "hoti pr"
test8 = df['pattern'] != "atthi pr"
test9 = df['pattern'] != "natthi pr"

filter = test1 & test2 & test3 & test4 & test5 & test6 & test7 & test8 & test9
df_other_pr = df.loc[filter]

# save other pr csv
df_other_pr[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/pr-other.csv", sep="\t", index=None)


# filter imp
test1 = df_orig['pos'] == "imp"
# pass and caus imp
test15 = df_orig['grammar'] != "pass"
test16 = df_orig['grammar'] != "caus"
test17 = df_orig['grammar'] != "caus, pass"
test18 = df_orig['grammar'] != "irreg"
test19 = df_orig['grammar'] != "neg"
test20 = df_orig['grammar'] != "reflx"
test21 = df_orig['grammar'] != "be"
test22 = df_orig['grammar'] != "4"

filter = test1 & test15 & test16 & test17 & test18 & test19 & test20 & test21 & test22
df_imp = df_orig.loc[filter]

test2 = df_imp['root_pali'].str.contains('1|4|5|6|8')
test3 = df_imp['root_pali'].str.contains('2|3|7')
filter = test2
df_imp_3 = df_imp.loc[filter]
filter = test3
df_imp_4 = df_imp.loc[filter]

test1 = df_orig['pos'] == "imp"
test21 = df_orig['grammar'] == "be"
filter = test1 & test21 & test22
df_be_imp = df_orig.loc[filter]

# save imp csv
df_imp[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/imp.csv", sep="\t", index=None)

# filter aor
test1 = df['pos'] == "aor"
test2 = df['pattern'] == "i aor"

test7 = df['pattern'] == "ahosi aor"
test8 = df['pattern'] == "āsi aor irreg"

test9 = df['pattern'] == "hari aor"
# irreg aor
test10 = df['pattern'] == "avoca aor"
test11 = df['pattern'] == "assosi aor"
test12 = df['pattern'] == "ddasa aor"
# pass and caus aor
test15 = df['grammar'] != "pass"
test16 = df['grammar'] != "caus"
test17 = df['grammar'] != "irreg"
test18 = df['grammar'] != "neg"
test19 = df['grammar'] != "4"
test20 = df['grammar'] != "5"

filter = test1 & test2 & test15 & test16 & test17 & test18 & test19 & test20
df_i_aor = df.loc[filter]


filter = test1 & test9 & test15 & test16 & test17 & test18 & test19 & test20
df_hari = df.loc[filter]

df_i_aor = pd.concat([df_i_aor, df_hari])
df_i_aor.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_i_aor['count'])))

filter = test1 & test7 & test15 & test16 & test17 & test19 & test20
df_ahosi = df.loc[filter]

filter = test1 & test8 & test15 & test16 & test17 & test19 & test20
df_aasi = df.loc[filter]

df_be_aor = pd.concat([df_aasi, df_ahosi])
df_be_aor.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_be_aor['count'])))

test1 = df_orig['pos'] == "aor"
test3 = df_orig['pattern'] == "esi aor"
test4 = df_orig['pattern'] == "āsi aor"
# pass and caus aor
test15 = df_orig['grammar'] != "pass"
test16 = df_orig['grammar'] != "caus"
test17 = df_orig['grammar'] != "irreg"
test18 = df_orig['grammar'] != "neg"
test19 = df_orig['grammar'] != "4"
test20 = df_orig['grammar'] != "5"

filter = test1 & test3 & test15 & test16 & test17 & test18 & test19 & test20
df_esi_aor = df_orig.loc[filter]
df_esi_aor = df_esi_aor.head(6)

filter = test1 & test4 & test15 & test16 & test17 & test18 & test19 & test20
df_aasi_aor = df_orig.loc[filter]
df_aasi_aor = df_aasi_aor.head(10)

# save aor
df_i_aor[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/aor-i.csv", sep="\t", index=None)

df_esi_aor[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/aor-esi.csv", sep="\t", index=None)

df_aasi_aor[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/aor-āsi.csv", sep="\t", index=None)

df_be_aor[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/aor-be.csv", sep="\t", index=None)

# filter other aor
test1 = df['pos'] == "aor"
test2 = df['pattern'] != "i aor"
test3 = df['pattern'] != "esi aor"
test4 = df['pattern'] != "āsi aor"
test5 = df['pattern'] != "i aor isuṃ"
test6 = df['pattern'] != "āsi aor iṃsu"
test7 = df['pattern'] != "ahosi aor"
test8 = df['pattern'] != "āsi aor irreg"
test9 = df['pattern'] != "hari aor"

filter = test1 & test2 & test3 & test4 & test5 & test6 & test7 & test8 & test9
df_other_aor = df.loc[filter]

# save other aor csv
df_other_aor[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/aor-other.csv", sep="\t", index=None)

# filter pers pron
test1 = df['pos'] == "pron"
test2 = df['pattern'] == "ahaṃ pron"
test3 = df['pattern'] == "tvaṃ pron"

filter = test1 & test2
df_1_pron = df.loc[filter]

filter = test1 & test3
df_2_pron = df.loc[filter]

df_pers_pron = pd.concat([df_1_pron, df_2_pron])

# save 1&2 pron
df_pers_pron[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/pron_pers.csv", sep="\t", index=None)

# filter other aor
test1 = df['pos'] == "pron"
test2 = df['pattern'] != "ahaṃ pron"
test3 = df['pattern'] != "tvaṃ pron"

filter = test1 & test2 & test3
df_other_pron = df.loc[filter]

# save other aor csv
df_other_pron[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/other-pron.csv", sep="\t", index=None)

# filter fut
test1 = df_orig['pos'] == "fut"
# pass and caus fut
test15 = df_orig['grammar'] != "pass"
test16 = df_orig['grammar'] != "caus"
test17 = df_orig['grammar'] != "irreg"
test18 = df_orig['grammar'] != "neg"
filter = test1 & test15 & test16 & test17 & test18
df_fut = df_orig.loc[filter]
df_fut = df_fut.head(25)

# save fut csv
df_fut[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/fut.csv", sep="\t", index=None)

# filter pr and masc neg
test1 = df['pos'] != "ind"
test2 = df['grammar'] == "neg"
filter = test1 & test2
df_neg_5 = df.loc[filter]

# save fut csv
df_neg_5[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/neg-4cl.csv", sep="\t", index=None)


# filter fem

test1 = df['pos'] == "fem"
test2 = df['pattern'] == "ā fem"
test3 = df['pattern'] == "i fem"

# pass and caus
test15 = df['grammar'] != "pass"
test16 = df['grammar'] != "caus"
test17 = df['grammar'] != "irreg"
test18 = df['grammar'] != "neg"

filter = test1 & test2 & test16
df_aa_fem = df.loc[filter]


filter = test1 & test3 & test16
df_i_fem = df.loc[filter]


test1 = df_orig['pos'] == "fem"
test4 = df_orig['pattern'] == "ī fem"
test5 = df_orig['pattern'] == "u fem"
test6 = df_orig['pattern'] == "ar fem"
test7 = df_orig['pattern'] == "ū fem"

filter = test1 & test4
df_ii_fem = df_orig.loc[filter]
df_ii_fem = df_ii_fem.head(15)

filter = test1 & test5
df_u_fem = df_orig.loc[filter]


filter = test1 & test6
df_ar_fem = df_orig.loc[filter]
df_ar_fem = df_ar_fem.head(10)

filter = test1 & test7
df_uu_fem = df_orig.loc[filter]


# save fem csv

df_aa_fem[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/fem-ā.csv", sep="\t", index=None)

df_i_fem[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/fem-i.csv", sep="\t", index=None)

df_ii_fem[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/fem-ī.csv", sep="\t", index=None)

df_u_fem[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/fem-u.csv", sep="\t", index=None)

df_uu_fem[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/fem-ū.csv", sep="\t", index=None)

df_ar_fem[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/fem-ar.csv", sep="\t", index=None)


# filter nt

test1 = df['pos'] == "nt"
test2 = df['pattern'] == "a nt"

test10 = df['grammar'] != "dat"

filter = test1 & test2 & test10
df_a_nt = df.loc[filter]


test1 = df_orig['pos'] == "nt"
test3 = df_orig['pattern'] == "i nt"
test4 = df_orig['pattern'] == "u nt"

filter = test1 & test3
df_i_nt = df_orig.loc[filter]

filter = test1 & test4
df_u_nt = df_orig.loc[filter]



# save nt csv

df_a_nt[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/nt-a.csv", sep="\t", index=None)

df_i_nt[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/nt-i.csv", sep="\t", index=None)

df_u_nt[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/nt-u.csv", sep="\t", index=None)

# filter inf
test1 = df_orig['pos'] == "inf"
test2 = df_orig['grammar'] != "irreg"
# pass and caus
test15 = df['grammar'] != "pass"
test16 = df['grammar'] != "caus"
test17 = df['grammar'] != "irreg"
test18 = df['grammar'] != "neg"

filter = test1 & test15 & test16
df_inf = df_orig.loc[filter]
df_inf = df_inf.head(40)

# save inf csv
df_inf[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/inf.csv", sep="\t", index=None)

# filter +inf
test2 = df_orig['grammar'] == "+inf"
filter = test2
df_plus_inf = df_orig.loc[filter]


# save +inf csv
df_plus_inf[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/+inf.csv", sep="\t", index=None)

# filter inf kāma
test2 = df_orig['grammar'] == "inf kāma"
filter = test2
df_inf_kam = df_orig.loc[filter]


# save inf kāma
df_inf_kam[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/inf-kāma.csv", sep="\t", index=None)

# filter dat of purpose
test2 = df_orig['grammar'] == "dat"
filter = test2
df_dat = df_orig.loc[filter]


# save dat of purpose
df_dat[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/dat.csv", sep="\t", index=None)

# filter until-then
test2 = df['grammar'] == "until-then"
filter = test2
df_until = df.loc[filter]

# save until-then
df_until[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/until-then.csv", sep="\t", index=None)



# filter opt
test1 = df['pos'] == "opt"
test2 = df['pattern'] == "eyya opt"
test3 = df['pattern'] == "ssa opt"
test4 = df['pattern'] == "siyā opt"

filter = test1 & test2
df_opt = df.loc[filter]

filter = test1 & test3
df_opt_ssa = df.loc[filter]

filter = test1 & test4
df_opt_siya = df.loc[filter]
df_opt_be = pd.concat([df_opt_ssa, df_opt_siya])

# save opt
df_opt[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/opt.csv", sep="\t", index=None)

df_opt_be[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/opt-be.csv", sep="\t", index=None)

# filter ger and abs
test1 = df['pos'] == "ger"
test2 = df['pos'] == "abs"
# pass and caus
test15 = df['grammar'] != "pass"
test16 = df['grammar'] != "caus"
test17 = df['grammar'] != "irreg"
test18 = df['grammar'] != "neg"

filter = test1 & test15 & test16
df_ger = df.loc[filter]

filter = test2 & test15 & test16
df_abs = df.loc[filter]

# save ger and abs
df_ger[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/ger.csv", sep="\t", index=None)

df_abs[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/abs.csv", sep="\t", index=None)


# filter prp
test1 = df['pos'] == "prp"
test2 = df['pattern'] == "anta prp"
test3 = df['pattern'] == "māna prp"
# pass and caus prp
test15 = df['grammar'] != "pass"
test16 = df['grammar'] != "caus"
test17 = df['grammar'] != "caus, pass"
test18 = df['grammar'] != "irreg"

filter = test1 & test2 & test15 & test16 & test17 & test18
df_anta_prp = df.loc[filter]


filter = test1 & test3 & test15 & test16 & test17 & test18
df_mana_prp = df.loc[filter]

test1 = df_orig['pos'] == "prp"
test4 = df_orig['pattern'] == "enta prp"
test5 = df_orig['pattern'] == "onta prp"
test6 = df_orig['pattern'] == "āna prp"
# pass and caus prp
test15 = df_orig['grammar'] != "pass"
test16 = df_orig['grammar'] != "caus"
test17 = df_orig['grammar'] != "caus, pass"
test18 = df_orig['grammar'] != "irreg"


filter = test1 & test4 & test15 & test16 & test17 & test18
df_enta_prp = df_orig.loc[filter]
df_enta_prp = df_enta_prp.head(20)

filter = test1 & test5 & test15 & test16 & test17 & test18
df_onta_prp = df_orig.loc[filter]
df_onta_prp = df_onta_prp.head(20)

filter = test1 & test6 & test15 & test16 & test17 & test18
df_ana_prp = df_orig.loc[filter]

# save prp csv

df_anta_prp[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/prp-anta.csv", sep="\t", index=None)

df_mana_prp[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/prp-māna.csv", sep="\t", index=None)

df_enta_prp[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/prp-enta.csv", sep="\t", index=None)

df_onta_prp[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/prp-onta.csv", sep="\t", index=None)

df_ana_prp[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/pr-āna.csv", sep="\t", index=None)

# filter def-art aññatara
test1 = df['grammar'] == "def-art"

filter = test1
df_def = df.loc[filter]

# filter pron
test1 = df['pos'] == "pron"
test2 = df['pattern'] != "tvaṃ pron"
test3 = df['pattern'] != "ahaṃ pron"
test4 = df['grammar'] != "until-then"
test5 = df['grammar'] != "interr"

filter = test1 & test2 & test3 & test4 & test5
df_pron = df.loc[filter]

df_pron[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/pron.csv", sep="\t", index=None)

# filter pp
test1 = df['pos'] == "pp"
# pass and caus pr
test15 = df['grammar'] != "pass"
test16 = df['grammar'] != "caus"
test17 = df['grammar'] != "caus, pass"
test18 = df['grammar'] != "irreg"

filter = test1 & test15 & test16 & test17 & test18
df_pp = df.loc[filter]


df_pp[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/pp.csv", sep="\t", index=None)

# filter adj
test1 = df['pos'] == "adj"
test2 = df['grammar'] != "def-art"
test3 = df['grammar'] != "+inf"
test4 = df['grammar'] != "inf kāma"
test5 = df['pattern'] != "ant adj"
test6 = df['grammar'] != "masc"

filter = test1 & test2 & test3 & test4 & test5 & test6
df_adj = df.loc[filter]


df_adj[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/adj.csv", sep="\t", index=None)

# filter abl of separation
test1 = df_orig['grammar'] == "abl"
filter = test1
df_abl = df_orig.loc[filter]


df_abl[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/abl.csv", sep="\t", index=None)

# filter numbers
test1 = df['pos'] == "card"
test2 = df['pos'] == "ordin"

filter = test1
df_card = df.loc[filter]

filter = test2
df_ordin = df.loc[filter]

df_card[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/card.csv", sep="\t", index=None)
df_ordin[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/ordin.csv", sep="\t", index=None)

# filter money
test1 = df['grammar'] == "money"

filter = test1
df_money = df.loc[filter]

df_money[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/money.csv", sep="\t", index=None)

# filter adv
test1 = df_orig['pos'] == "ind"
test2 = df_orig['grammar'] == "dhā"
test3 = df_orig['grammar'] == "so"
test4 = df_orig['grammar'] == "khattuṃ"
test5 = df_orig['grammar'] == "thaṃ"
test6 = df_orig['grammar'] == "to"
test7 = df_orig['grammar'] == "tra"
test8 = df_orig['grammar'] == "thā"
test9 = df_orig['grammar'] == "pure"

filter = test1 & test2
df_adv_dhā = df_orig.loc[filter]

filter = test1 & test3
df_adv_so = df_orig.loc[filter]

filter = test1 & test4
df_adv_khattum = df_orig.loc[filter]

filter = test1 & test5
df_adv_tham = df_orig.loc[filter]

filter = test1 & test6
df_adv_to = df_orig.loc[filter]

filter = test1 & test7
df_adv_tra = df_orig.loc[filter]

filter = test1 & test8
df_adv_tha = df_orig.loc[filter]

filter = test1 & test9
df_adv_pure = df_orig.loc[filter]

test1 = df['pos'] == "ind"
test2 = df['grammar'] == "adv"

filter = test1 & test2
df_adv_adv = df.loc[filter]


df_adv_dhā[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/adv-dhā.csv", sep="\t", index=None)
df_adv_so[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/adv-so.csv", sep="\t", index=None)
df_adv_khattum[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/adv-khattuṃ.csv", sep="\t", index=None)
df_adv_tham[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/adv-thaṃ.csv", sep="\t", index=None)
df_adv_to[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/adv-to.csv", sep="\t", index=None)
df_adv_tra[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/adv-tra.csv", sep="\t", index=None)
df_adv_tha[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/adv-thā.csv", sep="\t", index=None)
df_adv_pure[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/adv-pure.csv", sep="\t", index=None)
df_adv_adv[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/adv-adv.csv", sep="\t", index=None)

df_adv = pd.concat([df_adv_dhā, df_adv_so, df_adv_khattum, df_adv_tham, df_adv_to, df_adv_tra, df_adv_tha, df_adv_pure, df_adv_adv])
df_adv.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_adv['count'])))

df_adv[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/adv.csv", sep="\t", index=None)

# filter pass
test1 = df['grammar'] == "pass"
test2 = df['pos'] != "prp"

filter = test1 & test2
df_pass = df.loc[filter]

df_pass[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/pass.csv", sep="\t", index=None)

# filter caus
test1 = df['grammar'] == "caus"

filter = test1
df_caus = df.loc[filter]

df_caus[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/caus.csv", sep="\t", index=None)

# filter caus pass
test1 = df_orig['grammar'] == "caus, pass"
test2 = df_orig['pos'] == "pr"
test3 = df_orig['pos'] == "prp"

filter = test1 & test2
df_caus_pass_pr = df_orig.loc[filter]

filter = test1 & test3
df_caus_pass_prp = df_orig.loc[filter]
df_caus_pass_prp = df_caus_pass_prp.head(5)

df_caus_pass_prp[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/prp-caus-pass.csv", sep="\t", index=None)
df_caus_pass_pr[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/pr-caus-pass.csv", sep="\t", index=None)

# filter pass prp
test1 = df_orig['grammar'] == "pass"
test2 = df_orig['pos'] == "prp"

filter = test1 & test2
df_pass_prp = df_orig.loc[filter]
df_pass_prp = df_pass_prp.head(10)

df_pass_prp[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/prp-pass.csv", sep="\t", index=None)

# filter ptp
test1 = df['pos'] == "ptp"
test2 = df['grammar'] != "caus"
test3 = df['grammar'] != "pass"

filter = test1 & test2 & test3
df_ptp = df.loc[filter]


df_ptp[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/ptp.csv", sep="\t", index=None)

# extra words for class 2
test1 = df_orig['grammar'] == "2"
filter = test1
df_extra2 = df_orig.loc[filter]

# extra words for class 3
test1 = df_orig['grammar'] == "3"
filter = test1
df_extra3 = df_orig.loc[filter]

# extra words for class 4
test1 = df_orig['grammar'] == "4"
filter = test1
df_extra4 = df_orig.loc[filter]

# extra words for class 5
test1 = df_orig['grammar'] == "5"
filter = test1
df_extra5 = df_orig.loc[filter]

# extra words for class 6
test1 = df_orig['grammar'] == "6"
filter = test1
df_extra6 = df_orig.loc[filter]

# extra words for class 7
test1 = df_orig['grammar'] == "7"
filter = test1
df_extra7 = df_orig.loc[filter]

# extra words for class 8
test1 = df_orig['grammar'] == "8"
filter = test1
df_extra8 = df_orig.loc[filter]

# extra words for class 9
test1 = df_orig['grammar'] == "9"
filter = test1
df_extra9 = df_orig.loc[filter]

# extra words for class 10
test1 = df_orig['grammar'] == "10"
filter = test1
df_extra10 = df_orig.loc[filter]

# extra words for class 11
test1 = df_orig['grammar'] == "11"
filter = test1
df_extra11 = df_orig.loc[filter]

# extra words for class 12
test1 = df_orig['grammar'] == "12"
filter = test1
df_extra12 = df_orig.loc[filter]

# extra words for class 13
test1 = df_orig['grammar'] == "13"
filter = test1
df_extra13 = df_orig.loc[filter]

# extra words for class 14
test1 = df_orig['grammar'] == "14"
filter = test1
df_extra14 = df_orig.loc[filter]

# save summary csv
# df_summary = pd.concat([df_a_masc, df_ati_pr, df_eti_pr, df_aati_pr, df_oti_pr, df_be_pr, df_i_masc, df_i_aor, df_be_aor, df_esi_aor, df_pers_pron, df_fut, df_ii_masc, df_u_masc, df_ar_masc, df_ant, df_uu_masc, df_time, df_ar2_masc, df_neg, df_with])
# df_summary.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_summary['count'])))

# df_summary = df_summary[['pali_1', 'pos', 'pattern', 'count']]

# save comp for 2 class
df_comb_2 = pd.concat([df_a_masc, df_extra2])
df_comb_2.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_comb_2['count'])))
df_comb_2['sbs_class'] = "2"
df_comb_2 = df_comb_2[['pali_1', 'pos', 'pattern', 'sbs_class', 'count']]
df_comb_2.to_csv("csv-for-classes/class-2.csv", sep="\t", index=None)

# save comp for 3 class
df_comb_3 = pd.concat([df_pr_3, df_imp_3, df_extra3])
df_comb_3.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_comb_3['count'])))
df_comb_3['sbs_class'] = "3"
df_comb_3 = df_comb_3[['pali_1', 'pos', 'pattern', 'sbs_class', 'count']]
df_comb_3.to_csv("csv-for-classes/class-3.csv", sep="\t", index=None)

# save comp for 4 class
df_comb_4 = pd.concat([df_pr_4, df_imp_4, df_be_imp, df_be_pr, df_i_masc, df_i_aor, df_be_aor, df_esi_aor, df_aasi_aor, df_extra4])
df_comb_4.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_comb_4['count'])))
df_comb_4['sbs_class'] = "4"
df_comb_4 = df_comb_4[['pali_1', 'pos', 'pattern', 'sbs_class', 'count']]
df_comb_4.to_csv("csv-for-classes/class-4.csv", sep="\t", index=None)

# save comp for 5 class
df_comb_5 = pd.concat([df_pers_pron, df_fut, df_ii_masc, df_neg, df_neg_5, df_with, df_extra5])
df_comb_5.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_comb_5['count'])))
df_comb_5['sbs_class'] = "5"
df_comb_5 = df_comb_5[['pali_1', 'pos', 'pattern', 'sbs_class', 'count']]
df_comb_5.to_csv("csv-for-classes/class-5.csv", sep="\t", index=None)

# save comp for 6 class
df_comb_6 = pd.concat([df_u_masc, df_ar_masc, df_ar2_masc, df_ant, df_uu_masc, df_time, df_extra6])
df_comb_6.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_comb_6['count'])))
df_comb_6['sbs_class'] = "6"
df_comb_6 = df_comb_6[['pali_1', 'pos', 'pattern', 'sbs_class', 'count']]
df_comb_6.to_csv("csv-for-classes/class-6.csv", sep="\t", index=None)

# save comp for 7 class
df_comb_7 = pd.concat([df_aa_fem, df_opt, df_opt_be, df_extra7])
df_comb_7.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_comb_7['count'])))
df_comb_7['sbs_class'] = "7"
df_comb_7 = df_comb_7[['pali_1', 'pos', 'pattern', 'sbs_class', 'count']]
df_comb_7.to_csv("csv-for-classes/class-7.csv", sep="\t", index=None)

# save comp for 8 class
df_comb_8 = pd.concat([df_ger, df_abs, df_i_fem, df_ii_fem, df_u_fem, df_ar_fem, df_place, df_extra8])
df_comb_8.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_comb_8['count'])))
df_comb_8['sbs_class'] = "8"
df_comb_8 = df_comb_8[['pali_1', 'pos', 'pattern', 'sbs_class', 'count']]
df_comb_8.to_csv("csv-for-classes/class-8.csv", sep="\t", index=None)

# save comp for 9 class
df_comb_9 = pd.concat([df_a_nt, df_i_nt, df_u_nt, df_inf, df_plus_inf, df_inf_kam, df_dat, df_until, df_interr, df_extra9])
df_comb_9.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_comb_9['count'])))
df_comb_9['sbs_class'] = "9"
df_comb_9 = df_comb_9[['pali_1', 'pos', 'pattern', 'sbs_class', 'count']]
df_comb_9.to_csv("csv-for-classes/class-9.csv", sep="\t", index=None)

# save comp for 10 class
df_comb_10 = pd.concat([df_anta_prp, df_enta_prp, df_mana_prp, df_onta_prp, df_ana_prp, df_def, df_pron, df_extra10])
df_comb_10.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_comb_10['count'])))
df_comb_10['sbs_class'] = "10"
df_comb_10 = df_comb_10[['pali_1', 'pos', 'pattern', 'sbs_class', 'count']]
df_comb_10.to_csv("csv-for-classes/class-10.csv", sep="\t", index=None)

# save comp for 11 class
df_comb_11 = pd.concat([df_pp, df_adj, df_abl, df_extra11])
df_comb_11.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_comb_11['count'])))
df_comb_11['sbs_class'] = "11"
df_comb_11 = df_comb_11[['pali_1', 'pos', 'pattern', 'sbs_class', 'count']]
df_comb_11.to_csv("csv-for-classes/class-11.csv", sep="\t", index=None)

# save comp for 12 class
df_comb_12 = pd.concat([df_card, df_ordin, df_money, df_extra12])
df_comb_12.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_comb_12['count'])))
df_comb_12['sbs_class'] = "12"
df_comb_12 = df_comb_12[['pali_1', 'pos', 'pattern', 'sbs_class', 'count']]
df_comb_12.to_csv("csv-for-classes/class-12.csv", sep="\t", index=None)

# save comp for 13 class
df_comb_13 = pd.concat([df_adv, df_pass, df_pass_prp, df_extra13])
df_comb_13.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_comb_13['count'])))
df_comb_13['sbs_class'] = "13"
df_comb_13 = df_comb_13[['pali_1', 'pos', 'pattern', 'sbs_class', 'count']]
df_comb_13.to_csv("csv-for-classes/class-13.csv", sep="\t", index=None)

# save comp for 14 class
df_comb_14 = pd.concat([df_caus, df_caus_pass_pr, df_caus_pass_prp, df_ptp, df_extra14])
df_comb_14.sort_values(by='count', inplace=True, ascending = False, key=lambda x: np.argsort(index_natsorted(df_comb_14['count'])))
df_comb_14['sbs_class'] = "14"
df_comb_14 = df_comb_14[['pali_1', 'pos', 'pattern', 'sbs_class', 'count']]
df_comb_14.to_csv("csv-for-classes/class-14.csv", sep="\t", index=None)

# df_comb = df_comb_2
# df_comb = pd.concat([df_comb_2, df_comb_3])
# df_comb = pd.concat([df_comb_2, df_comb_3, df_comb_4])
# df_comb = pd.concat([df_comb_2, df_comb_3, df_comb_4, df_comb_5])
# df_comb = pd.concat([df_comb_2, df_comb_3, df_comb_4, df_comb_5, df_comb_6])
# df_comb = pd.concat([df_comb_2, df_comb_3, df_comb_4, df_comb_5, df_comb_6, df_comb_7])
# df_comb = pd.concat([df_comb_2, df_comb_3, df_comb_4, df_comb_5, df_comb_6, df_comb_7, df_comb_8])
# df_comb = pd.concat([df_comb_2, df_comb_3, df_comb_4, df_comb_5, df_comb_6, df_comb_7, df_comb_8, df_comb_9])
# df_comb = pd.concat([df_comb_2, df_comb_3, df_comb_4, df_comb_5, df_comb_6, df_comb_7, df_comb_8, df_comb_9, df_comb_10])
# df_comb = pd.concat([df_comb_2, df_comb_3, df_comb_4, df_comb_5, df_comb_6, df_comb_7, df_comb_8, df_comb_9, df_comb_10, df_comb_11])
# df_comb = pd.concat([df_comb_2, df_comb_3, df_comb_4, df_comb_5, df_comb_6, df_comb_7, df_comb_8, df_comb_9, df_comb_10, df_comb_11, df_comb_12])
# df_comb = pd.concat([df_comb_2, df_comb_3, df_comb_4, df_comb_5, df_comb_6, df_comb_7, df_comb_8, df_comb_9, df_comb_10, df_comb_11, df_comb_12, df_comb_13])
df_comb = pd.concat([df_comb_2, df_comb_3, df_comb_4, df_comb_5, df_comb_6, df_comb_7, df_comb_8, df_comb_9, df_comb_10, df_comb_11, df_comb_12, df_comb_13, df_comb_14])

# dps

df_dps = pd.read_csv("../spreadsheets/dps.ods-pali.csv", sep="\t", dtype= str)
df_dps.fillna("")

# choosing order of columns
df_dps = df_dps[['pali_1', 'pos', 'meaning_1', 'stem', 'pattern']]

# df_dps['Pāli2'] = df_dps['pali_1']
df_dps['pali_1'] = df_dps['pali_1'].str.replace('\d+', '')
df_dps['pali_1'] = df_dps['pali_1'].str.replace(' ', '')

df_dps_merged = pd.merge(df_dps, df_comb, how='left')

# find if not

test1 = ~df_comb['pali_1'].isin(df_dps['pali_1'])
# test2 = ~df_time['pattern'].isin(df_dps['pattern'])

logix = test1

df_absent = df_comb[logix]

df_absent.to_csv(f"frequent-words-dps/absent.csv", sep="\t", index=None)

# retern numbers
# df_dps_merged['pali_1']=df_dps_merged['Pāli2']

# adding feedback
# df_dps_merged['Pāli2'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform">Fix it here</a>."""

# df_or = pd.read_csv("../pāli-course/frequent-words.ods-original.csv", sep="\t", dtype= str)
# df_or.fillna("")
# df_or = df_or[['pali_1', 'pos', 'pattern', 'count']]

# df_dps_merged_2 = pd.merge(df_dps_merged, df_or)

df_dps_merged.to_csv("frequent-words-dps/summary-for-class.csv", sep="\t", index=None)

# nidh

df_nid = pd.read_csv("../spreadsheets/nidh_bold.xlsx.csv", sep="\t", dtype= str)
df_nid.fillna("")

df_nid['Pāli2'] = df_nid['pali_1']
df_nid['pali_1'] = df_nid['pali_1'].str.replace('\d+', '')
df_nid['pali_1'] = df_nid['pali_1'].str.replace(' ', '')

df_nid_merged = pd.merge(df_nid, df_absent, how='left')

# find if not

test1 = ~df_comb['pali_1'].isin(df_nid['pali_1'])
# test2 = ~df_time['pattern'].isin(df_dps['pattern'])

logix = test1

df_absent_nid = df_comb[logix]

df_absent_nid.to_csv(f"frequent-words-dps/absent-nid.csv", sep="\t", index=None)


# retern numbers
df_nid_merged['pali_1']=df_nid_merged['Pāli2']

# adding feedback
# df_nid_merged['Pāli2'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform">Fix it here</a>."""

# test1 = df_nid_merged['sbs_class'] != ""
# filter = test1
# df_nid_merged = df_nid_merged[filter]

# test2 = df_nid_merged['count'].str.contains('\d+')
# filter = test2
# df_nid_merged = df_nid_merged.loc[filter]

df_nid_merged.sort_values(by='sbs_class', inplace=True, ascending = True, key=lambda x: np.argsort(index_natsorted(df_nid_merged['count'])))


df_nid_merged.to_csv("frequent-words-dps/to-add.csv", sep="\t", index=None)


df_comb[['pali_1', 'pos', 'pattern', 'count']].to_csv("csv-all-pos/for-class.csv", sep="\t", index=None)

# df_absent = pd.concat([df_absent, df_time[logix]])
# df_absent = df_absent df_class_1[logix]

# adding feedback ?
# df_absent.reset_index(drop=True)


# print lenght

# a_masc_l = len(df_a_masc)
# print(f"lenght a_masc {a_masc_l}")

# ati_pr_l = len(df_ati_pr)
# print(f"lenght ati_pr {ati_pr_l}")

# eti_pr_l = len(df_eti_pr)
# print(f"lenght eti_pr {eti_pr_l}")

# aati_pr_l = len(df_aati_pr)
# print(f"lenght āti_pr {aati_pr_l}")

# oti_pr_l = len(df_oti_pr)
# print(f"lenght oti_pr {oti_pr_l}")

# be_pr_l = len(df_be_pr)
# print(f"lenght be_pr {be_pr_l}")

# i_masc_l = len(df_i_masc)
# print(f"lenght i_masc {i_masc_l}")

# i_aor_l = len(df_i_aor)
# print(f"lenght i_aor {i_aor_l}")

# be_aor_l = len(df_be_aor)
# print(f"lenght be_aor {be_aor_l}")

# esi_aor_l = len(df_esi_aor)
# print(f"lenght esi_aor {esi_aor_l}")

# pers_pron_l = len(df_pers_pron)
# print(f"lenght pers_pron {pers_pron_l}")

# fut_l = len(df_fut)
# print(f"lenght fut {fut_l}")

# ii_masc_l = len(df_ii_masc)
# print(f"lenght ī_masc {ii_masc_l}")

# u_masc_l = len(df_u_masc)
# print(f"lenght u_masc {u_masc_l}")

# ar_masc_l = len(df_ar_masc)
# print(f"lenght ar_masc {ar_masc_l}")

# ant_l = len(df_ant)
# print(f"lenght ant {ant_l}")

# uu_masc_l = len(df_uu_masc)
# print(f"lenght ū_masc {uu_masc_l}")

# adv_time_l = len(df_time)
# print(f"lenght adv_time {adv_time_l}")


