import string

def preprocess_documents(documents):
    for file_name, content in documents.items():
         
        content = content.lower()
        
        translator = str.maketrans(string.punctuation , " " * len(string.punctuation))
    
        content = content.translate(translator)
    
        tokens = content.split()
    
    
        documents[file_name] = tokens

    return documents    