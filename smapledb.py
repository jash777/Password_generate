import pymongo

# Create a MongoDB client and connect to a running MongoDB instance
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

# Create a new database and collection
my_db = client["mydb"]
my_collection = my_db["sample"]

# Insert a document into the collection
my_document = {"name": "R15", "age": 3.0}
my_collection.insert_one(my_document)



# Define a function to retrieve the user's answers from the database
def get_user_answers(user_id):
    user_answers = collection.find_one({'user_id': user_id})
    if user_answers:
        return user_answers['answers']
    else:
        return None
# Define a function to store the user's answers in the database
def store_user_answers(user_id, answers):
    document = {'user_id': user_id, 'answers': answers}
    collection.insert_one(document)
