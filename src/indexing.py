def create_inverted_index(documents):   
  inverted_index = {}
  for doc_name, tokens in documents.items():
      for token in tokens:
        if token not in inverted_index:

            inverted_index[token] = set()

        inverted_index[token].add(doc_name)

  return inverted_index


def create_positional_index(documents):  
 positional_index ={}
 for doc_name, tokens in documents.items():
    for position, token in enumerate(tokens):
        if token not in positional_index:
            positional_index[token]= {}
        if doc_name not in positional_index[token]:
            positional_index[token][doc_name]=[]
        positional_index[token][doc_name].append(position)
 return positional_index

def create_biword_index(documents):
  biword_index = {}
  for doc_name, tokens in documents.items():

    for i in range(len(tokens) - 1):

        biword = tokens[i] + " " + tokens[i + 1]

        if biword not in biword_index:
            biword_index[biword] = set()

        biword_index[biword].add(doc_name)
  return biword_index