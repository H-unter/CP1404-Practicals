"""
Word Occurrences
Estimate: 35 minutes
Actual: 5 minutes
8:18 start
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
