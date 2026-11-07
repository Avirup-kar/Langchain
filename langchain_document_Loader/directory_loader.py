from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

doc = loader.load() ## To load all the documents at once in memory
docs = loader.lazy_load() ## To load the documents one by one in memory

for document in docs:
    print(document.metadata)