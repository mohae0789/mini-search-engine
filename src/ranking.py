import math

def calculate_tf(term, documents):
    results = {}

    for doc_name, tokens in documents.items():
        tf = tokens.count(term.lower())

        if tf > 0:
            results[doc_name] = tf
    return results



def calculate_query_score(query,documents):
    query_tokens = query.lower().split()

    scores = {}

    for doc_name, tokens in documents.items():
        score = 0

        for term in query_tokens:
            score += tokens.count(term)

        if score > 0:
            scores[doc_name] = score

    return scores



def rank_results(query,documents):
    scores = calculate_query_score(query,documents)
    rank_results = sorted (
        scores.items(),
        key=lambda item: item[1],
        reverse = True
    )
    return rank_results


def calculate_idf(term,documents):
    N = len(documents)

    df = 0

    for tokens in documents.values():

        if term.lower() in tokens:
          df += 1
    if df ==0:
        return 0
    idf = math.log(N / df)
    return idf   

def calculate_tfidf(term , doc_name,documents):
    tf= documents[doc_name].count(term.lower())
    idf = calculate_idf(term,documents)
    return tf * idf

def calculate_tfidf_score(query,documents):
    query_tokens = query.lower().split()
    scores = {}
    for doc_name, tokens in documents.items():
        score = 0

        for term in query_tokens:

         tf = tokens.count(term)
         idf = calculate_idf(term,documents)
         score += tf * idf

        if score > 0:
         scores[doc_name] = score
    return sorted(
        scores.items(),
        key = lambda item: item[1],
        reverse = True
    )
