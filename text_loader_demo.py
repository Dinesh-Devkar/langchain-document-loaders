from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader

load_dotenv()


llm=ChatOpenAI(model='gpt-4o')

prompt=PromptTemplate(template="""summarize the below text : {text}""",
                      input_variables=['text'])

loader=TextLoader('cricket.txt',encoding='utf-8')

docs=loader.load()

# print(len(docs))
# print(docs[0].page_content)

parser=StrOutputParser()

chain = prompt | llm | parser

print(chain.invoke({'text':docs[0].page_content}))

