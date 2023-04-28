import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
import sys
import csv

# df_abbr
df_abbr = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="abbr", dtype=str)
df_abbr.fillna("", inplace=True)

df_abbr_dps = df_abbr[['abbrev', 'meaning', 'pāli', 'ru-meaning', 'example', 'explanation', 'ru-abbrev']]

df_abbr_dps.to_csv("../exporter/assets/abbreviations.csv", sep="\t", index=None)

test1 = df_abbr['type'] != ""
filter = test1
df_abbr_class = df_abbr.loc[filter]

df_abbr_class = df_abbr_class[['id', 'abbrev', 'meaning', 'pāli', 'example', 'explanation', 'pattern']]

df_abbr_class.to_excel("../csv-for-anki/abbr.xlsx", index=None)

# adding feedback
df_abbr_class.reset_index(drop=True, inplace=True)
df_abbr_class['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_abbr_class['abbrev'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

df_abbr_class.to_csv("../csv-for-anki/grammar/gr_1_class.csv", sep="\t", index=None)

# df_a_masc
df_a_masc = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="a_masc", dtype=str)
df_a_masc.fillna("", inplace=True)

df_a_masc.reset_index(drop=True, inplace=True)
df_a_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_a_masc['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

df_a_masc.to_csv("../csv-for-anki/grammar/gr_2_class.csv", sep="\t", index=None)

# df_pr
df_pr = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="pr", dtype=str)
df_pr.fillna("", inplace=True)

df_pr.reset_index(drop=True, inplace=True)
df_pr['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_pr['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

df_pr.to_csv("../csv-for-anki/grammar/gr_3_class.csv", sep="\t", index=None)

# df_pr_aor_be
df_pr_aor_be = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="pr_aor_be", dtype=str)
df_pr_aor_be.fillna("", inplace=True)

df_pr_aor_be.reset_index(drop=True, inplace=True)
df_pr_aor_be['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_pr_aor_be['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_pr_aor_be.to_csv("../csv-for-anki/grammar/df_pr_aor_be.csv", sep="\t", index=None)

# df_aor
df_aor = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="aor", dtype=str)
df_aor.fillna("", inplace=True)

df_aor.reset_index(drop=True, inplace=True)
df_aor['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_aor['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_aor.to_csv("../csv-for-anki/grammar/df_aor.csv", sep="\t", index=None)

# df_i_masc
df_i_masc = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="i_masc", dtype=str)
df_i_masc.fillna("", inplace=True)

df_i_masc.reset_index(drop=True, inplace=True)
df_i_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_i_masc['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_i_masc.to_csv("../csv-for-anki/grammar/df_i_masc.csv", sep="\t", index=None)

# df_4_class

df_4_class = pd.concat([df_i_masc, df_aor, df_pr_aor_be])

df_4_class.to_csv("../csv-for-anki/grammar/gr_4_class.csv", sep="\t", index=None)

# df_fut
df_fut = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="fut", dtype=str)
df_fut.fillna("", inplace=True)

df_fut.reset_index(drop=True, inplace=True)
df_fut['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_fut['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_fut.to_csv("../csv-for-anki/grammar/df_fut.csv", sep="\t", index=None)

# df_ii_masc
df_ii_masc = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="ii_masc", dtype=str)
df_ii_masc.fillna("", inplace=True)

df_ii_masc.reset_index(drop=True, inplace=True)
df_ii_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ii_masc['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_ii_masc.to_csv("../csv-for-anki/grammar/df_ii_masc.csv", sep="\t", index=None)

# df_pers_pron
df_pers_pron = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="pers_pron", dtype=str)
df_pers_pron.fillna("", inplace=True)

df_pers_pron.reset_index(drop=True, inplace=True)
df_pers_pron['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_pers_pron['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_pers_pron.to_csv("../csv-for-anki/grammar/df_pers_pron.csv", sep="\t", index=None)

# df_5_class

df_5_class = pd.concat([df_ii_masc, df_fut, df_pers_pron])

df_5_class.to_csv("../csv-for-anki/grammar/gr_5_class.csv", sep="\t", index=None)


# df_u_masc
df_u_masc = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="u_masc", dtype=str)
df_u_masc.fillna("", inplace=True)

