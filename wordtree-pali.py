#!/usr/bin/env python3.10
# coding: utf-8

from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from wordtree import search_and_draw
import pandas as pd

# open ebts_REPLACED.txt
with open ("curated-sources/ebts_REPLACED.txt", "r") as f:
	text = str(f.read())

# open ebt freq csv and make a list
ebt_freq_df = pd.read_csv("csv-for-pic/class2.csv", sep="\t", dtype= str)
ebt_freq_df['Pāli1'] = ebt_freq_df['Pāli1'].str.replace('\d+', '')
ebt_freq_df['Pāli1'] = ebt_freq_df['Pāli1'].str.replace(' ', '')
df_length = ebt_freq_df.shape[0]
ebt_freq_list = ebt_freq_df['Pāli1'].to_list()
print(ebt_freq_list[:200])

# make ngrams
def get_ngrams(text, n):
    n_grams = ngrams(word_tokenize(text), n)
    return [ ' '.join(grams) for grams in n_grams]
ngrams_text = get_ngrams(text, 3)
# print(ngrams_text)

for row in range(200):
    word = ebt_freq_list[row]
    g = search_and_draw(corpus=ngrams_text, keyword=word, max_n=3)
    g.render(f"pics-wordtree/class2/{word}") 
