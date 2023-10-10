"""
Word Occurrences
Estimate: 35 minutes
Actual:    minutes
start 8:18am
"""

sentence = input("Text: ").strip().split(" ")  # error check
word_to_frequency = {}
for word in sentence:
    if word in list(word_to_frequency.keys()):
        print("DETECTED!")
        word_to_frequency[word] += 1
    else:
        print("NEW WORD!")
        word_to_frequency[word] = 1
