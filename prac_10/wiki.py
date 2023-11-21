import wikipedia

query = input("Search Wikipedia: ")
while query != "":
    print(wikipedia.summary(query))
    query = input("Search Wikipedia: ")
