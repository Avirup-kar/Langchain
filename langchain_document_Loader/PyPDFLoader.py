from langchain_community.document_loaders import PyMuPDFLoader

loader = PyMuPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(docs[1].page_content)