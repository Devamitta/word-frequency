import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
import sys
import csv

# df_abbr
df_abbr = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="abbr", dtype=str)
df_abbr.fillna("", inplace=True)

df_abbr_dps = df_abbr[['abbrev', 'meaning', 'pāli', 'ru-meaning', 'example', 'explanation', 'ru-abbrev']]

df_abbr_dps.to_csv("../exporter/assets/abbreviations.csv", sep="\t", index=None)

test1 = df_abbr['type'] != ""
filter = test1
df_abbr_class = df_abbr.loc[filter]

df_abbr_class = df_abbr_class[['abbrev', 'meaning', 'pāli', 'example', 'explanation']]

df_abbr_class.to_excel("../csv-for-anki/abbr.xlsx", index=None)

# adding feedback
df_abbr_class.reset_index(drop=True, inplace=True)
df_abbr_class['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_abbr_class['abbrev'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

df_abbr_class.to_csv("../csv-for-anki/grammar/gr_1_class.csv", sep="\t", index=None)

# df_a_masc
df_a_masc = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="a_masc", dtype=str)
df_a_masc.fillna("", inplace=True)

df_a_masc.reset_index(drop=True, inplace=True)
df_a_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_a_masc['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

df_a_masc.to_csv("../csv-for-anki/grammar/gr_2_class.csv", sep="\t", index=None)

# df_pr
df_pr = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="pr", dtype=str)
df_pr.fillna("", inplace=True)

df_pr.reset_index(drop=True, inplace=True)
df_pr['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_pr['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

df_pr.to_csv("../csv-for-anki/grammar/gr_3_class.csv", sep="\t", index=None)

# df_pr_aor_be
df_pr_aor_be = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="pr_aor_be", dtype=str)
df_pr_aor_be.fillna("", inplace=True)

df_pr_aor_be.reset_index(drop=True, inplace=True)
df_pr_aor_be['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_pr_aor_be['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_pr_aor_be.to_csv("../csv-for-anki/grammar/df_pr_aor_be.csv", sep="\t", index=None)

# df_aor
df_aor = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="aor", dtype=str)
df_aor.fillna("", inplace=True)

df_aor.reset_index(drop=True, inplace=True)
df_aor['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_aor['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_aor.to_csv("../csv-for-anki/grammar/df_aor.csv", sep="\t", index=None)

# df_i_masc
df_i_masc = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="i_masc", dtype=str)
df_i_masc.fillna("", inplace=True)

df_i_masc.reset_index(drop=True, inplace=True)
df_i_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_i_masc['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_i_masc.to_csv("../csv-for-anki/grammar/df_i_masc.csv", sep="\t", index=None)

# df_4_class

df_4_class = pd.concat([df_i_masc, df_aor, df_pr_aor_be])

df_4_class.to_csv("../csv-for-anki/grammar/gr_4_class.csv", sep="\t", index=None)

# df_fut
df_fut = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="fut", dtype=str)
df_fut.fillna("", inplace=True)

df_fut.reset_index(drop=True, inplace=True)
df_fut['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_fut['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_fut.to_csv("../csv-for-anki/grammar/df_fut.csv", sep="\t", index=None)

# df_ii_masc
df_ii_masc = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="ii_masc", dtype=str)
df_ii_masc.fillna("", inplace=True)

df_ii_masc.reset_index(drop=True, inplace=True)
df_ii_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ii_masc['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_ii_masc.to_csv("../csv-for-anki/grammar/df_ii_masc.csv", sep="\t", index=None)

# df_pers_pron
df_pers_pron = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="pers_pron", dtype=str)
df_pers_pron.fillna("", inplace=True)

df_pers_pron.reset_index(drop=True, inplace=True)
df_pers_pron['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_pers_pron['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_pers_pron.to_csv("../csv-for-anki/grammar/df_pers_pron.csv", sep="\t", index=None)

# df_5_class

df_5_class = pd.concat([df_ii_masc, df_fut, df_pers_pron])

df_5_class.to_csv("../csv-for-anki/grammar/gr_5_class.csv", sep="\t", index=None)


# df_u_masc
df_u_masc = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="u_masc", dtype=str)
df_u_masc.fillna("", inplace=True)

df_u_masc.reset_index(drop=True, inplace=True)
df_u_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_u_masc['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_u_masc.to_csv("../csv-for-anki/grammar/df_u_masc.csv", sep="\t", index=None)


# df_ar_masc
df_ar_masc = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="ar_masc", dtype=str)
df_ar_masc.fillna("", inplace=True)

