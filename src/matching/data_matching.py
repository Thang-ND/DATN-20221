import pandas as pd
import os
import glob
import numpy as np
import strsimpy
import hashlib
from tqdm import tqdm
from pymongo import MongoClient
import datetime
import json
from pymongo import MongoClient
import datetime
import json

class DataMatching():
    levenshtein  = strsimpy.NormalizedLevenshtein()
    client = MongoClient("mongodb+srv://winner:Mongodb2022@apple-hust.ngecy7x.mongodb.net/?retryWrites=true&w=majority")
    database = 'Apple'
    collection1 = 'Product_Search'
    collection2 = 'Products'

    def levenshtein_score(self,x,y):
        if (x=='unknown' or y =='unknown'):
            return 1
        return 1 - self.levenshtein.distance(x,y)

    def difference_score(self,x,y):
        if (x=='unknown' or y =='unknown'):
            return 1
        return 1 if x==y else 0

    def clust_filter(self,arr):
        flag = [False]*len(arr)
        cluster = []
        for i in tqdm(range(0,len(arr)-1)):
            if flag[i]==False:
                list_id = []
                list_id.append(arr[i][10])
                for j in range(i + 1, len(arr)):
                    if flag[j]==False:
                        name = self.difference_score(arr[i][0],arr[j][0])
                        ram = self.difference_score(arr[i][2],arr[j][2])
                        rom = self.difference_score(arr[i][3],arr[j][3])
                        color = self.levenshtein_score(arr[i][6],arr[j][6])
                        status = self.difference_score(arr[i][7], arr[j][7])
                        score = 0.5 * name + 0.05 * ram + 0.15 * rom + 0.2 * color + 0.1 * status
                        if score >= 0.9:
                            flag[j] = True
                            list_id.append(arr[j][10])
                list_id = list(set(list_id))
                arr[i].append(list_id)
                cluster.append(arr[i])
                
        return cluster


    def matching_score(self, new_record, old_record):
        name = self.difference_score(new_record['name'],old_record['name'])
        ram = self.difference_score(new_record['ram'],old_record['ram'])
        rom = self.difference_score(new_record['rom'],old_record['rom'])
        color = self.levenshtein_score(new_record['color'],old_record['color'])
        status = self.difference_score(new_record['status'], old_record['status'])
        score = 0.5 * name + 0.05 * ram + 0.15 * rom + 0.2 * color + 0.1 * status
        return score

    def findPosMaxScore(self, item, searchs):
        searchs = list(searchs)
        max_score = 0
        pos_max = -1
        for id in range(len(searchs)):
            new_score = self.matching_score(item, searchs[id])
            if new_score >= 0.9 and new_score > max_score:
                pos_max = id
                max_score = max(new_score, max_score)
        return pos_max

    def encrypt_string(self, hash_string):
        sha_signature = hashlib.sha256(hash_string.encode()).digest()
        return "".join(["{:x}".format(b) for b in sha_signature])

    def insertNewData(self, df):
        db = self.client[self.database]
        col1 = db[self.collection1] # product_search
        col2 = db[self.collection2] # products

        df['id'] = df['name'].astype(str) + df['url'].astype(str)  + df['rom'].astype(str)+ df['ram'].astype(str) + df['color'] + \
            df['status'].astype(str) + df['store'].astype(str) 
        df['id'] = df['id'].apply(self.encrypt_string) 
        df = df.to_dict('records')

        for item in tqdm(df):
            col2.replace_one({'id': item['id']}, item, upsert=True)
            # checks = col2.find({'id': item['id_orgin']})
            # isExists = len(list(checks)) > 0
            # if(isExists):
            #     col2.replace_one({'id': item['id_orgin']}, item, upsert=True)
            # else:
                # list_searchs = col2.find()
                # pos_max = self.findPosMaxScore(item, list_searchs)
                # if pos_max != -1:
                #     new_record = list_searchs[pos_max]
                #     new_record['list_id'].append(item['id'])
                #     col1.replace_one({'_id': new_record['_id']}, item, upsert=True)
                # else:
                #     #item.rename({'id':'id_orgin'}, inplace=True)
                #     item['list_id'] = []
                #     item['list_id'].append(item['id_orgin'])
                #     # data = item.to_dict('records')
                #     data = item
                #     col1.insert_one(data)                
                # col2.insert_one(item)
        print("Successfully insert into mongodb")