import os 
import sys
sys.path.insert(0, "..")
from crawler.dienmaycholon import DienMayChoLon
from preprocess.preprocess_data import PreprocessData
import pandas as pd
import json
from datetime import date

import sys
from matching.matching_system import MatchingSystem
from matching.data_matching import DataMatching



if __name__ == '__main__':
    test = DienMayChoLon("dienmaycholon")

    matchingSystem = MatchingSystem()
    preprocess = PreprocessData()
    datamatching = DataMatching()

    try:
        df = test.crawl()
        df = test.getMessageFromKafka()
        df = pd.DataFrame.from_records(df)

        data = matchingSystem.pipelineMatching(df)
        newDf = preprocess.extractRomFromName(data)
        newDf = preprocess.extractRamFromName(newDf)
        newDf = preprocess.preprocessData(newDf, status=0)
        newDf = preprocess.preprocessColor(newDf)

        newDf['store'] = 'dienmaycholon'
        # filename = date.today().strftime('dienmaycholon'+"%Y%m%d.csv")
        # newDf.to_csv('../data/production/' + filename)
        datamatching.insertNewData(newDf)
    except Exception as e:
        print(e)
        pass