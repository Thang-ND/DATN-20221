from crawler.store24h import Store24h
from preprocess.preprocess_data import PreprocessData
import pandas as pd
import json
from datetime import datetime
import sys
from matching.matching_system import MatchingSystem


if __name__ == '__main__':
    test = Store24h("24hstore")

    createdDate = datetime.now()
    matchingSystem = MatchingSystem()
    preprocess = PreprocessData()


    try:
        test.crawl()
        test.saveDataToLocalFile()
        df_origin = pd.read_json('./data/24hstore/24hstore20230102.json')
        data = matchingSystem.pipelineMatching(df_origin)
        newDf = preprocess.extractRamFromName(data)
        # newDf = preprocess.extractRomFromName(newDf)
        newDf = preprocess.preprocessData(newDf, status=0)
        newDf = preprocess.preprocessColor(newDf)
        newDf['store'] = '24hstore'

    except Exception as e:
        print(e)
        pass