df_u_masc.reset_index(drop=True, inplace=True)
df_u_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_u_masc['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_u_masc.to_csv("../csv-for-anki/grammar/df_u_masc.csv", sep="\t", index=None)


# df_ar_masc
df_ar_masc = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="ar_masc", dtype=str)
df_ar_masc.fillna("", inplace=True)

df_ar_masc.reset_index(drop=True, inplace=True)
df_ar_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ar_masc['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_ar_masc.to_csv("../csv-for-anki/grammar/df_ar_masc.csv", sep="\t", index=None)

# df_ar2_masc
df_ar2_masc = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="ar2_masc", dtype=str)
df_ar2_masc.fillna("", inplace=True)

df_ar2_masc.reset_index(drop=True, inplace=True)
df_ar2_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ar2_masc['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_ar2_masc.to_csv("../csv-for-anki/grammar/df_ar2_masc.csv", sep="\t", index=None)

# df_uu_masc
df_uu_masc = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="uu_masc", dtype=str)
df_uu_masc.fillna("", inplace=True)

df_uu_masc.reset_index(drop=True, inplace=True)
df_uu_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_uu_masc['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_uu_masc.to_csv("../csv-for-anki/grammar/df_uu_masc.csv", sep="\t", index=None)

# df_ant
df_ant = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="ant", dtype=str)
df_ant.fillna("", inplace=True)

df_ant.reset_index(drop=True, inplace=True)
df_ant['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ant['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_ant.to_csv("../csv-for-anki/grammar/df_ant.csv", sep="\t", index=None)

# df_adv_time
df_adv_time = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="adv_time", dtype=str)
df_adv_time.fillna("", inplace=True)

df_adv_time.reset_index(drop=True, inplace=True)
df_adv_time['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_adv_time['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_6_class

df_6_class = pd.concat([df_ar2_masc, df_ar_masc, df_u_masc, df_uu_masc, df_ant, df_adv_time])

df_6_class.to_csv("../csv-for-anki/grammar/gr_6_class.csv", sep="\t", index=None)


# df_aa_fem
df_aa_fem = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="aa_fem", dtype=str)
df_aa_fem.fillna("", inplace=True)

df_aa_fem.reset_index(drop=True, inplace=True)
df_aa_fem['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_aa_fem['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_aa_fem.to_csv("../csv-for-anki/grammar/df_aa_fem.csv", sep="\t", index=None)

# df_opt
df_opt = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="opt", dtype=str)
df_opt.fillna("", inplace=True)

df_opt.reset_index(drop=True, inplace=True)
df_opt['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_opt['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_opt.to_csv("../csv-for-anki/grammar/df_opt.csv", sep="\t", index=None)

# df_opt_be
df_opt_be = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="opt_be", dtype=str)
df_opt_be.fillna("", inplace=True)

df_opt_be.reset_index(drop=True, inplace=True)
df_opt_be['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_opt_be['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_opt_be.to_csv("../csv-for-anki/grammar/df_opt_be.csv", sep="\t", index=None)


# df_adv_place
df_adv_place = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="adv_place", dtype=str)
df_adv_place.fillna("", inplace=True)

df_adv_place.reset_index(drop=True, inplace=True)
df_adv_place['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_adv_place['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_ger
df_ger = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="ger", dtype=str)
df_ger.fillna("", inplace=True)

df_ger.reset_index(drop=True, inplace=True)
df_ger['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ger['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_abs
df_abs = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="abs", dtype=str)
df_abs.fillna("", inplace=True)

df_abs.reset_index(drop=True, inplace=True)
df_abs['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_abs['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_7_class

df_7_class = pd.concat([df_aa_fem, df_opt, df_opt_be, df_adv_place, df_abs, df_ger])

df_7_class.to_csv("../csv-for-anki/grammar/gr_7_class.csv", sep="\t", index=None)


# df_i_fem
df_i_fem = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="i_fem", dtype=str)
df_i_fem.fillna("", inplace=True)

