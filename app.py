import streamlit as st
import requests

#step1
def getAllBookstore():
	url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
	headers = {"accept": "application/json"}
	response = requests.get(url, headers=headers)
	res=response.json # 將 response 轉換成 json 格式
	return res # 回傳值


def getCountyOption(items):
    optionList = []
    for item in items:
        name = item['cityName'][0:3]
        if name not in optionList:
            optionList.append(name)
    return optionList

def getSpecificBookstore(items, county):
    specificBookstoreList = []
    for item in items: 
        name = item['cityName']
        if country not in name:continue # 如果 name 不是我們選取的 county 則跳過 # hint: 用 if-else 判斷並用 continue 跳過
        specificBookstoreList.append(item)
    return specificBookstoreList




def getBookstoreInfo(items):
    expanderList = []
    for item in items:
        expander = st.expander(item['name'])
        expander.image(item['representImage'])
        expander.metric('hitRate', item['hitRate'])
        expander.subheader('Introduction')
        expander.write(item['introduction']) # 用 expander.write 呈現書店的 Introduction
        expander.subheader('Address')
        expander.write('address') # 用 expander.write 呈現書店的 Address
        expander.subheader('Open Time')
        expander.write('open Time') # 用 expander.write 呈現書店的 Open Time
        expander.subheader('Email')
        expander.write(item['email'])# 用 expander.write 呈現書店的 Email
        expanderList.append(expander)# 將該 expander 放到 expanderList 中
    return expanderList

def app():
	bookstoreList = getAllBookstore()

	countyOption = getCountyOption(bookstoreList)
	
	st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstoreList))
	county = st.selectbox('請選擇縣市', countyOption) 
	districtOption = getDistrictOption(bookstoreList, county)
	district = st.multiselect('請選擇區域', districtOption) 
	
	specificBookstore = getSpecificBookstore(bookstoreList, county, district)
	num = len(specificBookstore)
	st.write(f'總共有{num}項結果', num)
	
	# 呼叫 getBookstoreInfo 並將回傳值賦值給變數 bookstoreInfo

def app():
	bookstoreList = getAllBookstore()
	CountyOption = getCountyOption(bookstoreList)# 呼叫 getCountyOption 並將回傳值賦值給變數 countyOption
	st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstoreList))
	county = st.selectbox('請選擇縣市', CountyOption) # 將['A', 'B', 'C']替換成縣市選項 
    
	specificBookstore = getSpecificBookstore(bookstoreList, county, district)
	num = len(specificBookstore)
	st.write(f'總共有{num}項結果', num)
    bookstoreInfo = getBookstoreInfo(specificBookstore)# 呼叫 getBookstoreInfo 並將回傳值賦值給變數 bookstoreInfo


if __name__ == '__main__':
    app()