df_ar_masc.reset_index(drop=True, inplace=True)
df_ar_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ar_masc['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_ar_masc.to_csv("../csv-for-anki/grammar/df_ar_masc.csv", sep="\t", index=None)

# df_ar2_masc
df_ar2_masc = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="ar2_masc", dtype=str)
df_ar2_masc.fillna("", inplace=True)

df_ar2_masc.reset_index(drop=True, inplace=True)
df_ar2_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ar2_masc['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_ar2_masc.to_csv("../csv-for-anki/grammar/df_ar2_masc.csv", sep="\t", index=None)

# df_uu_masc
df_uu_masc = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="uu_masc", dtype=str)
df_uu_masc.fillna("", inplace=True)

df_uu_masc.reset_index(drop=True, inplace=True)
df_uu_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_uu_masc['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_uu_masc.to_csv("../csv-for-anki/grammar/df_uu_masc.csv", sep="\t", index=None)

# df_ant
df_ant = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="ant", dtype=str)
df_ant.fillna("", inplace=True)

df_ant.reset_index(drop=True, inplace=True)
df_ant['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ant['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_ant.to_csv("../csv-for-anki/grammar/df_ant.csv", sep="\t", index=None)


# df_6_class

df_6_class = pd.concat([df_ar2_masc, df_ar_masc, df_u_masc, df_uu_masc, df_ant])

df_6_class.to_csv("../csv-for-anki/grammar/gr_6_class.csv", sep="\t", index=None)


# df_aa_fem
df_aa_fem = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="aa_fem", dtype=str)
df_aa_fem.fillna("", inplace=True)

df_aa_fem.reset_index(drop=True, inplace=True)
df_aa_fem['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_aa_fem['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_aa_fem.to_csv("../csv-for-anki/grammar/df_aa_fem.csv", sep="\t", index=None)

# df_opt
df_opt = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="opt", dtype=str)
df_opt.fillna("", inplace=True)

df_opt.reset_index(drop=True, inplace=True)
df_opt['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_opt['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_opt.to_csv("../csv-for-anki/grammar/df_opt.csv", sep="\t", index=None)

# df_opt_be
df_opt_be = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="opt_be", dtype=str)
df_opt_be.fillna("", inplace=True)

df_opt_be.reset_index(drop=True, inplace=True)
df_opt_be['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_opt_be['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_opt_be.to_csv("../csv-for-anki/grammar/df_opt_be.csv", sep="\t", index=None)

# df_7_class

df_7_class = pd.concat([df_aa_fem, df_opt, df_opt_be])

df_7_class.to_csv("../csv-for-anki/grammar/gr_7_class.csv", sep="\t", index=None)


# df_i_fem
df_i_fem = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="i_fem", dtype=str)
df_i_fem.fillna("", inplace=True)

df_i_fem.reset_index(drop=True, inplace=True)
df_i_fem['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_i_fem['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_i_fem.to_csv("../csv-for-anki/grammar/df_i_fem.csv", sep="\t", index=None)

# df_u_fem
df_u_fem = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="u_fem", dtype=str)
df_u_fem.fillna("", inplace=True)

df_u_fem.reset_index(drop=True, inplace=True)
df_u_fem['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_u_fem['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_u_fem.to_csv("../csv-for-anki/grammar/df_u_fem.csv", sep="\t", index=None)

# df_ar_fem
df_ar_fem = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="ar_fem", dtype=str)
df_ar_fem.fillna("", inplace=True)

df_ar_fem.reset_index(drop=True, inplace=True)
df_ar_fem['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ar_fem['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_ar_fem.to_csv("../csv-for-anki/grammar/df_ar_fem.csv", sep="\t", index=None)

# df_8_class

df_8_class = pd.concat([df_i_fem, df_u_fem, df_ar_fem])

df_8_class.to_csv("../csv-for-anki/grammar/gr_8_class.csv", sep="\t", index=None)

# df_a_nt
df_a_nt = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="a_nt", dtype=str)
df_a_nt.fillna("", inplace=True)

df_a_nt.reset_index(drop=True, inplace=True)
df_a_nt['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_a_nt['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_i_nt
df_i_nt = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="i_nt", dtype=str)
df_i_nt.fillna("", inplace=True)

