from pymongo import MongoClient
import datetime
import json

def ingestData(file_path, collection, database):
    client = MongoClient("mongodb+srv://winner:Mongodb2022@apple-hust.ngecy7x.mongodb.net/?retryWrites=true&w=majority")
    db = client[database]
    col = db[collection]
    with open(file_path) as file:
        file_data = json.load(file)

    if isinstance(file_data, list):
        col.insert_many(file_data)
    else:
        col.insert_one(file_data)

if __name__ == '__main__':
    print("Ingest iphone info dataset into MongoDb Atlas Cloud")
    print("......")
    ingestData("./info-iphone.json", "Product_Detail", "Apple")
    print("Done")

    print("=======================================")
    print("Ingest ipad info dataset into MongoDb Atlas Cloud")
    print("......")
    ingestData("./info-ipad.json", "Product_Detail", "Apple")
    print("Done")

    print("=======================================")
    print("Ingest watch info dataset into MongoDb Atlas Cloud")
    print("......")
    ingestData("./info-watch.json", "Product_Detail", "Apple")
    print("Done")