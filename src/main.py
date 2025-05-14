from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from run_llama import start_ollama


start_ollama()
prompt1 = ChatPromptTemplate.from_template("translates {korean_word} to English, only return the translation, no other text.")
prompt2 = ChatPromptTemplate.from_template(
    "explain {english_word} using oxford dictionary to me in Korean. Only return the explanation, no other text. The answer should be in Korean."
)
output_parser = StrOutputParser()
model = OllamaLLM(model="llama3.2")
chain1 = prompt1 | model | output_parser
chain2 = (
    {"english_word": chain1}
    | prompt2
    | model
    | StrOutputParser()
)
response = chain2.invoke({"korean_word": "미래"})
print(response)