df_i_nt.reset_index(drop=True, inplace=True)
df_i_nt['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_i_nt['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_u_nt
df_u_nt = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="u_nt", dtype=str)
df_u_nt.fillna("", inplace=True)

df_u_nt.reset_index(drop=True, inplace=True)
df_u_nt['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_u_nt['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_9_class

df_9_class = pd.concat([df_a_nt, df_i_nt, df_u_nt])

df_9_class.to_csv("../csv-for-anki/grammar/gr_9_class.csv", sep="\t", index=None)

# df_ta_pron
df_ta_pron = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="ta_pron", dtype=str)
df_ta_pron.fillna("", inplace=True)

df_ta_pron.reset_index(drop=True, inplace=True)
df_ta_pron['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ta_pron['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_ima_pron
df_ima_pron = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="ima_pron", dtype=str)
df_ima_pron.fillna("", inplace=True)

df_ima_pron.reset_index(drop=True, inplace=True)
df_ima_pron['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ima_pron['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_a_pron
df_a_pron = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="a_pron", dtype=str)
df_a_pron.fillna("", inplace=True)

df_a_pron.reset_index(drop=True, inplace=True)
df_a_pron['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_a_pron['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_mana_prp
df_mana_prp = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="mana_prp", dtype=str)
df_mana_prp.fillna("", inplace=True)

df_mana_prp.reset_index(drop=True, inplace=True)
df_mana_prp['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_mana_prp['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_anta_prp
df_anta_prp = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="anta_prp", dtype=str)
df_anta_prp.fillna("", inplace=True)

df_anta_prp.reset_index(drop=True, inplace=True)
df_anta_prp['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_anta_prp['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_10_class

df_10_class = pd.concat([df_ta_pron, df_ima_pron, df_a_pron, df_mana_prp, df_anta_prp])

df_10_class.to_csv("../csv-for-anki/grammar/gr_10_class.csv", sep="\t", index=None)

# df_a_pp
df_a_pp = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="a_pp", dtype=str)
df_a_pp.fillna("", inplace=True)

df_a_pp.reset_index(drop=True, inplace=True)
df_a_pp['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_a_pp['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_a_adj
df_a_adj = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="a_adj", dtype=str)
df_a_adj.fillna("", inplace=True)

df_a_adj.reset_index(drop=True, inplace=True)
df_a_adj['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_a_adj['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_i_adj
df_i_adj = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="i_adj", dtype=str)
df_i_adj.fillna("", inplace=True)

df_i_adj.reset_index(drop=True, inplace=True)
df_i_adj['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_i_adj['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_u_adj
df_u_adj = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="u_adj", dtype=str)
df_u_adj.fillna("", inplace=True)

df_u_adj.reset_index(drop=True, inplace=True)
df_u_adj['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_u_adj['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_11_class

df_11_class = pd.concat([df_a_pp, df_a_adj, df_i_adj, df_u_adj])

df_11_class.to_csv("../csv-for-anki/grammar/gr_11_class.csv", sep="\t", index=None)

# df_card
df_card = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="card", dtype=str)
df_card.fillna("", inplace=True)

df_card.reset_index(drop=True, inplace=True)
df_card['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_card['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_a_card
df_a_card = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="a_card", dtype=str)
df_a_card.fillna("", inplace=True)

df_a_card.reset_index(drop=True, inplace=True)
df_a_card['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_a_card['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_i_card
df_i_card = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="i_card", dtype=str)
df_i_card.fillna("", inplace=True)

df_i_card.reset_index(drop=True, inplace=True)
df_i_card['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_i_card['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_ordin
df_ordin = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="ordin", dtype=str)
df_ordin.fillna("", inplace=True)

df_ordin.reset_index(drop=True, inplace=True)
df_ordin['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_ordin['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_12_class

df_12_class = pd.concat([df_card, df_a_card, df_i_card, df_ordin])

df_12_class.to_csv("../csv-for-anki/grammar/gr_12_class.csv", sep="\t", index=None)

# df_a_ptp
df_a_ptp = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="a_ptp", dtype=str)
df_a_ptp.fillna("", inplace=True)

df_a_ptp.reset_index(drop=True, inplace=True)
df_a_ptp['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_a_ptp['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

# df_14_class

df_14_class = pd.concat([df_a_ptp])

df_14_class.to_csv("../csv-for-anki/grammar/gr_14_class.csv", sep="\t", index=None)
