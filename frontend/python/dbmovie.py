from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://test:1234@Cluster0.tmrbb2j.mongodb.net/?retryWrites=true&w=majority')
db = client.testC

print(db.movies.find_one({"title" : "원더"})['star'])

starVar = db.movies.find_one({"title" : "원더"})['star']

titleWithStar = list(db.movies.find({"star" : starVar},{"_id" : False}))
for m in titleWithStar:
    print(m["title"])
    
db.movies.update_one(
    {
        "title" : "원더"
    },
    {
        '$set' : {
            'star' : '0'
        }
    }
)