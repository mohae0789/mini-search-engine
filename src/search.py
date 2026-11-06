def biword_query(query, biword_index):
    query = query.lower()
    query_tokens = query.split()

    if len(query_tokens) < 2:
        print("Enter at least two words")
        return

    query_biwords = []

    for i in range(len(query_tokens) - 1):
        biword = query_tokens[i] + " " + query_tokens[i + 1]
        query_biwords.append(biword)

    results = None

    for biword in query_biwords:
        if biword not in biword_index:
            print("No result found")
            return

        if results is None:
            results = biword_index[biword].copy()
        else:
            results = results.intersection(biword_index[biword])

    print("Search Results:", results)




def phrase_query(query, positional_index):
    query = query.lower()
    query_tokens = query.split()
    print("Search Query:",query_tokens)
    for token in query_tokens:
        if token not in positional_index:
            print("No result found")
            return
    first_token = query_tokens[0]
    for doc_name, positions in positional_index[first_token].items():
        for position in positions:
            match = True
            for i in range(1,len(query_tokens)):
                next_position = position + i
                token = query_tokens[i]

                if next_position not in positional_index[token].get(doc_name,[]):
                    match = False
                    break
            if match:
                print("Phrase found in:", doc_name)
            



def proximity_query(word1, word2, distance,positional_index):
    word1 = word1.lower()
    word2 = word2.lower()

    if word1 not in positional_index or word2 not in positional_index:
        print("No result found")
        return

    found = False

    for doc_name, positions1 in positional_index[word1].items():

        positions2 = positional_index[word2].get(doc_name, [])

        for pos1 in positions1:
            for pos2 in positions2:

                if abs(pos1 - pos2) <= distance:
                    print("Proximity found in:", doc_name)
                    found = True
                    break

            if found:
                break

    if not found:
        print("No result found")