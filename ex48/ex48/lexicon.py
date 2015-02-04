directions = ('north', 'south', 'east')
verbs = ('go', 'kill', 'eat')
stop_words = ('the', 'in', 'of')
nouns = ('bear', 'princess')

def get_tuple(word):
    test_word = word.lower()

    if test_word in directions:
        return ('direction', word)
    elif test_word in verbs:
        return ('verb', word)
    elif test_word in stop_words:
        return ('stop', word)
    elif test_word in nouns:
        return ('noun', word)
    elif test_word.isdigit():
        return ('number', int(word))
    else:
        return ('error', word)

def scan(sentence):
    words = sentence.split()
    return [get_tuple(word) for word in words]