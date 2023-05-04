
#import necessary libraries
import nltk
from nltk.util import ngrams
from collections import Counter
import random

# load list of names

with open('names.txt',"r") as file:
    names = [name.rstrip() for name in file.readlines()]

# create bigrams from names
bigrams = []
for name in names:
    name_bigrams = list(ngrams(name, 2, pad_left=True, pad_right=True))
    bigrams += name_bigrams

# count occurrence of bigrams
bigram_counts = Counter(bigrams)

# calculate probability of each bigram
bigram_prob = {}
for bigram, count in bigram_counts.items():
    preceding_letter = bigram[0]
    prob = count / sum(bigram_counts[ngram] for ngram in bigram_counts.keys() if ngram[0] == preceding_letter)
    bigram_prob[bigram] = prob
