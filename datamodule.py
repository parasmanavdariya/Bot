import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["botdatabase"]

mycol = mydb["Note"]




def add(mydict):
    mycol.insert_one(mydict)
   

def show (mycol=mycol):
    for x in mycol.find():
        print(x)