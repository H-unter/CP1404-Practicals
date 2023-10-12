"""
CP1404 Practical 05 Hunter Kruger-Ilingworth
Program to determine word occurrences for a given sentence
Estimate: 35 minutes
Actual: 11 minutes
"""

sentence = input("Text: ").strip().split(" ")  # error check
word_to_frequency = {}
largest_word_length = max(len(word) for word in sentence)

for word in sentence:
    if word in list(word_to_frequency.keys()):
        word_to_frequency[word] += 1
    else:
        word_to_frequency[word] = 1
for word, frequency in word_to_frequency.items():
    print(f"{word:{largest_word_length}} : {frequency}")
