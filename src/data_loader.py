import os

def load_documents(documents_folder):
    
 files=os.listdir(documents_folder)

 documents = {}


 for file_name in files:
     file_path = os.path.join(documents_folder,file_name)

     with open(file_path ,"r",encoding="utf-8") as file:
        content=file.read()

     documents[file_name]=content
 return documents