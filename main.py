import pandas as pd
import wikipedia as wiki
import re

class scraper():
    def __init__(self,inputDir):
        # self.dataFrameOutput = pd.DataFrame()
        self.outputDir = './output.xlsx'
        self.inputDir = inputDir
        self.keyWordList = {"software","information","technology"}
        # self.companyDict = dict()

    def write_file(self):
        
        self.dataFrameInput.to_excel(self.outputDir)
        pass


    def read_file(self):
        self.dataFrameInput = pd.read_excel(self.inputDir)
        # print(self.dataFrameInput.head())
        pass

    def input_handler(self):
        pass

    def get_data_from_web(self):
        listSumm = []
        for idx,row in self.dataFrameInput.iterrows():
            item = row['Company']
            try:
                tempData = wiki.summary(item,sentences=3).lower()
            except:
                tempData = 'N/A'
            listSumm.append(tempData)
            # print(wiki.summary(item,sentences=3))
            # print("=========")
        # print(self.companyDict)
        self.dataFrameInput["Summary"] = listSumm
        pass

    def search_keywork(self):
        # for name in self.dataFrameInput["Company"]:
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


obj = scraper('input.xlsx')
obj.read_file()
obj.get_data_from_web()
obj.search_keywork()
obj.write_file()