from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

def generate_translation(language, text):
    translation_prompt = PromptTemplate(
        input_variables=['language', 'text'],
        template="Translate {text} to {language}"
    )

    chain = LLMChain(llm=llm, prompt=translation_prompt, output_key="translatedText")
    response = chain({'language': language, 'text': text})
    return response

if __name__ == "__main__":
    print(generate_translation("French","Hello"))
