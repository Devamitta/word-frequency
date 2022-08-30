import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
import sys
import csv

# df_abbr
df_abbr = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="abbr", dtype=str)
df_abbr.fillna("", inplace=True)

df_abbr_dps = df_abbr[['abbrev', 'meaning', 'pāli', 'ru_meaning', 'example', 'explanation']]

df_abbr_dps.to_csv("../exporter/assets/abbreviations.csv", sep="\t", index=None)

test1 = df_abbr['type'] != ""
filter = test1
df_abbr_class = df_abbr.loc[filter]

df_abbr_class = df_abbr_class[['abbrev', 'meaning', 'pāli', 'example', 'explanation']]

df_abbr_class.to_excel("../csv-for-anki/abbr.xlsx", index=None)

# adding feedback
df_abbr_class.reset_index(drop=True, inplace=True)
df_abbr_class['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_abbr_class['abbrev'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

df_abbr_class.to_csv("../csv-for-anki/grammar/df_abbr.csv", sep="\t", index=None)

# df_a_masc
df_a_masc = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="a_masc", dtype=str)
df_a_masc.fillna("", inplace=True)

df_a_masc.reset_index(drop=True, inplace=True)
df_a_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_a_masc['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

df_a_masc.to_csv("../csv-for-anki/grammar/df_a_masc.csv", sep="\t", index=None)

# df_pr
df_pr = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="pr", dtype=str)
df_pr.fillna("", inplace=True)

df_pr.reset_index(drop=True, inplace=True)
df_pr['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_pr['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

df_pr.to_csv("../csv-for-anki/grammar/df_pr.csv", sep="\t", index=None)

# df_pr_aor_be
df_pr_aor_be = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="pr_aor_be", dtype=str)
df_pr_aor_be.fillna("", inplace=True)

df_pr_aor_be.reset_index(drop=True, inplace=True)
df_pr_aor_be['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_pr_aor_be['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

df_pr_aor_be.to_csv("../csv-for-anki/grammar/df_pr_aor_be.csv", sep="\t", index=None)

# df_aor
df_aor = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="aor", dtype=str)
df_aor.fillna("", inplace=True)

df_aor.reset_index(drop=True, inplace=True)
df_aor['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_aor['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

df_aor.to_csv("../csv-for-anki/grammar/df_aor.csv", sep="\t", index=None)

# df_i_masc
df_i_masc = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="i_masc", dtype=str)
df_i_masc.fillna("", inplace=True)

df_i_masc.reset_index(drop=True, inplace=True)
df_i_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSc0KxEDyN5G2Mqr4t3AvDpXxSOIbIBi0GrZsAGhDB207sjLow/viewform?usp=pp_url&entry.438735500=""" + df_i_masc['pali'] + """&entry.644913945=Anki Deck Grammar Beginner Pāli Course">Fix it here</a>."""

df_i_masc.to_csv("../csv-for-anki/grammar/df_i_masc.csv", sep="\t", index=None)

df_4_class = pd.concat([df_i_masc, df_aor, df_pr_aor_be])

df_4_class.to_csv("../csv-for-anki/grammar/gr_4_class.csv", sep="\t", index=None)


