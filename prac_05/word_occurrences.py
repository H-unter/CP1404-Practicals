"""
CP1404 Practical 05 Hunter Kruger-Ilingworth
Program to determine word occurrences for a given sentence
Estimate: 35 minutes
Actual: 11 minutes
"""

words = input("Text: ").strip().split(" ")
word_to_frequency = {}
largest_word_length = max(len(word) for word in words)

for word in words:
    if word in list(word_to_frequency.keys()):
        word_to_frequency[word] += 1
    else:
        word_to_frequency[word] = 1

words = list(word_to_frequency.keys())
words.sort()
for word in words:
    print(f"{word:{largest_word_length}} : {word_to_frequency[word]}")
