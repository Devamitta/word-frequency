import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re

df = read_ods("original-sources/frequent-words.ods")
df.fillna("", inplace=True)
# df = df.astype(str)
# df = df.replace(to_replace ="\.0", value = "", regex = True) #removes all flaots .0

# sort by frequency
df = df.sort_values(by=['count'], ascending = False)

#filter adv
test1 = df['POS'] == "ind"
test2 = df['Grammar'] == "time"
test3 = df['Grammar'] == "place"
test4 = df['Grammar'] == "interr"
test5 = df['Grammar'] == "neg"
test6 = df['Grammar'] == "with"

filter = test1 & test2
df_time = df.loc[filter]

filter = test1 & test3
df_place = df.loc[filter]

filter = test1 & test4
df_interr = df.loc[filter]

filter = test1 & test5
df_neg = df.loc[filter]

filter = test1 & test6
df_with = df.loc[filter]

# save adv csv
df_time = df_time[['Pāli1', 'POS', 'Pattern', 'count']]
df_time.to_csv("frequent-words/adv_time.csv", sep="\t", index=None)

df_place = df_place[['Pāli1', 'POS', 'Pattern', 'count']]
df_place.to_csv("frequent-words/adv_place.csv", sep="\t", index=None)

df_interr = df_interr[['Pāli1', 'POS', 'Pattern', 'count']]
df_interr.to_csv("frequent-words/adv_interr.csv", sep="\t", index=None)

df_neg = df_neg[['Pāli1', 'POS', 'Pattern', 'count']]
df_neg.to_csv("frequent-words/ind_neg.csv", sep="\t", index=None)

df_with = df_with[['Pāli1', 'POS', 'Pattern', 'count']]
df_with.to_csv("frequent-words/ind_with.csv", sep="\t", index=None)

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
test3 = df_orig['Grammar'] != "desid"
# test3 = df_orig['Grammar'] != "name"
filter = test1 & test2 & test3
df_orig = df_orig.loc[filter]

# filter what is done
df = df.head(1550)

# filter not comp | comp vb | name
test1 = df['Grammar'] != "comp"
test3 = df_orig['Grammar'] != "desid"
# test3 = df_orig['Grammar'] != "name"
filter = test1 & test2 & test3
df = df.loc[filter]