df_i_fem.reset_index(drop=True, inplace=True)
df_i_fem['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_i_fem['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_i_fem.to_csv("../csv-for-anki/grammar/df_i_fem.csv", sep="\t", index=None)

# df_u_fem
df_u_fem = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="u_fem", dtype=str)
df_u_fem.fillna("", inplace=True)

df_u_fem.reset_index(drop=True, inplace=True)
df_u_fem['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_u_fem['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_u_fem.to_csv("../csv-for-anki/grammar/df_u_fem.csv", sep="\t", index=None)

# df_ar_fem
df_ar_fem = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="ar_fem", dtype=str)
df_ar_fem.fillna("", inplace=True)

df_ar_fem.reset_index(drop=True, inplace=True)
df_ar_fem['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ar_fem['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_inf
df_inf = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="inf", dtype=str)
df_inf.fillna("", inplace=True)

df_inf.reset_index(drop=True, inplace=True)
df_inf['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_inf['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""


# df_8_class

df_8_class = pd.concat([df_i_fem, df_u_fem, df_ar_fem, df_inf])

df_8_class.to_csv("../csv-for-anki/grammar/gr_8_class.csv", sep="\t", index=None)

# df_a_nt
df_a_nt = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="a_nt", dtype=str)
df_a_nt.fillna("", inplace=True)

df_a_nt.reset_index(drop=True, inplace=True)
df_a_nt['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_a_nt['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_i_nt
df_i_nt = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="i_nt", dtype=str)
df_i_nt.fillna("", inplace=True)

df_i_nt.reset_index(drop=True, inplace=True)
df_i_nt['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_i_nt['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_u_nt
df_u_nt = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="u_nt", dtype=str)
df_u_nt.fillna("", inplace=True)

df_u_nt.reset_index(drop=True, inplace=True)
df_u_nt['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_u_nt['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_adv_interr
df_adv_interr = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="adv_interr", dtype=str)
df_adv_interr.fillna("", inplace=True)

df_adv_interr.reset_index(drop=True, inplace=True)
df_adv_interr['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_adv_interr['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""


# df_9_class

df_9_class = pd.concat([df_a_nt, df_i_nt, df_u_nt, df_adv_interr])

df_9_class.to_csv("../csv-for-anki/grammar/gr_9_class.csv", sep="\t", index=None)

# df_ta_pron
df_ta_pron = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="ta_pron", dtype=str)
df_ta_pron.fillna("", inplace=True)

df_ta_pron.reset_index(drop=True, inplace=True)
df_ta_pron['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ta_pron['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_ima_pron
df_ima_pron = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="ima_pron", dtype=str)
df_ima_pron.fillna("", inplace=True)

df_ima_pron.reset_index(drop=True, inplace=True)
df_ima_pron['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ima_pron['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_a_pron
df_a_pron = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="a_pron", dtype=str)
df_a_pron.fillna("", inplace=True)

df_a_pron.reset_index(drop=True, inplace=True)
df_a_pron['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_a_pron['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_mana_prp
df_mana_prp = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="mana_prp", dtype=str)
df_mana_prp.fillna("", inplace=True)

df_mana_prp.reset_index(drop=True, inplace=True)
df_mana_prp['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_mana_prp['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_anta_prp
df_anta_prp = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="anta_prp", dtype=str)
df_anta_prp.fillna("", inplace=True)

df_anta_prp.reset_index(drop=True, inplace=True)
df_anta_prp['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_anta_prp['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_10_class

df_10_class = pd.concat([df_ta_pron, df_ima_pron, df_a_pron, df_mana_prp, df_anta_prp])

df_10_class.to_csv("../csv-for-anki/grammar/gr_10_class.csv", sep="\t", index=None)

# df_a_pp
df_a_pp = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="a_pp", dtype=str)
df_a_pp.fillna("", inplace=True)

df_a_pp.reset_index(drop=True, inplace=True)
df_a_pp['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_a_pp['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_a_adj
df_a_adj = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="a_adj", dtype=str)
df_a_adj.fillna("", inplace=True)

