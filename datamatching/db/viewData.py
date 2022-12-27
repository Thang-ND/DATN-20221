from pymongo import MongoClient
import datetime
import json

def viewData(collection, database):
    client = MongoClient("mongodb+srv://winner:Mongodb2022@apple-hust.ngecy7x.mongodb.net/?retryWrites=true&w=majority")
    db = client[database]
    col = db[collection]


    x = col.find_one({'name': 'IPHONE 14 PRO MAX'})
    print(x)

if __name__ == '__main__':
    print("View a sample of products dataset on MongoDb Atlas Cloud")
    viewData('Products', 'Apple')