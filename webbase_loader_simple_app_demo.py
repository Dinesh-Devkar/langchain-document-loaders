from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()


llm=ChatOpenAI(model='gpt-4o')

url="https://www.amazon.in/dp/B0HLKSVW2T/ref=lp_1805560031_1_3?pf_rd_p=9e034799-55e2-4ab2-b0d0-eb42f95b2d05&pf_rd_r=SBY5K89ASW9APG8BC4XM&sbo=7oa42w0ILTiF6GME4JGy%2BQ%3D%3D&th=1"
web_loader=WebBaseLoader(url)

docs=web_loader.load()

prompt= PromptTemplate(template=""" answer the following question {question} based on following text : \n {text}""",
                       input_variables=['question','text'])

parser=StrOutputParser()

chain =RunnableSequence(prompt,llm,parser)

result=chain.invoke({'question':'tell me the specifications about the product','text':docs[0].page_content})

print(result)