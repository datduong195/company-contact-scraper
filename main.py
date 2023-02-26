import pandas as pd
import wikipedia as wiki
import re
import time
import random

class scraper():
    def __init__(self):
        self.inputDir = './input.xlsx'
        self.outputDir = './output.xlsx'
        self.keyWordList = {"software","information","technology"}

    def write_file(self):
        self.dataFrameInput.to_excel(self.outputDir)
        pass


    def read_file(self):
        self.dataFrameInput = pd.read_excel(self.inputDir)
        # print(self.dataFrameInput.head())
        pass

    def get_data_from_web(self):
        listSumm = []
        for idx,row in self.dataFrameInput.iterrows():
            item = row['Company']
            print("Searching ",idx," of ",len(self.dataFrameInput.index))
            try:
                tempData = wiki.summary(item,sentences=4).lower()
            except:
                tempData = 'N/A'
            listSumm.append(tempData)
            time.sleep(random.random())
            # print(wiki.summary(item,sentences=3))
            # print("=========")
        # print(self.companyDict)
        self.dataFrameInput["Summary"] = listSumm
        pass

    def search_keywork(self):
        tempList = []
        for idx,row in self.dataFrameInput.iterrows():
            summ = row['Summary']
            keywordStr = ''

            for key in self.keyWordList:
            # print("Searching "+key)
                searchexp = re.compile("(%s)" % key, re.M)
                if searchexp.search(summ):
                    # print(name+" has: " + key)
                    keywordStr  += key +","
            tempList.append(keywordStr)
            # print(tempList)
        self.dataFrameInput["Keyword"] = tempList 
        # print(self.dataFrameInput.head())
        pass


obj = scraper()
obj.read_file()
obj.get_data_from_web()
obj.search_keywork()
obj.write_file()