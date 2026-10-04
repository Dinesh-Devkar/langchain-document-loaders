from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

doc_loader= DirectoryLoader(path="datasets/",
                           glob="*.pdf",
                           loader_cls=PyPDFLoader)

docs=doc_loader.lazy_load()

print(type(docs))
# print("="*40)
# print(docs[1].page_content)

for document in docs:
    print(document.metadata)