df_a_adj.reset_index(drop=True, inplace=True)
df_a_adj['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_a_adj['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_i_adj
df_i_adj = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="i_adj", dtype=str)
df_i_adj.fillna("", inplace=True)

df_i_adj.reset_index(drop=True, inplace=True)
df_i_adj['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_i_adj['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_u_adj
df_u_adj = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="u_adj", dtype=str)
df_u_adj.fillna("", inplace=True)

df_u_adj.reset_index(drop=True, inplace=True)
df_u_adj['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_u_adj['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_11_class

df_11_class = pd.concat([df_a_pp, df_a_adj, df_i_adj, df_u_adj])

df_11_class.to_csv("../csv-for-anki/grammar/gr_11_class.csv", sep="\t", index=None)

# df_card
df_card = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="card", dtype=str)
df_card.fillna("", inplace=True)

df_card.reset_index(drop=True, inplace=True)
df_card['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_card['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_a_card
df_a_card = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="a_card", dtype=str)
df_a_card.fillna("", inplace=True)

df_a_card.reset_index(drop=True, inplace=True)
df_a_card['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_a_card['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_i_card
df_i_card = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="i_card", dtype=str)
df_i_card.fillna("", inplace=True)

df_i_card.reset_index(drop=True, inplace=True)
df_i_card['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_i_card['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_ordin
df_ordin = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="ordin", dtype=str)
df_ordin.fillna("", inplace=True)

df_ordin.reset_index(drop=True, inplace=True)
df_ordin['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ordin['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_12_class

df_12_class = pd.concat([df_card, df_a_card, df_i_card, df_ordin])

df_12_class.to_csv("../csv-for-anki/grammar/gr_12_class.csv", sep="\t", index=None)

# df_adv
df_adv = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="adv", dtype=str)
df_adv.fillna("", inplace=True)

df_adv.reset_index(drop=True, inplace=True)
df_adv['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_adv['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_13_class

df_13_class = pd.concat([df_adv])

df_13_class.to_csv("../csv-for-anki/grammar/gr_13_class.csv", sep="\t", index=None)


# df_a_ptp
df_a_ptp = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="a_ptp", dtype=str)
df_a_ptp.fillna("", inplace=True)

df_a_ptp.reset_index(drop=True, inplace=True)
df_a_ptp['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_a_ptp['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_14_class

df_14_class = pd.concat([df_a_ptp])

df_14_class.to_csv("../csv-for-anki/grammar/gr_14_class.csv", sep="\t", index=None)

# df_v_sandhi
df_v_sandhi = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="v_sandhi", dtype=str)
df_v_sandhi.fillna("", inplace=True)

df_v_sandhi.reset_index(drop=True, inplace=True)
df_v_sandhi['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_v_sandhi['example'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_16_class

df_16_class = pd.concat([df_v_sandhi])

df_16_class.to_csv("../csv-for-anki/grammar/gr_16_class.csv", sep="\t", index=None)

# df_c_sandhi
df_c_sandhi = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="c_sandhi", dtype=str)
df_c_sandhi.fillna("", inplace=True)

df_c_sandhi.reset_index(drop=True, inplace=True)
df_c_sandhi['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_c_sandhi['example'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_m_sandhi
df_m_sandhi = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="m_sandhi", dtype=str)
df_m_sandhi.fillna("", inplace=True)

df_m_sandhi.reset_index(drop=True, inplace=True)
df_m_sandhi['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_m_sandhi['example'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_alph
df_alph = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="alph", dtype=str)
df_alph.fillna("", inplace=True)

df_alph.reset_index(drop=True, inplace=True)
df_alph['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_alph['abbrev'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""


# df_17_class

df_17_class = pd.concat([df_c_sandhi, df_m_sandhi])

df_17_class.to_csv("../csv-for-anki/grammar/gr_17_class.csv", sep="\t", index=None)

df_17_class_a = pd.concat([df_alph])

df_17_class_a.to_csv("../csv-for-anki/grammar/gr_17_class_a.csv", sep="\t", index=None)

# df_assim
df_assim = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="assim", dtype=str)
df_assim.fillna("", inplace=True)

