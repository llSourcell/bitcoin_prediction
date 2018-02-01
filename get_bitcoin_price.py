__author__ = 'Chandra S Narain Kappera'

import requests

def getPrices():
    date_prices = {}
    for page in range(1,1000):
        page_string = str(page)
        page_link = 'https://api.coinbase.com/v1/prices/historical?page=' + page_string
        r = requests.get(page_link)
        r = r.text
        year_string = r[0:4]
        month_string = r[5:7]
        day_string = r[8:10]
        year_int = int(year_string)
        month_int = int(month_string)
        day_int = int(day_string)
        date_tuple = (year_int, month_int, day_int)
        if date_tuple not in date_prices:
            date_string = year_string + "-" + month_string + "-" + day_string
            start_point = r.index(date_string) + 26
            end_point = start_point
            while r[end_point] != '.':
                end_point = end_point + 1
            end_point = end_point + 2
            value_string = r[start_point:end_point]
            value_float = float(value_string)
            date_prices[date_tuple] = value_float
        day_on_page = True
        while day_on_page:
            if month_int == 3 and day_int == 1:
                month_int = 2
                day_int = 28
            elif (month_int == 5 or month_int == 7 or month_int == 10 or month_int == 12) and day_int == 1:
                month_int = month_int - 1
                day_int = 30
            elif (month_int == 2 or month_int == 4 or month_int == 6 or month_int == 8 or month_int == 9 or month_int == 11) and day_int == 1:
                month_int = month_int - 1
                day_int = 31
            elif month_int == 1 and day_int == 1:
                month_int = 12
                day_int = 31
                year_int = year_int - 1
            else:
                day_int = day_int - 1
            month_string = str(month_int)
            if len(month_string) < 2:
                month_string = '0' + month_string
            day_string = str(day_int)
            if len(day_string) < 2:
                day_string = '0' + day_string
            date_string = str(year_int) + '-' + month_string + '-' + day_string
            if r.find(date_string) == -1:
                day_on_page = False
                break
            start_point = r.index(date_string) + 26
            end_point = start_point
            while r[end_point] != '.':
                end_point = end_point + 1
            end_point = end_point + 2
            value_string = r[start_point:end_point]
            value_float = float(value_string)
            date_tuple = (year_int, month_int, day_int)
            date_prices[date_tuple] = value_float
    return date_prices


        #figure out first day in list
        #if we don't have data for that day
            #get data
        #otherwise
            #find next day's data
            #add day to days list
            #if we can't find next day's data
                #next page


target = open('bitcoinprices.txt', 'w')

price_dict = getPrices()
# not very elegant - need to modify this, but commiting the current logic - Chandra
for key in price_dict.keys():
    year = key[0]
    month = key[1]
    date = key[2]
    year = year*10000
    month = month*100
    stamp = year+month+date
    value = price_dict[key]
    target.write(str(stamp)+','+str(value)+'\n')
