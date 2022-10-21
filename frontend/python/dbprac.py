from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://test:1234@Cluster0.tmrbb2j.mongodb.net/?retryWrites=true&w=majority')
db = client.testC

# =-
# doc = {
#     'name' : 'bob',
#     'age' : 27
# }

# db.users.insert_one({
#     'name' : 'john',
#     'age' : 27
# })

# db.users.insert_one({
#     'name' : 'check',
#     'age' : 27
# })

# db.users.insert_one({
#     'name' : 'helloworld',
#     'age' : 27
# })

# all_users = list(db.users.find({},{'_id' : False}))

# for user in all_users:
#     print(user)

# user = db.users.find_one({'name':'bobby'})

# print(user)

db.users.update_one({'name':'john'}, {'$set':{'age':19}})