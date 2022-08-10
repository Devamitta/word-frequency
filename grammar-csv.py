import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re
import sys

# df_abbr
df_abbr = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="abbr", dtype=str)
df_abbr.fillna("", inplace=True)

df_abbr.to_csv("grammar-csv/df_abbr.csv", sep="\t", index=None)

# df_a_masc
df_a_masc = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="a_masc", dtype=str)
df_a_masc.fillna("", inplace=True)

df_a_masc.to_csv("grammar-csv/df_a_masc.csv", sep="\t", index=None)

# df_pr
df_pr = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="pr", dtype=str)
df_pr.fillna("", inplace=True)

df_pr.to_csv("grammar-csv/df_pr.csv", sep="\t", index=None)

# df_pr_aor_be
df_pr_aor_be = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="pr_aor_be", dtype=str)
df_pr_aor_be.fillna("", inplace=True)

df_pr_aor_be.to_csv("grammar-csv/df_pr_aor_be.csv", sep="\t", index=None)

# df_aor
df_aor = pd.read_excel("pāli-course/grammar.xlsx", sheet_name="aor", dtype=str)
df_aor.fillna("", inplace=True)

df_aor.to_csv("grammar-csv/df_aor.csv", sep="\t", index=None)