df_assim.reset_index(drop=True, inplace=True)
df_assim['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_assim['example'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_mx_sandhi
df_mx_sandhi = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="mx_sandhi", dtype=str)
df_mx_sandhi.fillna("", inplace=True)

df_mx_sandhi.reset_index(drop=True, inplace=True)
df_mx_sandhi['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_mx_sandhi['example'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_as_masc
df_as_masc = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="as_masc", dtype=str)
df_as_masc.fillna("", inplace=True)

df_as_masc.reset_index(drop=True, inplace=True)
df_as_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_as_masc['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_go_masc
df_go_masc = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="go_masc", dtype=str)
df_go_masc.fillna("", inplace=True)

df_go_masc.reset_index(drop=True, inplace=True)
df_go_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_go_masc['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>.""" 

# df_a2_masc
df_a2_masc = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="a2_masc", dtype=str)
df_a2_masc.fillna("", inplace=True)

df_a2_masc.reset_index(drop=True, inplace=True)
df_a2_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_a2_masc['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_raja_masc
df_raja_masc = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="raja_masc", dtype=str)
df_raja_masc.fillna("", inplace=True)

df_raja_masc.reset_index(drop=True, inplace=True)
df_raja_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_raja_masc['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_18_class

df_18_class = pd.concat([df_as_masc, df_go_masc, df_a2_masc, df_raja_masc])

df_18_class.to_csv("../csv-for-anki/grammar/gr_18_class.csv", sep="\t", index=None)


df_18_class_s = pd.concat([df_assim, df_mx_sandhi])

df_18_class_s.to_csv("../csv-for-anki/grammar/gr_18_class_s.csv", sep="\t", index=None)

# df_samasa
df_samasa = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="samasa", dtype=str)
df_samasa.fillna("", inplace=True)

df_samasa.reset_index(drop=True, inplace=True)
df_samasa['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_samasa['abbrev'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_19_class

df_19_class = pd.concat([df_samasa])

df_19_class.to_csv("../csv-for-anki/grammar/gr_19_class.csv", sep="\t", index=None)

# df_change_s
df_change_s = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="change_s", dtype=str)
df_change_s.fillna("", inplace=True)

df_change_s.reset_index(drop=True, inplace=True)
df_change_s['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_change_s['example'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_20_class

df_20_class = pd.concat([df_change_s])

df_20_class.to_csv("../csv-for-anki/grammar/gr_20_class.csv", sep="\t", index=None)

# df_reflx
df_reflx = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="reflx", dtype=str)
df_reflx.fillna("", inplace=True)

df_reflx.reset_index(drop=True, inplace=True)
df_reflx['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_reflx['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_perf
df_perf = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="perf", dtype=str)
df_perf.fillna("", inplace=True)

df_perf.reset_index(drop=True, inplace=True)
df_perf['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_perf['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_21_class

df_21_class = pd.concat([df_reflx, df_perf])

df_21_class.to_csv("../csv-for-anki/grammar/gr_21_class.csv", sep="\t", index=None)

# df_cond
df_cond = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="cond", dtype=str)
df_cond.fillna("", inplace=True)

df_cond.reset_index(drop=True, inplace=True)
df_cond['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_cond['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_irr_base
df_irr_base = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="irr_base", dtype=str)
df_irr_base.fillna("", inplace=True)

df_irr_base.reset_index(drop=True, inplace=True)
df_irr_base['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_irr_base['result'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_22_class

df_22_class = pd.concat([df_cond])

df_22_class.to_csv("../csv-for-anki/grammar/gr_22_class.csv", sep="\t", index=None)

df_22_class_s = pd.concat([df_irr_base])

df_22_class_s.to_csv("../csv-for-anki/grammar/gr_22_class_s.csv", sep="\t", index=None)


# df_upasagga
df_upasagga = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="upasagga", dtype=str)
df_upasagga.fillna("", inplace=True)

