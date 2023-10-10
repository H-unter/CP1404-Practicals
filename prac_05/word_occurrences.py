"""
Word Occurrences
Estimate: 35 minutes
Actual: 5 minutes
"""

sentence = input("Text: ").strip().split(" ")  # error check
word_to_frequency = {}
for word in sentence:
    if word in list(word_to_frequency.keys()):
        word_to_frequency[word] += 1
    else:
        word_to_frequency[word] = 1

print(word_to_frequency)
