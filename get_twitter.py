__author__ = 'Chandra S Narain Kappera'


from pprint import pprint
import requests, json
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime


#Format
#{"importance": 0-10, "sentiment": positive/negative/neutral, "score":0-1}
#

def get_sentiment(year, month, day):
    month_string = str(month)
    if len(month_string) < 2:
        month_string = "0" + month_string
    day_string = str(day)
    if len(day_string) < 2:
        day_string = "0" + day_string
    date = str(year) + month_string + day_string

    r1 = requests.get("http://archive.org/wayback/available?url=reddit.com/r/bitcoin&timestamp=" + date)

    if(r1.status_code == 200):
        data1 = json.loads(r1.text)
        archive_url = data1['archived_snapshots']['closest']['url']
    else:
        archive_url = None
        print("Error return code = "+str(r1.status_code))

    r2 = requests.get("https://api.idolondemand.com/1/api/sync/analyzesentiment/v1?apikey=fe6dea49-084f-4cd8-be86-0976baf9a714&url=" + archive_url)

    if(r2.status_code == 200):
        data2 = json.loads(r2.text)
        return data2['aggregate']['score']
    else:
        print("Error return code = "+str(r2.status_code))


def make_dict():
    scores = {}
    date = datetime.date(2017, 11, 14)
    target = open('sentiment6.txt', 'w')
    for i in range(643):
        #print(date.year)
        #print(date.month)
        #print(date.day)
        stamp = date.year*10000+date.month*100+date.day
        value = get_sentiment(date.year, date.month, date.day)
        scores[(date.year, date.month, date.day)] = value
        date -= datetime.timedelta(days=1)
        target.write(str(stamp)+','+str(value))
        target.write('\n')
    target.close()
make_dict()