df_upasagga.reset_index(drop=True, inplace=True)
df_upasagga['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_upasagga['abbrev'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

test1 = df_upasagga['example'] != ""
filter = test1
df_upasagga = df_upasagga.loc[filter]

# df_23_class

df_23_class = pd.concat([df_upasagga])

df_23_class.to_csv("../csv-for-anki/grammar/gr_23_class.csv", sep="\t", index=None)

# df_app
df_app = pd.read_excel("../pāli-course/grammar.xlsx", sheet_name="app", dtype=str)
df_app.fillna("", inplace=True)

df_app.reset_index(drop=True, inplace=True)
df_app['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_app['pali'] + """&entry.644913945=Anki Deck Grammar Pāli Course">Fix it here</a>."""

# df_24_class

df_24_class = pd.concat([df_app])

df_24_class.to_csv("../csv-for-anki/grammar/gr_24_class.csv", sep="\t", index=None)


# concat df_sum_abbr

df_sum_abbr = pd.concat([df_abbr_class, df_alph, df_samasa, df_upasagga
])

df_sum_abbr.to_csv("../csv-for-anki/grammar/gr_sum_abbr.csv", sep="\t", index=None)

# concat df_sum_gramm

df_sum_gramm = pd.concat([df_a_masc, df_pr, df_4_class, df_5_class, df_6_class, df_7_class, df_8_class, df_9_class, df_10_class, df_11_class, df_12_class, df_13_class, df_14_class, df_18_class, df_21_class, df_22_class, df_24_class])

df_sum_gramm.to_csv("../csv-for-anki/grammar/gr_sum_gramm.csv", sep="\t", index=None)

# concat df_sum_sandhi

df_sum_sandhi = pd.concat([df_16_class, df_17_class, df_18_class_s, df_change_s, df_irr_base])

df_sum_sandhi.to_csv("../csv-for-anki/grammar/gr_sum_sandhi.csv", sep="\t", index=None)

# for ID inserstion

# concat df_sum_abbr before 21

# df_upd_sum_abbr = pd.concat([df_abbr_class, df_alph, df_samasa])

# df_upd_sum_abbr.to_csv("../csv-for-anki/grammar/upd_gr_sum_abbr.csv", sep="\t", index=None)

# df_upd_sum_abbr_ID = df_upd_sum_abbr[['abbrev', 'meaning', 'pāli', 'example', 'explanation', 'pattern', 'id']]

# df_upd_sum_abbr_ID.to_csv("../csv-for-anki/grammar/upd_gr_sum_abbr_ID.csv", sep="\t", index=None)

# # concat df_sum_gramm before 21

# df_upd_sum_gramm = pd.concat([df_a_masc, df_pr, df_4_class, df_5_class, df_6_class, df_7_class, df_8_class, df_9_class, df_10_class, df_11_class, df_12_class, df_13_class, df_14_class, df_18_class, df_21_class])

# df_upd_sum_gramm.to_csv("../csv-for-anki/grammar/upd_gr_sum_gramm.csv", sep="\t", index=None)

# df_upd_sum_gramm_ID = df_upd_sum_gramm[['pali', 'gram', 'of', 'transl', 'decl-con', 'pattern', 'id']]

# df_upd_sum_gramm_ID.to_csv("../csv-for-anki/grammar/upd_gr_sum_gramm_ID.csv", sep="\t", index=None)

# # concat df_sum_sandhi before 21

# df_upd_sum_sandhi = pd.concat([df_16_class, df_17_class, df_18_class_s, df_change_s])

# df_upd_sum_sandhi.to_csv("../csv-for-anki/grammar/upd_gr_sum_sandhi.csv", sep="\t", index=None)

# df_upd_sum_sandhi_ID = df_upd_sum_sandhi[['example', 'sandhi', 'details', 'result', 'meeting', 'pattern', 'id']]

# df_upd_sum_sandhi_ID.to_csv("../csv-for-anki/grammar/upd_gr_sum_sandhi_ID.csv", sep="\t", index=None)

