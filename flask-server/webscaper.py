from pymongo.mongo_client import MongoClient 
from pymongo.server_api import ServerApi
from apify_client import ApifyClient

def fetch_and_store_instagram_posts(mongo_uri, apify_token, db_name, collection_name, usernames, post_limit):
    # Initialize MongoDB client
    mongo_client = MongoClient(mongo_uri, server_api=ServerApi('1'))
    
    # Select the database and collection
    db = mongo_client[db_name]
    collection = db[collection_name]
    
    # Initialize Apify client
    apify_client = ApifyClient(apify_token)
    
    # Prepare the Actor input
    run_input = {
        "username": usernames,
        "resultsLimit": post_limit,
    }
    
    try:
        # Run the Actor and wait for it to finish
        run = apify_client.actor("apify/instagram-post-scraper").call(run_input=run_input)
        
        # Fetch and store Actor results in the database
        for item in apify_client.dataset(run["defaultDatasetId"]).iterate_items():
            collection.insert_one(item)
            print("Inserted document:", item)
            
        print("All documents inserted successfully.")
    except Exception as e:
        print("An error occurred:", e)

# Example usage
mongo_uri = "mongodb+srv://jimmyphan101004:b5ZRMEY0G3GdYHL3@cluster0.zduycsi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
apify_token = "apify_api_4SDu7dhMg8TGsyriGAf4zaXPrbqZdh21MvcY"
db_name = "your_database_name"  # Replace with your database name
collection_name = "your_collection_name"  # Replace with your collection name
usernames = ["uwengsoc"]
post_limit = 5

fetch_and_store_instagram_posts(mongo_uri, apify_token, db_name, collection_name, usernames, post_limit)
