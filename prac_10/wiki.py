import wikipedia

query = input("Search Wikipedia: ")
while query != "":
    page_result = wikipedia.page(query)
    print(page_result.title)
    print(page_result.url)
    print(page_result.summary)
    query = input("Search Wikipedia: ")