# save all done
df[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("curated-sources/frequent-words.csv", sep="\t", index=None)

# filter masc

test1 = df['POS'] == "masc"
test2 = df['Pattern'] == "a masc"
test3 = df['Pattern'] == "i masc"

test9 = df['Pattern'] == "ar2 masc"

test10 = df['Grammar'] != "dat"
test11 = df['Grammar'] != "neg"
# pass and caus
test15 = df['Grammar'] != "pass"
test16 = df['Grammar'] != "caus"
test17 = df['Grammar'] != "irreg"
test18 = df['Grammar'] != "neg"

filter = test1 & test2 & test10 & test11 & test16
df_a_masc = df.loc[filter]
df_a_masc = df_a_masc.head(200)

filter = test1 & test3 & test11
df_i_masc = df.loc[filter]

filter = test1 & test9
df_ar2_masc = df.loc[filter]


test1 = df_orig['POS'] == "masc"

test4 = df_orig['Pattern'] == "ī masc"
test5 = df_orig['Pattern'] == "u masc"
test6 = df_orig['Pattern'] == "ar masc"
test7 = df_orig['Pattern'] == "ū masc"

filter = test1 & test4
df_ii_masc = df_orig.loc[filter]
df_ii_masc = df_ii_masc.head(10)

filter = test1 & test5
df_u_masc = df_orig.loc[filter]
df_u_masc = df_u_masc.head(12)

filter = test1 & test6
df_ar_masc = df_orig.loc[filter]
df_ar_masc = df_ar_masc.head(10)

filter = test1 & test7
df_uu_masc = df_orig.loc[filter]
df_uu_masc = df_uu_masc.head(6)


# save masc csv

df_a_masc[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/masc-a.csv", sep="\t", index=None)

df_i_masc[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/masc-i.csv", sep="\t", index=None)

df_ii_masc[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/masc-ī.csv", sep="\t", index=None)

df_u_masc[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/masc-u.csv", sep="\t", index=None)

df_uu_masc[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/masc-ū.csv", sep="\t", index=None)

df_ar_masc[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/masc-ar.csv", sep="\t", index=None)

df_ar2_masc[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/masc-ar2.csv", sep="\t", index=None)

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
# test9 = df['Pattern'] == "natthi pr"
# irreg pr
test10 = df['Pattern'] == "eti pr 2"
test11 = df['Pattern'] == "brūti pr"
test12 = df['Pattern'] == "dakkhati pr"
test13 = df['Pattern'] == "hanati pr"
test14 = df['Pattern'] == "kubbati pr"
# pass and caus pr
test15 = df['Grammar'] != "pass"
test16 = df['Grammar'] != "caus"
test17 = df['Grammar'] != "irreg"
test18 = df['Grammar'] != "neg"

filter = test1 & test2 & test15 & test16 & test17 & test18
df_ati_pr = df.loc[filter]
df_ati_pr = df_ati_pr.head(100)

filter = test1 & test3 & test15 & test16 & test17 & test18
df_eti_pr = df.loc[filter]

filter = test1 & test4 & test15 & test16 & test17 & test18
df_aati_pr = df.loc[filter]

filter = test1 & test5 & test15 & test16 & test17 & test18
df_oti_pr = df.loc[filter]

filter = test1 & test6 & test15 & test16 & test17 & test18
df_karoti = df.loc[filter]

df_oti_pr = pd.concat([df_oti_pr, df_karoti])
df_oti_pr = df_oti_pr.sort_values(by=['count'], ascending = False)

# df_pr = pd.concat([df_ati_pr, df_eti_pr, df_aati_pr, df_oti_pr])

# test1 = df_pr['Grammar'] == "pass"
# test2 = df_pr['Grammar'] == "caus"
# filter = test1 & test2
# df_pr_act = df_pr.loc[filter]

# df_pr_act = df_pr_act.sort_values(by=['count'], ascending = False)


filter = test1 & test7
df_hoti = df.loc[filter]

filter = test1 & test8
df_atthi = df.loc[filter]

# filter = test1 & test9 & test18
# df_natthi = df.loc[filter]

df_be_pr = pd.concat([df_hoti, df_atthi])
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

test4 = df['Pattern'] == "āsi aor"

test7 = df['Pattern'] == "ahosi aor"
test8 = df['Pattern'] == "āsi aor irreg"

test9 = df['Pattern'] == "hari aor"
# irreg aor
test10 = df['Pattern'] == "avoca aor"
test11 = df['Pattern'] == "assosi aor"
test12 = df['Pattern'] == "ddasa aor"
# pass and caus aor
test15 = df['Grammar'] != "pass"
test16 = df['Grammar'] != "caus"
test17 = df['Grammar'] != "irreg"

filter = test1 & test2 & test15 & test16 & test17
df_i_aor = df.loc[filter]

filter = test1 & test9 & test15 & test16 & test17
df_hari = df.loc[filter]

df_i_aor = pd.concat([df_i_aor, df_hari])
df_i_aor = df_i_aor.sort_values(by=['count'], ascending = False)

filter = test1 & test4 & test15 & test16 & test17
df_aasi_aor = df.loc[filter]

filter = test1 & test7 & test15 & test16 & test17
df_ahosi = df.loc[filter]

filter = test1 & test8 & test15 & test16 & test17
df_aasi = df.loc[filter]

df_be_aor = pd.concat([df_aasi, df_ahosi])
df_be_aor = df_be_aor.sort_values(by=['count'], ascending = False)

test1 = df_orig['POS'] == "aor"
test3 = df_orig['Pattern'] == "esi aor"
# pass and caus aor
test15 = df_orig['Grammar'] != "pass"
test16 = df_orig['Grammar'] != "caus"
test17 = df_orig['Grammar'] != "irreg"
filter = test1 & test3 & test15 & test16 & test17
df_esi_aor = df_orig.loc[filter]
df_esi_aor = df_esi_aor.head(10)

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
filter = test1 & test2
df_fut = df_orig.loc[filter]
df_fut = df_fut.head(25)

# save fut csv
df_fut[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/fut.csv", sep="\t", index=None)

# filter pr and masc neg
test1 = df['POS'] != "ind"
test2 = df['Grammar'] == "neg"
filter = test1 & test2
df_neg_4 = df.loc[filter]

# save fut csv
df_neg_4[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/neg-4cl.csv", sep="\t", index=None)


# filter fem

test1 = df['POS'] == "fem"
test2 = df['Pattern'] == "ā fem"
test3 = df['Pattern'] == "i fem"

# pass and caus
test15 = df['Grammar'] != "pass"
test16 = df['Grammar'] != "caus"
test17 = df['Grammar'] != "irreg"
test18 = df['Grammar'] != "neg"

filter = test1 & test2 & test16
df_aa_fem = df.loc[filter]
df_aa_fem = df_aa_fem.head(200)

filter = test1 & test3 & test16
df_i_fem = df.loc[filter]


test1 = df_orig['POS'] == "fem"
test4 = df_orig['Pattern'] == "ī fem"
test5 = df_orig['Pattern'] == "u fem"
test6 = df_orig['Pattern'] == "ar fem"
test7 = df_orig['Pattern'] == "ū fem"

filter = test1 & test4
df_ii_fem = df_orig.loc[filter]
df_ii_fem = df_ii_fem.head(15)

filter = test1 & test5
df_u_fem = df_orig.loc[filter]
# df_u_fem = df_u_fem.head(12)

filter = test1 & test6
df_ar_fem = df_orig.loc[filter]
df_ar_fem = df_ar_fem.head(10)

filter = test1 & test7
df_uu_fem = df_orig.loc[filter]
# df_uu_fem = df_uu_fem.head(6)

# save fem csv

df_aa_fem[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/fem-ā.csv", sep="\t", index=None)

df_i_fem[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/fem-i.csv", sep="\t", index=None)

df_ii_fem[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/fem-ī.csv", sep="\t", index=None)

df_u_fem[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/fem-u.csv", sep="\t", index=None)

df_uu_fem[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/fem-ū.csv", sep="\t", index=None)

df_ar_fem[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/fem-ar.csv", sep="\t", index=None)


# filter nt

test1 = df['POS'] == "nt"
test2 = df['Pattern'] == "a nt"

test10 = df['Grammar'] != "dat"

filter = test1 & test2 & test10
df_a_nt = df.loc[filter]

df_a_nt = df_a_nt.head(200)

test1 = df_orig['POS'] == "nt"
test3 = df_orig['Pattern'] == "i nt"
test4 = df_orig['Pattern'] == "u nt"

filter = test1 & test3
df_i_nt = df_orig.loc[filter]

filter = test1 & test4
df_u_nt = df_orig.loc[filter]
df_u_nt = df_u_nt.head(10)


# save nt csv

df_a_nt[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/nt-a.csv", sep="\t", index=None)

df_i_nt[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/nt-i.csv", sep="\t", index=None)

df_u_nt[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/nt-u.csv", sep="\t", index=None)

# filter inf
test1 = df_orig['POS'] == "inf"
test2 = df_orig['Grammar'] != "irreg"
# pass and caus
test15 = df['Grammar'] != "pass"
test16 = df['Grammar'] != "caus"
test17 = df['Grammar'] != "irreg"
test18 = df['Grammar'] != "neg"

filter = test1 & test15 & test16
df_inf = df_orig.loc[filter]
df_inf = df_inf.head(20)

# save inf csv
df_inf[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/inf.csv", sep="\t", index=None)

# filter +inf
test2 = df_orig['Grammar'] == "+inf"
filter = test2
df_plus_inf = df_orig.loc[filter]
# df_plus_inf = df_plus_inf.head(20)

# save +inf csv
df_plus_inf[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/+inf.csv", sep="\t", index=None)

# filter inf kāma
test2 = df_orig['Grammar'] == "inf kāma"
filter = test2
df_inf_kam = df_orig.loc[filter]
# df_inf_kam = df_inf_kam.head(20)

# save inf kāma
df_inf_kam[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/inf-kāma.csv", sep="\t", index=None)

# filter dat of purpose
test2 = df_orig['Grammar'] == "dat"
filter = test2
df_dat = df_orig.loc[filter]
# df_dat = df_dat.head(20)

# save dat of purpose
df_dat[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/dat.csv", sep="\t", index=None)

# filter until-then
test2 = df['Grammar'] == "until-then"
filter = test2
df_until = df.loc[filter]

# save until-then
df_until[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/until-then.csv", sep="\t", index=None)



# filter opt
test1 = df['POS'] == "opt"
test2 = df['Pattern'] == "eyya opt"
test3 = df['Pattern'] == "ssa opt"
test4 = df['Pattern'] == "siyā opt"

filter = test1 & test2
df_opt = df.loc[filter]

filter = test1 & test3
df_opt_ssa = df.loc[filter]

filter = test1 & test4
df_opt_siya = df.loc[filter]
df_opt_be = pd.concat([df_opt_ssa, df_opt_siya])

# save opt
df_opt[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/opt.csv", sep="\t", index=None)

df_opt_be[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/opt-be.csv", sep="\t", index=None)

# filter ger and abs
test1 = df['POS'] == "ger"
test2 = df['POS'] == "abs"
# pass and caus
test15 = df['Grammar'] != "pass"
test16 = df['Grammar'] != "caus"
test17 = df['Grammar'] != "irreg"
test18 = df['Grammar'] != "neg"

filter = test1 & test15 & test16
df_ger = df.loc[filter]

filter = test2 & test15 & test16
df_abs = df.loc[filter]

# save ger and abs
df_ger[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/ger.csv", sep="\t", index=None)

df_abs[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/abs.csv", sep="\t", index=None)


# filter prp
test1 = df['POS'] == "prp"
test2 = df['Pattern'] == "anta prp"
test3 = df['Pattern'] == "māna prp"
# pass and caus prp
test15 = df['Grammar'] != "pass"
test16 = df['Grammar'] != "caus"
test17 = df['Grammar'] != "irreg"

filter = test1 & test2 & test15 & test16 & test17
df_anta_prp = df.loc[filter]
# df_anta_prp = df_anta_prp.head(100)

filter = test1 & test3 & test15 & test16 & test17
df_mana_prp = df.loc[filter]

test1 = df_orig['POS'] == "prp"
test4 = df_orig['Pattern'] == "enta prp"
test5 = df_orig['Pattern'] == "onta prp"
test6 = df_orig['Pattern'] == "āna prp"
# pass and caus prp
test15 = df_orig['Grammar'] != "pass"
test16 = df_orig['Grammar'] != "caus"
test17 = df_orig['Grammar'] != "irreg"


filter = test1 & test4 & test15 & test16 & test17
df_enta_prp = df_orig.loc[filter]
df_enta_prp = df_enta_prp.head(5)

filter = test1 & test5 & test15 & test16 & test17
df_onta_prp = df_orig.loc[filter]
df_onta_prp = df_onta_prp.head(5)

filter = test1 & test6 & test15 & test16 & test17
df_ana_prp = df_orig.loc[filter]

# save prp csv

df_anta_prp[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/prp-anta.csv", sep="\t", index=None)

df_mana_prp[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/prp-māna.csv", sep="\t", index=None)

df_enta_prp[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/prp-enta.csv", sep="\t", index=None)

df_onta_prp[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/prp-onta.csv", sep="\t", index=None)

df_ana_prp[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/pr-āna.csv", sep="\t", index=None)

# filter def-art aññatara
test1 = df['Grammar'] == "def-art"

filter = test1
df_def = df.loc[filter]

# filter pron
test1 = df['POS'] == "pron"
test2 = df['Pattern'] != "tvaṃ pron"
test3 = df['Pattern'] != "ahaṃ pron"
test4 = df['Grammar'] != "until-then"
test5 = df['Grammar'] != "interr"

filter = test1 & test2 & test3 & test4 & test5
df_pron = df.loc[filter]

df_pron[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/pron.csv", sep="\t", index=None)

# filter pp
test1 = df['POS'] == "pp"
# pass and caus pr
test15 = df['Grammar'] != "pass"
test16 = df['Grammar'] != "caus"
test17 = df['Grammar'] != "irreg"

filter = test1 & test15 & test16 & test17
df_pp = df.loc[filter]
df_pp = df_pp.head(100)

df_pp[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/pp.csv", sep="\t", index=None)

# filter adj
test1 = df['POS'] == "adj"
test2 = df['Grammar'] != "def-art"
test3 = df['Grammar'] != "+inf"
test4 = df['Grammar'] != "inf kāma"
test5 = df['Pattern'] != "ant adj"

filter = test1 & test2 & test3 & test4 & test5
df_adj = df.loc[filter]
df_adj = df_adj.head(150)

df_adj[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/adj.csv", sep="\t", index=None)

# filter abl of separation
test1 = df['Grammar'] == "abl"

filter = test1
df_abl = df.loc[filter]
df_abl = df_abl.head(150)

df_abl[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/abl.csv", sep="\t", index=None)

# filter numbers
test1 = df['POS'] == "card"
test2 = df['POS'] == "ordin"

filter = test1
df_card = df.loc[filter]

filter = test2
df_ordin = df.loc[filter]

df_card[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/card.csv", sep="\t", index=None)
df_ordin[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/ordin.csv", sep="\t", index=None)

# filter money
test1 = df['Grammar'] == "money"

filter = test1
df_money = df.loc[filter]

df_money[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/money.csv", sep="\t", index=None)

# filter adv
test1 = df_orig['POS'] == "ind"
test2 = df_orig['Grammar'] == "dhā"
test3 = df_orig['Grammar'] == "so"
test4 = df_orig['Grammar'] == "khattuṃ"
test5 = df_orig['Grammar'] == "thaṃ"
test6 = df_orig['Grammar'] == "to"
test7 = df_orig['Grammar'] == "tra"
test8 = df_orig['Grammar'] == "thā"
test9 = df_orig['Grammar'] == "pure"

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

test1 = df['POS'] == "ind"
test2 = df['Grammar'] == "adv"

filter = test1 & test2
df_adv_adv = df.loc[filter]
# df_adv = df_adv.head(30)

df_adv_dhā[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/adv-dhā.csv", sep="\t", index=None)
df_adv_so[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/adv-so.csv", sep="\t", index=None)
df_adv_khattum[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/adv-khattuṃ.csv", sep="\t", index=None)
df_adv_tham[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/adv-thaṃ.csv", sep="\t", index=None)
df_adv_to[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/adv-to.csv", sep="\t", index=None)
df_adv_tra[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/adv-tra.csv", sep="\t", index=None)
df_adv_tha[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/adv-thā.csv", sep="\t", index=None)
df_adv_pure[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/adv-pure.csv", sep="\t", index=None)
df_adv_adv[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/adv-adv.csv", sep="\t", index=None)

df_adv = pd.concat([df_adv_dhā, df_adv_so, df_adv_khattum, df_adv_tham, df_adv_to, df_adv_tra, df_adv_tha, df_adv_pure, df_adv_adv])
df_adv = df_adv.sort_values(by=['count'], ascending = False)

df_adv[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/adv.csv", sep="\t", index=None)

# filter pass
test1 = df_orig['Grammar'] == "pass"

filter = test1
df_pass = df_orig.loc[filter]

df_pass[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/pass.csv", sep="\t", index=None)


# save summary csv
df_summary = pd.concat([df_a_masc, df_ati_pr, df_eti_pr, df_aati_pr, df_oti_pr, df_be_pr, df_i_masc, df_i_aor, df_be_aor, df_esi_aor, df_pers_pron, df_fut, df_ii_masc, df_u_masc, df_ar_masc, df_ant, df_uu_masc, df_time, df_ar2_masc, df_neg, df_with])
df_summary = df_summary.sort_values(by=['count'], ascending = False)

df_summary = df_summary[['Pāli1', 'POS', 'Pattern', 'count']]

# save comp for 1 class
df_comb_1 = pd.concat([df_a_masc])
df_comb_1 = df_comb_1.sort_values(by=['count'], ascending = False)
df_comb_1['class'] = "1"
df_comb_1 = df_comb_1[['Pāli1', 'POS', 'Pattern', 'class', 'count']]
df_comb_1.to_csv("csv-for-classes/class-1.csv", sep="\t", index=None)

# save comp for 2 class
df_comb_2 = pd.concat([df_ati_pr, df_eti_pr, df_aati_pr, df_oti_pr])
df_comb_2 = df_comb_2.sort_values(by=['count'], ascending = False)
df_comb_2['class'] = "2"
df_comb_2 = df_comb_2[['Pāli1', 'POS', 'Pattern', 'class', 'count']]
df_comb_2.to_csv("csv-for-classes/class-2.csv", sep="\t", index=None)

# save comp for 3 class
df_comb_3 = pd.concat([df_be_pr, df_i_masc, df_i_aor, df_be_aor, df_esi_aor, df_aasi_aor])
df_comb_3 = df_comb_3.sort_values(by=['count'], ascending = False)
df_comb_3['class'] = "3"
df_comb_3 = df_comb_3[['Pāli1', 'POS', 'Pattern', 'class', 'count']]
df_comb_3.to_csv("csv-for-classes/class-3.csv", sep="\t", index=None)

# save comp for 4 class
df_comb_4 = pd.concat([df_pers_pron, df_fut, df_ii_masc, df_neg, df_neg_4, df_with])
df_comb_4 = df_comb_4.sort_values(by=['count'], ascending = False)
df_comb_4['class'] = "4"
df_comb_4 = df_comb_4[['Pāli1', 'POS', 'Pattern', 'class', 'count']]
df_comb_4.to_csv("csv-for-classes/class-4.csv", sep="\t", index=None)

# save comp for 5 class
df_comb_5 = pd.concat([df_u_masc, df_ar_masc, df_ar2_masc, df_ant, df_uu_masc, df_time])
df_comb_5 = df_comb_5.sort_values(by=['count'], ascending = False)
df_comb_5['class'] = "5"
df_comb_5 = df_comb_5[['Pāli1', 'POS', 'Pattern', 'class', 'count']]
df_comb_5.to_csv("csv-for-classes/class-5.csv", sep="\t", index=None)

# save comp for 6 class
df_comb_6 = pd.concat([df_aa_fem, df_opt, df_opt_be])
df_comb_6 = df_comb_6.sort_values(by=['count'], ascending = False)
df_comb_6['class'] = "6"
df_comb_6 = df_comb_6[['Pāli1', 'POS', 'Pattern', 'class', 'count']]
df_comb_6.to_csv("csv-for-classes/class-6.csv", sep="\t", index=None)

# save comp for 7 class
df_comb_7 = pd.concat([df_ger, df_abs, df_i_fem, df_ii_fem, df_u_fem, df_ar_fem, df_place])
df_comb_7 = df_comb_7.sort_values(by=['count'], ascending = False)
df_comb_7['class'] = "7"
df_comb_7 = df_comb_7[['Pāli1', 'POS', 'Pattern', 'class', 'count']]
df_comb_7.to_csv("csv-for-classes/class-7.csv", sep="\t", index=None)

# save comp for 8 class
df_comb_8 = pd.concat([df_a_nt, df_i_nt, df_u_nt, df_inf, df_plus_inf, df_inf_kam, df_dat, df_until, df_interr])
df_comb_8 = df_comb_8.sort_values(by=['count'], ascending = False)
df_comb_8['class'] = "8"
df_comb_8 = df_comb_8[['Pāli1', 'POS', 'Pattern', 'class', 'count']]
df_comb_8.to_csv("csv-for-classes/class-8.csv", sep="\t", index=None)

# save comp for 9 class
df_comb_9 = pd.concat([df_anta_prp, df_enta_prp, df_mana_prp, df_onta_prp, df_ana_prp, df_def, df_pron])
df_comb_9 = df_comb_9.sort_values(by=['count'], ascending = False)
df_comb_9['class'] = "9"
df_comb_9 = df_comb_9[['Pāli1', 'POS', 'Pattern', 'class', 'count']]
df_comb_9.to_csv("csv-for-classes/class-9.csv", sep="\t", index=None)

# save comp for 10 class
df_comb_10 = pd.concat([df_pp, df_adj, df_abl])
df_comb_10 = df_comb_10.sort_values(by=['count'], ascending = False)
df_comb_10['class'] = "10"
df_comb_10 = df_comb_10[['Pāli1', 'POS', 'Pattern', 'class', 'count']]
df_comb_10.to_csv("csv-for-classes/class-10.csv", sep="\t", index=None)

# save comp for 11 class
df_comb_11 = pd.concat([df_card, df_ordin, df_money])
df_comb_11 = df_comb_11.sort_values(by=['count'], ascending = False)
df_comb_11['class'] = "11"
df_comb_11 = df_comb_11[['Pāli1', 'POS', 'Pattern', 'class', 'count']]
df_comb_11.to_csv("csv-for-classes/class-11.csv", sep="\t", index=None)

# save comp for 12 class
df_comb_12 = pd.concat([df_adv, df_pass])
df_comb_12 = df_comb_12.sort_values(by=['count'], ascending = False)
df_comb_12['class'] = "12"
df_comb_12 = df_comb_12[['Pāli1', 'POS', 'Pattern', 'class', 'count']]
df_comb_12.to_csv("csv-for-classes/class-12.csv", sep="\t", index=None)

# df_comb = df_comb_1
# df_comb = pd.concat([df_comb_1, df_comb_2])
# df_comb = pd.concat([df_comb_1, df_comb_2, df_comb_3])
# df_comb = pd.concat([df_comb_1, df_comb_2, df_comb_3, df_comb_4])
# df_comb = pd.concat([df_comb_1, df_comb_2, df_comb_3, df_comb_4, df_comb_5])
# df_comb = pd.concat([df_comb_1, df_comb_2, df_comb_3, df_comb_4, df_comb_5, df_comb_6])
# df_comb = pd.concat([df_comb_1, df_comb_2, df_comb_3, df_comb_4, df_comb_5, df_comb_6, df_comb_7])
# df_comb = pd.concat([df_comb_1, df_comb_2, df_comb_3, df_comb_4, df_comb_5, df_comb_6, df_comb_7, df_comb_8])
# df_comb = pd.concat([df_comb_1, df_comb_2, df_comb_3, df_comb_4, df_comb_5, df_comb_6, df_comb_7, df_comb_8, df_comb_9])
# df_comb = pd.concat([df_comb_1, df_comb_2, df_comb_3, df_comb_4, df_comb_5, df_comb_6, df_comb_7, df_comb_8, df_comb_9, df_comb_10])
# df_comb = pd.concat([df_comb_1, df_comb_2, df_comb_3, df_comb_4, df_comb_5, df_comb_6, df_comb_7, df_comb_8, df_comb_9, df_comb_10, df_comb_11])
df_comb = pd.concat([df_comb_1, df_comb_2, df_comb_3, df_comb_4, df_comb_5, df_comb_6, df_comb_7, df_comb_8, df_comb_9, df_comb_10, df_comb_11, df_comb_12])

# dps

df_dps = pd.read_csv("../spreadsheets/dps.csv", sep="\t", dtype= str)
df_dps.fillna("", inplace=True)

df_dps['Pāli2'] = df_dps['Pāli1']
df_dps['Pāli1'] = df_dps['Pāli1'].str.replace('\d+', '')
df_dps['Pāli1'] = df_dps['Pāli1'].str.replace(' ', '')

df_dps_merged = pd.merge(df_dps, df_comb, how='left')

# find if not

test1 = ~df_comb['Pāli1'].isin(df_dps['Pāli1'])
# test2 = ~df_time['Pattern'].isin(df_dps['Pattern'])

logix = test1

df_absent = df_comb[logix]

df_absent.to_csv(f"frequent-words-dps/absent.csv", sep="\t", index=None)

# retern numbers
df_dps_merged['Pāli1']=df_dps_merged['Pāli2']

# adding feedback
# df_dps_merged['Pāli2'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform">Fix it here</a>."""

# df_dps_merged = df_dps_merged.sort_values(by=['Pāli1'])
df_dps_merged.to_csv("frequent-words-dps/summary-for-class.csv", sep="\t", index=None)

# nidh

df_nid = pd.read_csv("../spreadsheets/nidh_bold.csv", sep="\t", dtype= str)
df_nid.fillna("", inplace=True)

df_nid['Pāli2'] = df_nid['Pāli1']
df_nid['Pāli1'] = df_nid['Pāli1'].str.replace('\d+', '')
df_nid['Pāli1'] = df_nid['Pāli1'].str.replace(' ', '')

df_nid_merged = pd.merge(df_nid, df_absent, how='left')

# find if not

test1 = ~df_comb['Pāli1'].isin(df_nid['Pāli1'])
# test2 = ~df_time['Pattern'].isin(df_dps['Pattern'])

logix = test1

df_absent_nid = df_comb[logix]

df_absent_nid.to_csv(f"frequent-words-dps/absent-nid.csv", sep="\t", index=None)


# retern numbers
df_nid_merged['Pāli1']=df_nid_merged['Pāli2']

# adding feedback
# df_nid_merged['Pāli2'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform">Fix it here</a>."""

# test1 = df_nid_merged['count'] != ""
# filter = test1
# df_nid_merged = df_nid_merged[filter]

# test2 = df_nid_merged['count'].str.contains('\d+')
# filter = test2
# df_nid_merged = df_nid_merged.loc[filter]

# df_nid_merged = df_nid_merged.sort_values(by=['Pāli1'])

df_nid_merged.to_csv("frequent-words-dps/to-add.csv", sep="\t", index=None)


df_comb[['Pāli1', 'POS', 'Pattern', 'count']].to_csv("frequent-words/for-class.csv", sep="\t", index=None)

# df_absent = pd.concat([df_absent, df_time[logix]])
# df_absent = df_absent df_class_1[logix]

# adding feedback ?
# df_absent.reset_index(drop=True, inplace=True)


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


