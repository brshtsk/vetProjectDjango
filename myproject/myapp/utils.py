# utils.py

def my_utility_function(name):
    return str(name).capitalize() + ", hello from utility function!"

# from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
# from langchain import OpenAI
# import sys
# import os
#
# def construct_index(directory_path):
#     # set maximum input size
#     max_input_size = 4096
#     # set number of output tokens
#     num_outputs = 2000
#     # set maximum chunk overlap
#     max_chunk_overlap = 20
#     # set chunk size limit
#     chunk_size_limit = 600
#
#     # define prompt helper
#     prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
#
#     # define LLM
#     llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="text-davinci-003", max_tokens=num_outputs))
#
#     documents = SimpleDirectoryReader(directory_path).load_data()
#
#     service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)
#     index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)
#
#     index.save_to_disk('index.json')
#
#     return index
#
# def get_response(query):
#     os.environ["OPENAI_API_KEY"] = "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"
#     construct_index("GPTdata/convData")
#     index = GPTSimpleVectorIndex.load_from_disk('index.json')
#     return index.query(query)

from openai import OpenAI
import os

def get_response(question):
  instruction = "Ты ассистент, который помогает, если у питомцев проблемы с давлением. Запомни рекомендации, которые ты должен давать:"
  with open("simpleConv.txt", encoding="utf-8") as file:
    for line in file:
      if line[-1] == "\n":
        line = line[:-1]
      instruction += " " + line + ";"

  os.environ["OPENAI_API_KEY"] = "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"
  client = OpenAI()

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
      {"role": "system", "content": instruction},
      {"role": "user", "content": question}
    ]
  )

  return completion.choices[0].message.content
