import os 
import sys
sys.path.insert(0, "..")
from crawler.store24h import Store24h
from preprocess.preprocess_data import PreprocessData
import pandas as pd
import json
from datetime import date

import sys
from matching.matching_system import MatchingSystem
from matching.data_matching import DataMatching


if __name__ == '__main__':
    test = Store24h("24hstore")

    matchingSystem = MatchingSystem()
    preprocess = PreprocessData()
    datamatching = DataMatching()

    # try:
    df = test.crawl()
    df = test.getMessageFromKafka()
    # print(len(df))
    df = pd.DataFrame.from_records(df)
    data = matchingSystem.pipelineMatching(df)
    newDf = preprocess.extractRamFromName(data)
    # newDf = preprocess.extractRomFromName(newDf)
    newDf = preprocess.preprocessData(newDf, status=0)
    newDf = preprocess.preprocessColor(newDf)
    newDf['store'] = '24hstore'
    # filename = date.today().strftime('24hstore'+"%Y%m%d.json")
    # newDf.to_csv('../data/production/' + filename)
    datamatching.insertNewData(newDf)
    # except Exception as e:
    #     print(e)
    #     pass