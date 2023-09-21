import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

# Sample list of words
words = ["round", "black", "walk", "apple"]

for word in words:
    synsets = wordnet.synsets(word)
    if synsets:
        synset = synsets[0]  # Consider the first synset for simplicity
        pos = synset.pos()
        print(f"{word} - Part of Speech: {pos}")
    else:
        print(f"{word} - No synsets found")
