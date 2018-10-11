def mixAndMatchSentences(sentence):
    """
    Given a sentence (sequence of words), return a list of all "mix and matched" sentences.

    We define these sentences to:
      - have the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the original sentence

    Example:
      - Input: 'the house and the car'
      - Output: ['and the house and the', 'house and the house and', 'the house and the house',
                'the house and the car']
    """

    # make a list of the individual words
    wordlist = str.split(sentence)

    graph = {}

    # Create a graph with words and their adjacent words
    for i in xrange(0, len(wordlist)-1):
        if wordlist[i] in graph:
            if wordlist[i+1] not in graph[wordlist[i]]:
                graph[wordlist[i]].append(wordlist[i+1])
        else:
            graph[wordlist[i]] = []
            graph[wordlist[i]].append(wordlist[i+1])

    sentencelist = []

    # Recursive function to make sentences
    def recurse(curr, k):
        if len(curr.split()) == len(wordlist):
            sentencelist.append(curr)
        else:
            if k in graph:
                for v in graph[k]:
                    recurse(curr + ' ' + v, v)

    for k in graph:
        curr = k
        recurse(curr, k)

    return sentencelist


print mixAndMatchSentences('the house and the car')