
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

# generate a name using the bigram language model
seed_letter = None
generated_name = ''
while True:
    if not seed_letter:
        # choose a random first letter as seed
        seed_letter = random.choice([name[0] for name in names])
        generated_name += seed_letter
    else:
        # choose the next letter based on the probability distribution of bigrams
        next_letter_candidates = [(bigram[1], prob) for bigram, prob in bigram_prob.items() if bigram[0] == seed_letter]
        if not next_letter_candidates:
            # if no bigram found with the current seed letter, choose another seed letter
            seed_letter = None
            continue
        next_letter = random.choices(population=[letter[0] for letter in next_letter_candidates],
                                      weights=[letter[1] for letter in next_letter_candidates],
                                      k=1)[0]
        generated_name += next_letter
        seed_letter = next_letter
        if seed_letter in ['a', 'e', 'i', 'o', 'u', 'y']:
            # stop generating the name when the next letter is a vowel
            break

# print(bigram_prob)
print(generated_name.capitalize())
