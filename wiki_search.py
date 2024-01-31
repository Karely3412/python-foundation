import wikipedia

def wiki_search():
    search_topic = input('Enter a search topic: ')

    result = wikipedia.search(search_topic)
    print(wikipedia.summary(result[0], sentences=20))

    # print(result)
    return(result)



wiki_search()