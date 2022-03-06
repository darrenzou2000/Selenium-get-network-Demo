from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

import time
import json

def processLog(log):
    log = json.loads(log['message'])['message']
    if ("Network.responseReceived" in log["method"] and "params" in log.keys()):
        # print(log)
        if("response" in log["params"]):
            if(log["params"]["response"]["mimeType"]=="application/json"):
                body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': log["params"]["requestId"]})
                if(body['body'][0]!="["):
                    if("count" in json.loads(body['body']).keys()):
                        print(json.loads(body['body']))
                        return 1
    return 0
yoururl = "https://www.barchart.com/stocks/quotes/TROV/technical-chart?plot=BAR&volume=total&data=MO&density=L&pricesOn=1&asPctChange=0&logscale=0&startDate=2015-08-16&endDate=2016-08-15&daterange=specific&sym=TROV&grid=1&height=500&studyheight=100"

caps = DesiredCapabilities.CHROME
caps['goog:loggingPrefs'] = {'performance': 'ALL'}
driver = webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=caps)
driver.get(yoururl)
time.sleep(2) # wait for all the data to arrive. 
perf = driver.get_log('performance')
# for i in perf:
#     result = processLog(i)
#     if(result): break
driver.close()


    # if ("Network.responseReceived" in log["method"] and "params" in log.keys()):
    #     body = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': log["params"]["requestId"]})
    #     print("body")

# data = requests.get("https://www.barchart.com/proxies/core-api/v1/chart?plot=CANDLE&volume=0&data=MO&density=L&pricesOn=0&asPctChange=0&logscale=0&startDate=2013-08-15&endDate=2016-08-15&daterange=specific&sym=TROV&grid=1&height=250&studyheight=100&width=854", headers= headers )
# count =0
# for i in range(1,1000):
#     data = requests.get("https://www.barchart.com/proxies/core-api/v1/chart?plot=CANDLE&volume=0&data=MO&density=L&pricesOn=0&asPctChange=0&logscale=0&startDate=2013-08-15&endDate=2016-08-15&daterange=specific&sym=TROV&grid=1&height=250&studyheight=100&width=854", headers= headers )
#     if data.status_code ==200:
#         count+=1
#     else:
#         break

# print(data.status_code)
# stock_data = data.json()["data"]["map"]

# print("This is data for TROV")
# for monthly in stock_data:
#     print(f"{monthly['data']['date']} open:{monthly['data']['open']}")