import together
from pymongo import MongoClient
from typing import List
import time
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv(dotenv_path='./secrets.env')

#mongoDB connection

uri = os.getenv('MONGO_CONN_URI')

# Create a new client and connect to the server
mongoclient = MongoClient(uri)
# Select the database (create if not exists)
db = mongoclient['Instagram']  # Replace 'your_database_name' with the actual database name
collection = db['Posts'] 


#init together ai
together.api_key = os.getenv('TOGETHER_API_KEY')
#code for embedding
embedding_model_string = 'WhereIsAI/UAE-Large-V1' # model API string from Together.
vector_database_field_name = 'embedded' # define your embedding field name.
NUM_DOC_LIMIT = 200 # the number of documents you will process and generate embeddings.

def generate_embedding(input_texts: List[str], model_api_string: str) -> List[List[float]]:
  together_client = together.Together()
  outputs = together_client.embeddings.create(
      input=input_texts,
      model=model_api_string,
  )
  return [x.embedding for x in outputs.data]

def return_events(prompt):
  query = prompt
  query_emb = generate_embedding([query], embedding_model_string)[0]

  results = collection.aggregate([
    {
      "$vectorSearch": {
        "queryVector": query_emb,
        "path": "embeddings",
        "numCandidates": 100, # this should be 10-20x the limit
        "limit": 3, # the number of documents to return in the results
        "index": "vector_index", # the index name you used in Step 4.
      }
    }
  ])

  response = ""
  for i in results:
      response += (i['caption']+ "\n"+ i['url'] + '\n\n')
  return response
