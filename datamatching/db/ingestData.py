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
    print("Ingest products dataset into MongoDb Atlas Cloud")
    print("......")
    ingestData("./products.json", "Test", "Apple")
    print("Done")

    # print("=======================================")
    # print("Ingest search dataset into MongoDb Atlas Cloud")
    # print("......")
    # ingestData("./search.json", "Product_Search", "Apple")
    # print("Done")