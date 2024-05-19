import together
import pymongo
from typing import List

together.api_key = "00801d9e52f3257f9f6957d51f9231b6b27a1b873e0cc7598fafd21210712f6c"

#Query is fed into mistral to generate a hypothetical wikipedia article name. It is then inputted into 
query = "What events have free food?"

uri= open("RAG_Components/mongoURI.txt","r").read().splitlines()[0]

client = pymongo.MongoClient(uri)
db = client["UW_UPNEXT"]
collection_name = db["POST"]
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

query_emb = generate_embedding([query], embedding_model_string)[0]

data = {
    'inputUrl': 'https://www.instagram.com/uwengsoc',
    'id': '3369946306410358751',
    'type': 'Image',
    'shortCode': 'C7EdE-Zuqff',
    'caption': 'Genius Bowl is a once per term multi category trivia night where teams of 1 or 2 compete to have their name on the Genius Bowl trophy + giftcard! \n\nDrinks and food are provided, come to POETS from 6pm-8pm for a night full of trivia and fun.',
    'hashtags': [],
    'mentions': [],
    'url': 'https://www.instagram.com/p/C7EdE-Zuqff/',
    'commentsCount': 0,
    'firstComment': '',
    'latestComments': [],
    'dimensionsHeight': 1320,
    'dimensionsWidth': 1080,
    'displayUrl': 'https://scontent.cdninstagram.com/v/t51.29350-15/443842424_1522650781927681_8726807010980568327_n.jpg?stp=dst-jpg_e15_fr_p1080x1080&_nc_ht=scontent.cdninstagram.com&_nc_cat=101&_nc_ohc=YME__1ouuaAQ7kNvgEiV1p6&edm=APs17CUBAAAA&ccb=7-5&oh=00_AYApAUTCQ6i68lLvxSAdK8RzHMYP0n7NY83BC1slB03gsQ&oe=664FDC46&_nc_sid=10d13b',
    'images': [],
    'alt': "Photo by Waterloo Engineering Society on May 17, 2024. May be a doodle of \u200etext that says '\u200eENCIWEERING ริ OF WAT GENIUS BOWL ? 1۹ ؟ ዘክም હ POETS May 24th 6pm 8pm Battle against other teams in topics from pop culture to history for a chance to win a giftcard!\u200e'\u200e.",
    'likesCount': 34,
    'timestamp': '2024-05-17T12:28:46.000Z',
    'childPosts': [],
    'ownerFullName': 'Waterloo Engineering Society',
    'ownerUsername': 'uwengsoc',
    'ownerId': '390270574',
    'isSponsored': False
}

data["embeddings"] = str(generate_embedding([data['caption']+data['alt']], embedding_model_string)[0])

print(data)