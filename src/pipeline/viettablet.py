import os 
import sys
sys.path.insert(0, "..")

from preprocess.preprocess_data import PreprocessData
import pandas as pd
import json
from datetime import date
import re
from matching.matching_system import MatchingSystem
from crawler.viettablet import Viettablet
from matching.data_matching import DataMatching


def checkIsAlNum(string):
    res = ''.join(e for e in string if e.isalnum() or e == ' ')
    res = ''.join(e for e in res if not e.isdigit() or e == ' ')
    return res

if __name__ == '__main__':
    test = Viettablet("viettablet")

    matchingSystem = MatchingSystem()
    preprocess = PreprocessData()
    datamatching = DataMatching()

    try:

        df = test.crawl()
        df = test.getMessageFromKafka()
        df = pd.DataFrame.from_records(df)

        df['extract'] = df['color'].apply(lambda x: x.split('</i>')[1].split('<span')[0].replace('\n','').strip())  
        df['color'] = df['extract'].apply(checkIsAlNum)
        df = matchingSystem.pipelineMatching(df)
        newDf = preprocess.extractRomFromName(df)
        newDf = preprocess.extractRamFromName(newDf)
        newDf = preprocess.preprocessData(newDf, status=1)
        newDf = preprocess.preprocessColor(newDf)

        newDf['store'] = 'viettablet'
        # filename = date.today().strftime('viettablet'+"%Y%m%d.json")
        newDf.drop_duplicates(inplace=True)
        # newDf.to_csv('../data/production/' + filename)
        datamatching.insertNewData(newDf)

    except Exception as e:
        print(e)
        pass