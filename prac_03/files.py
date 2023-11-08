"""
CP1404 Practical 03 Hunter Kruger-Ilingworth
1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
Remember to close your file.

2. (In the same file, but as if it were a separate program) Write code that opens "name.txt" and reads the name (as
above) then prints, "Your name is Bob" (or whatever the name is in the file).

3. Create a text file called numbers.txt and save it in your prac directory. Put the following three numbers on separate
lines in the file and save it: 17 42 400 Write code that opens "numbers.txt", reads only the first two numbers and
adds them together then prints the result, which should be... 59.

4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file with any number of
numbers."""

name_file = "name.txt"
number_file = "numbers.txt"

# 1)
name = input("What is your name? ")
with open(name_file, "w") as file:
    print(f"{name}", file=file)

# 2)
with open(name_file, "r") as file:
    name = file.read()
    print(f"Your name is {name}")

# 3 & 4)
numbers = []
with open(number_file, "r") as file:
    for line in file:
        numbers.append(int(line.strip()))  # written in a way that is easily extendable for future functionality
result = numbers[0] + numbers[1]
print(result)
print(sum(numbers))
