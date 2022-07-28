import pandas as pd
import numpy as np
from pandas_ods_reader import read_ods 
import re


# read ods df_a_masc
df_a_masc = pd.read_excel("original-sources/grammar.xlsx", sheet_name="a-masc", dtype=str)
df_a_masc.fillna("", inplace=True)
# df_a_masc = pd.read_excel("declensions & conjugations.xlsx", sheet_name="index", dtype=str)

# adding feedback df_a_masc
df_a_masc.reset_index(drop=True, inplace=True)
df_a_masc['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df_a_masc.pali + """&entry.1433863141=Pāli Class Grammar">Fix it here</a>."""

# save csv df_a_masc
df_a_masc.to_csv("grammar-csv/df_a_masc.csv", sep="\t", index=None)

# read ods df_pr
df_pr = pd.read_excel("original-sources/grammar.xlsx", sheet_name="pr", dtype=str)
df_pr.fillna("", inplace=True)

# adding feedback
df_pr.reset_index(drop=True, inplace=True)
df_pr['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df_pr.pali + """&entry.1433863141=Pāli Class Grammar">Fix it here</a>."""

# save csv df_pr
df_pr.to_csv("grammar-csv/df_pr.csv", sep="\t", index=None)

# read ods df_pr_be
df_pr_be = pd.read_excel("original-sources/grammar.xlsx", sheet_name="pr-be", dtype=str)
df_pr_be.fillna("", inplace=True)

# adding feedback df_pr_be
df_pr_be.reset_index(drop=True, inplace=True)
df_pr_be['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + df_pr_be.pali + """&entry.1433863141=Pāli Class Grammar">Fix it here</a>."""

# save csv df_pr_be
df_pr_be.to_csv("grammar-csv/df_pr_be.csv", sep="\t", index=None)

