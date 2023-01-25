import os 
import sys
sys.path.insert(0, "..")

from preprocess.preprocess_data import PreprocessData
import pandas as pd
import json
from datetime import date
import re
from matching.matching_system import MatchingSystem
from crawler.viettel_store import ViettelStore
from matching.data_matching import DataMatching


if __name__ == '__main__':
    test = ViettelStore("viettelstore")

    matchingSystem = MatchingSystem()
    preprocess = PreprocessData()
    datamatching = DataMatching()

    try:

        df = test.crawl()
        df = test.getMessageFromKafka()
        df = pd.DataFrame.from_records(df)

        data = matchingSystem.pipelineMatching(df)
        newDf = preprocess.extractRamFromName(data)
        newDf = preprocess.extractRomFromName(newDf)
        newDf = preprocess.preprocessData(newDf, status=0)
        newDf = preprocess.preprocessColor(newDf)
        newDf.replace(r'^\s*$', 0, regex=True, inplace=True)

        newDf['store'] = 'viettelstore'
        # filename = date.today().strftime('viettelstore'+"%Y%m%d.json")
        newDf.drop_duplicates(inplace=True)
        # newDf.to_csv('../data/production/' + filename)
        datamatching.insertNewData(newDf)

    except Exception as e:
        print(e)
        pass