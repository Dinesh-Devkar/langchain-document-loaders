from langchain_community.document_loaders import PyPDFLoader,PyMuPDFLoader

loader=PyPDFLoader("The_AI_Marketing_Canvas.pdf")

# loader_1 =PyMuPDFLoader("The_AI_Marketing_Canvas.pdf")

docs=loader.load()

# # print(len(docs))
# # print(docs[1])

# docs=loader_1.load()

print(len(docs))
print("="*40)
print(docs[0])


