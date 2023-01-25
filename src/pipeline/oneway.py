import os 
import sys
sys.path.insert(0, "..")
from crawler.oneway import OneWay
from preprocess.preprocess_data import PreprocessData
import pandas as pd
import json
from datetime import date
import re
import sys
from matching.matching_system import MatchingSystem
from matching.data_matching import DataMatching


if __name__ == '__main__':
    test = OneWay("onewaymobile")

    matchingSystem = MatchingSystem()
    preprocess = PreprocessData()
    datamatching = DataMatching()

    try:
        #Crawl Iphone
        df = test.crawlIphone()
        df = test.getMessageFromKafka(topic='onewaymobile-Iphone')
        df = pd.DataFrame.from_records(df)
        data = matchingSystem.pipelineMatching(df)
        newDf = preprocess.extractRomFromName(data)
        newDf = preprocess.extractRamFromName(newDf)
        newDf = preprocess.preprocessData(newDf, status=0)
        newDf = preprocess.preprocessColor(newDf)

        newDf['store'] = 'onewaymobie'
        # filename = date.today().strftime('onewaymobile'+"%Y%m%d.json")
        newDf.drop_duplicates(inplace=True)
        # newDf.to_csv('../data/production/' + filename)
        datamatching.insertNewData(newDf)
        #Crawl Mac
        # df = test.crawlOther()
        # df = test.getMessageFromKafka(topic='onewaymobile-Mac')
        # df = pd.DataFrame.from_records(df)
        # df['ram'] = df['info'].apply(lambda x: re.sub(r'\D', '', x.split('\n')[1]))
        # data = matchingSystem.pipelineMatching(df)  
        # newDf = preprocess.extractRomFromName(data)
        # newDf = preprocess.preprocessData(newDf, status=0)
        # newDf = preprocess.preprocessColor(newDf) 

        # newDf['store'] = 'onewaymobie'
        # filename = date.today().strftime('onewaymobile-mac'+"%Y%m%d.json")
        # newDf.drop_duplicates(inplace=True)
        # newDf.to_csv('../data/production/' + filename)
    except Exception as e:
        print(e)
        pass