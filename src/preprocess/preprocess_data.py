import pandas as pd
import json
import re
from datetime import datetime

class PreprocessData():
    def __init__(self):
        self.timeNow = datetime.now()
        self.model = ["IPHONE 14 MINI", "IPHONE 14 PRO MAX", "IPHONE 14 PRO", "IPHONE 14","IPHONE 13 MINI", "IPHONE 13 PRO MAX", "IPHONE 13 PRO", "IPHONE 13", "IPHONE 12 MINI", "IPHONE 12 PRO MAX",
             "IPHONE 12 PRO", "IPHONE 12",
             "IPHONE 11 PRO MAX", "IPHONE 11 PRO",
             "IPHONE 11", "IPHONE XS MAX", "IPHONE XS", "IPHONE XR", "IPHONE X",
             "IPHONE 8 PLUS", "IPHONE 8", "IPHONE 7 PLUS", "IPHONE 7",
             "IPHONE 6S PLUS", "IPHONE 6 PLUS", "IPHONE 6S", "IPHONE 6",
             "IPHONE 5S", "IPHONE 5C", "IPHONE 5", "IPHONE 4S", "IPHONE 4",
             "IPHONE SE 2020", "IPHONE SE 2022",
             "IPHONE SE 2", "IPHONE SE 3",
             "IPHONE SE",
             "IPHONE 3GS", "IPHONE 3G", "IPHONE 2G",
             "IPAD MINI 3", "IPAD MINI 1", "IPAD GEN 5", "IPAD AIR 2", "IPAD AIR 1", "IPAD 4", "IPAD GEN 6",
             "IPAD PRO 12,9", "IPAD PRO 9.7", "IPAD PRO 10.5", "IPAD PRO 12.9", "IPAD 10.2",
             "IPAD 9 10.2", "IPAD AIR 10.9", "IPAD PRO M1 12.9", "IPAD AIR 10.9 INCH", "IPAD 10.2 INCH",
             "IPAD MINI 6", "IPAD 2010", "IPAD 2 2011", "IPAD PRO M1 11 INCH", "IPAD 10.2 INCH",
             "IPAD 6 MINI", "IPAD 3 MINI", "IPAD AIR 3", "IPAD GEN 9", "IPAD PRO M1 11", "IPAD AIR M1 10.9",
             "IPAD MINI GEN 6TH", "IPAD PRO M1 11", "IPAD AIR4 10.9",
             "IPAD 3 2012", "IPAD 4 2012", "IPAD MINI 2012", "IPAD AIR 2013",
             "IPAD MINI 2", "IPAD AIR 2 2014", "IPAD MINI 3 2014", "IPAD PRO 12,9 INCH",
             "IPAD MINI 4", "IPAD PRO 9.7 INCH", "IPAB 2017", "IPAD PRO 10.5 INCH", "IPAD PRO 12.9 INCH",
             "IPAD PRO 12.9 INCH 2017", "IPAD 2018", "IPAD PRO 11", "IPAD PRO 12.9 INCH 2018",
             "IPAD AIR 2019", "IPAD MINI 5", "IPAD 10.2 INCH 2019", "IPAD AIR 4",
             "IPAD AIR 4 2020", "IPAD PRO 11 INCH 2020", "IPAD PRO 12.9 INCH 2020", "IPAD PRO 12.9 INCH 2021",
             "IPAD 9", "IPAD 9 10.2 INCH", "IPAD 9 10.2 INCH 2021", "IPAB MINI 6 2021",
             "IPAD AIR 5 M1", "IPAD AIR 5 M1 2022", "IPAD PRO M1 12.9 INCH",
             "IPAD MINI 7.9 INCH", "IPAD PRO M1 2021 12.9 INCH", "IPAD PRO M1 2021 11 INCH", "IPAD AIR 10.5 INCH",
             "IPAD PRO M1 2021 12.9 INCH", "IPAD PRO M1 2021 12.9 INCH", "IPAD AIR 10.5 INCH",
             "APPLE GEN 1", "APPLE SERIES 1", "APPLE SERIES 2", "APPLE SERIES 3", "APPLE SERIES 4",
             "APPLE SERIES 5", "APPLE SERIES 6", "APPLE WATCH GEN 1",
             "APPLE WATCH SERIES 1", "APPLE WATCH SERIES 2", "APPLE WATCH SERIES 3", "APPLE WATCH SERIES 4",
             "APPLE WATCH SERIES 5", "APPLE WATCH SERIES 6", "APPLE WATCH S1", "APPLE WATCH S2", "APPLE WATCH S3",
             "APPLE WATCH S4", "APPLE WATCH S5", "APPLE WATCH S6", "APPLE WATCH S7", "APPLE WATCH SE", "APPLE SE",
             "MACBOOK PRO M1 PRO", "MACBOOK AIR M1", "MACBOOK PRO", "MACBOOK AIR", "MAC MINI", "MAC STUDIO", "IPAD 2", "IPAD 3", "IPAD AIR", "IPAD MINI"]

        self.cpu = ["A16", "A15", "A14", "A13", "A12", "A11", "A10", "A9", "A8", "A7", "A6"]
        self.color1 = ['ĐEN', 'TRẮNG', 'TÍM', 'ĐỎ', 'XANH LÁ', 'XANH', 'VÀNG', 'XANH DƯƠNG', 'THAN CHÌ',
            'HỒNG', 'BẠC', 'XANH RÊU', 'JETBLACK', 'XÁM', 'XANH DƯƠNG', 'CAM', 'DA XANH',
            'XANH BIỂN', 'VÀNG HỒNG', 'ĐEN MỜ', 'XANH ĐEN', 'ĐEN BÓNG', 'XANH NAVY', 'VÀNG ĐỒNG']
        self.color2 = ['BLACK', 'WHITE', 'PURPLE', 'RED', 'GREEN', 'BLUE', 'YELLOW', 'BLUE', 'GRAPHITE',
                    'PINK', 'SILVER', 'MOSS GREEN', 'JETBLACK', 'GRAY', 'BLUE', 'ORANGE', 'BLUE SKIN',
                    'SEA BLUE', 'ROSE GOLD', 'BLACK', 'BLUE', 'BLACK', 'BLUE', 'YELLOW']
        self.rom = ["16GB", "32GB", "64GB", "128GB", "256GB", "512GB", "1TB", "16G", "32G", "64G", "128G", "256G", "512G", "1T", "1"]
        self.rom2 = ["16", "32", "64", "128", "256", "512", "1024","16", "32", "64", "128", "256", "512", "1024", "1024"]

        self.mapping_Ram = {"IPHONE 14 MINI":6, "IPHONE 14 PRO MAX":6, "IPHONE 14 PRO":6, "IPHONE 14":6,"IPHONE 13 MINI":6, "IPHONE 13 PRO MAX":6, "IPHONE 13 PRO":6, "IPHONE 13":4, "IPHONE 12 MINI":4, "IPHONE 12 PRO MAX":6,
             "IPHONE 12 PRO":6, "IPHONE 12":4,
             "IPHONE 11 PRO MAX":4, "IPHONE 11 PRO":4,
             "IPHONE 11":4, "IPHONE XS MAX":4, "IPHONE XS":4, "IPHONE XR":3, "IPHONE X":3,
             "IPHONE 8 PLUS":2, "IPHONE 8":2, "IPHONE 7 PLUS":3, "IPHONE 7":2,
             "IPHONE 6S PLUS":2, "IPHONE 6 PLUS":1, "IPHONE 6S":2, "IPHONE 6":1,
             "IPHONE 5S":1, "IPHONE 5C":1, "IPHONE 5":1, "IPHONE 4S":0.512, "IPHONE 4":0.512,
             "IPHONE SE 2020":3, "IPHONE SE 2022":4,
             "IPHONE SE 2":3, "IPHONE SE 3":4,
             "IPHONE SE":2,
             "IPHONE 3GS":0.256, "IPHONE 3G":0.128, "IPHONE 2G":0.128}
    def preprocessData(self, df, status=1):
        for i in range(len(df)):
            for j in range(len(self.model)):
                if df.loc[i, 'name'].upper().find(self.model[j]) != -1:
                    df.loc[i, 'name'] = self.model[j]
                    break

        df['createdDate'] = self.timeNow
        df['status'] = status
        try:
            df_obj = df.select_dtypes(['object'])
            df['price'] = df_obj.price.apply(lambda x: re.sub(r'\D', '', x).replace(' ', '').strip())
            df['rom'] = df_obj.rom.apply(lambda x: re.sub(r'\D', '', x).strip())
            df['color'] = df_obj.color.apply(lambda x: x.replace('\n', '').strip())
        except Exception as e:
            print(e)
        df.fillna('unknown', inplace=True)
        return df

    def extractRomFromName(self, df):
        for i in range(len(df)):
            for j in range(len(self.rom)):
                if df.loc[i, 'name'].upper().find(self.rom[j]) != -1:
                    df.loc[i, 'rom'] = self.rom2[j]
                    break

        return df

    def extractRamFromName(self, df):
        for i in range(len(df)):
            for j in self.mapping_Ram:
                if df.loc[i, 'name'].upper().find(j) != -1:
                    df.loc[i, 'ram'] = self.mapping_Ram[j]
                    break

        return df 
    
    def preprocessInfo(self, df):
        for i in range(len(df)):
            for j in range(len(self.model)):
                if df.loc[i, 'name'].upper().find(self.model[j]) != -1:
                    df.loc[i, 'name'] = self.model[j]
                    break
        return df
    def preprocessColor(self, df):
        for i in range(len(df)):
            for j in range(len(self.color1)):
                if df.loc[i, 'color'].upper() == self.color1[j]:
                    df.loc[i, 'color'] = self.color2[j]
                    break

        return df 