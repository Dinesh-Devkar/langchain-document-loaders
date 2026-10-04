from langchain_community.document_loaders import WebBaseLoader

url='https://www.amazon.in/dp/B0HLKSVW2T/ref=lp_1805560031_1_3?pf_rd_p=9e034799-55e2-4ab2-b0d0-eb42f95b2d05&pf_rd_r=SBY5K89ASW9APG8BC4XM&sbo=7oa42w0ILTiF6GME4JGy%2BQ%3D%3D&th=1'

web_loader=WebBaseLoader(url)

docs=web_loader.load()

print(len(docs))
print("="*50)

print(docs[0].page_content)