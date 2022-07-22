import pandas as pd
import csv
import re

# opening words for current class
sum_df = pd.read_csv("frequent-words/summary.csv", header = None, index_col=None, sep="\t")
sum_length = len(sum_df)

# opening dpd_df
dpd_df = pd.read_csv("../spreadsheets/nidh_bold.csv", index_col=None, sep="\t", dtype=str)
dpd_df.fillna("", inplace=True)
dpd_df_length = len(dpd_df)

# opening words which already exists
class_df = pd.read_csv("../spreadsheets/class-vocab.csv", index_col=None, sep="\t", dtype=str)
class_df.fillna("", inplace=True)
class_df_length = len(class_df)

add_df = pd.DataFrame()

missing = open("output/missing.csv", "w")
missing.write(f"pali\tpattern\n")

used_patterns = []

#processing sum_length

for row in range(sum_length): #sum_length
	
	word = sum_df.iloc[row, 0]
	patt = sum_df.iloc[row, 1]
	count = sum_df.iloc[row, 2]

	word_dpd = sum_df.iloc[row, 0]
	patt_dpd = sum_df.iloc[row, 37]

	if word == dpd_df['Pāli1'] and patt == dpd_df['Pattern']:
		used_patterns.append(headword)
		test1 = dpd_df['Pāli1'] == headword
		test2 = dpd_df['Meaning IN CONTEXT'] != ""
		test3 = dpd_df['Source1'] != ""
		filter = test1 & test2 & test3
		dpd_row = dpd_df.loc[filter]

		if word != class_df['Pāli1'] and patt != class_df['Pattern']:
			class_df = class_df.append([dpd_row])

	else:
		if not re.findall(fr"\d", headword) or \
		re.findall("1", headword):
			missing.write(f"{word}\t{headword}\n")

output_file = "../spreadsheets/add-to-class.csv"

# adding feedback
class_df.reset_index(drop=True, inplace=True)
class_df['Feedback'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLScNC5v2gQbBCM3giXfYIib9zrp-WMzwJuf_iVXEMX2re4BFFw/viewform?usp=pp_url&entry.438735500=""" + class_df.Pāli1 + """&entry.1433863141=Pāli Class">Fix it here</a>."""

class_df.to_csv(output_file, sep="\t", index = None, header=None)
missing.close()