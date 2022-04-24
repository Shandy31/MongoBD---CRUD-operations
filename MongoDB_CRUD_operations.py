import pymongo
# connection to MongoDB
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/') # mongodb - protocol, 127.0.0.1 - IP of localhost, 27017 - Port number 

# to list all database names
client.list_database_names() 

# creating database
database_name = "Food"
mydb = client[database_name]

# creating collection
collection_name = "Starters"
collection = mydb[collection_name]

# inserting documents

document = {
    'Name':'Samosa',
    'Type':'Veg',
    'Price':20,
    'Rating':'3'
}
collection.insert_one(document) # Inserts a single documents

documents = [{'Name':'Pakoda','Type':'Veg','Price':15,'Rating':'2'},
            {'Name':'French fries','Type':'Veg','Price':45,'Rating':'4'},
            {'Name':'Chicken nuggets','Type':'Non-Veg','Price':75,'Rating':'5'},
            {'Name':'Nuggets','Type':'Veg','Price':35,'Rating':'2'},
            {'Name':'Tomato soup','Type':'Veg','Price':20,'Rating':'3'},
            {'Name':'Chicken soup','Type':'Non-Veg','Price':90,'Rating':'5'},
            {'Name':'Mutton soup','Type':'Non-Veg','Price':110,'Rating':'5'},
            {'Name':'Gobi 65','Type':'Veg','Price':50,'Rating':'4'},
            {'Name':'Chicken 65','Type':'Non-Veg','Price':75,'Rating':'5'}]

collection.insert_many(documents) # Inserts multiple documents

# Retrieving of the data

query = {'Name':'Nuggets'}
print(collection.find_one(query)) # for single document

query = {'Type': 'Veg'}
result = collection.find(query) # for multiple documents
for i in result:
    print(i)

result = collection.find({}).limit(3) # limiting the results
for i in result:
    print(i)

query = {'Rating':{'$eq':'4'}} # Filtering the document - $eq -> Matches values that are equal to a specified value
print(collection.find_one(query))

query = {'Price':{'$gt':50}} # Filtering the document - $gt -> Matches values that are greater than a specified value
print(collection.find(query))

# Updating the data

query = {'Name':{'$eq':'Chicken nuggets'}}
data = collection.find_one(query)
new_data = {'$set':{'Name':'Fish nuggets'}}
collection.update_one(data,new_data) # for single document

data = {'Rating':'2'}
new_data = {'$set':{'Rating':'3'}}
collection.update_many(data,new_data) # for multiple documents

# Deleting the data

query = {'Name':'Pakoda'}
collection.delete_one(query) #  for single document

query = {'Rating':'4'}
collection.delete_many(query) #  for multipe documents

# for dropping a colletion -> collection.drop()