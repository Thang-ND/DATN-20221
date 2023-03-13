import os 
import sys
sys.path.insert(0, "..")
from crawler.cellphone.cellphone.spiders.iphone_spider import IphoneSpider
from crawler.cellphone.cellphone.spiders.ipad_spider import IpadSpider
from preprocess.preprocess_data import PreprocessData
import pandas as pd
import json
from datetime import date

import sys
from matching.matching_system import MatchingSystem
from matching.data_matching import DataMatching

if __name__ == '__main__':

    matchingSystem = MatchingSystem()
    preprocess = PreprocessData()
    datamatching = DataMatching()

    test = IphoneSpider()
    test2 = IpadSpider()
    try:
        test.crawl()
        df = test.getMessageFromKafka()
        df = pd.DataFrame.from_records(df)
        data = matchingSystem.pipelineMatching(df)
        newDf = preprocess.extractRamFromName(data)
        newDf = preprocess.extractRomFromName(newDf)
        newDf = preprocess.preprocessData(newDf, status=1)
        newDf = preprocess.preprocessColor(newDf)
        newDf['store'] = 'tragopdidong'
        # filename = date.today().strftime('tragopdidong-iphone'+"%Y%m%d.csv")
        # newDf.to_csv('../data/production/' + filename)
        datamatching.insertNewData(newDf)
        #print('========================Done============================')
        
    except Exception as e:
        print(e)
    
    # try:
    #     test2.crawl()
    #     df = test.getMessageFromKafka()
    #     df = pd.DataFrame.from_records(df)

    #     data = matchingSystem.pipelineMatching(df)
    #     newDf = preprocess.extractRamFromName(data)
    #     newDf = preprocess.extractRomFromName(newDf)
    #     newDf = preprocess.preprocessData(newDf, status=1)

    #     newDf['store'] = 'tragopdidong'
    #     filename = date.today().strftime('tragopdidong-ipad'+"%Y%m%d.csv")
    #     newDf.to_csv('../data/production/' + filename)        
    # except Exception as e:
    #     print(e)



