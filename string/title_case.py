def title_case(title, minor_words=''):
    arr = []
    minor_words = minor_words.lower().split()
    for word in title.capitalize().split():
        if word in minor_words:
            arr.append(word)
        else:
            arr.append(word.capitalize())
    return " ".join(arr)


print(title_case('THE WIND IN THE WILLOWS', 'The In')) # should return: 'The Wind in the Willows'
print(title_case('a clash of KINGS', 'a an the of')) # should return: 'A Clash of Kings'
print(title_case('the quick brown fox')) # should return: 'The Quick Brown Fox'
