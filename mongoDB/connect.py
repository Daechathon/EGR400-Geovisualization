import pymongo
client = pymongo.MongoClient(
    "mongodb+srv://admin:ArjenRobben10@cluster0-txyt7.mongodb.net/test?retryWrites=true&w=majority")

db = client.list_database_names()
print(db)


