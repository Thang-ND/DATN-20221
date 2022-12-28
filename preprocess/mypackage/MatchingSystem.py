import pandas as pd 
from strsimpy.levenshtein import Levenshtein

class MatchingSystem():
    def __init__(self):
        self.mapping_columns = {
            "name": ["model", "name", "Tên"],
            "url": ["url", "short-link", "link", "short_url"],
            "ram": ["ram", "RAM", "Ram", "Memory"],
            "rom": ["Bộ nhớ trong", "rom"],
            "price": ["giá", "price"],
            "createdDate": ["createdDate"],
            "color": ["Màu sắc", "color", "màu"],
            "status": ["tình trạng", "status"],
            "url_img": ["img_url", "url_img", "link_url"]
        }

        self.levenshtein = Levenshtein()
    
    def getTargetSchema(self):
        target_schema = []
        for col in self.mapping_columns:
            target_schema.append(col)
        return target_schema

    def similarity_score(self, x, y):
        x = x.lower().strip()
        y = y.lower().strip()
        return (len(x) + len(y) - self.levenshtein.distance(x, y))/ (len(x) + len(y))
    
    def check_similarity(self, x, y, threshold=0.8):
        score = self.similarity_score(x, y)
        if (score > threshold):
            return True
        return False

    def schemaMatching(self, cols, threshold=0.85):
        res = dict()
        for col in cols:
            for key in self.mapping_columns:
                listMatching = self.mapping_columns[key]
                for match in listMatching:
                    score = self.similarity_score(col, match)
                    if (score > threshold):
                        print("{0:20}\t{0:20}\t".format(col, match) + str(score))
                        res[col] = key
        
        return res

    def matchedCol(self, result):
        matched_col = []
        source_col = []
        for key in result:
            matched_col.append(result[key])
            source_col.append(key)

        return (matched_col, source_col)


    def pipelineMatching(self, df):
        targetSchema = self.getTargetSchema()
        data = pd.DataFrame(columns=targetSchema)

        columns = list(df.columns)
        res = self.schemaMatching(columns, threshold=0.85)
        # (matchedCol, sourceCol) = self.matchedCol(res)
        matchedCol = list(res.values())
        sourceCol = list(res.keys())
        df_tmp = df[sourceCol].rename(columns=res)
        data[matchedCol] = df_tmp[matchedCol]

        return data