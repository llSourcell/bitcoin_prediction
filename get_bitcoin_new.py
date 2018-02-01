import requests, json
from time import sleep
from datetime import datetime
import sys 
import traceback
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("outputfile", nargs='?', default="bitcoin_price.json")
parser.add_argument("errorfile", nargs='?', default="bitcoin_price_error.txt")
args = parser.parse_args()

def getBitcoinPrice():
    URL = 'https://www.bitstamp.net/api/ticker/'
    try:
        r = requests.get(URL)
        bitcoindata = json.loads(r.text)
        bitcoindata['datetime'] = datetime.utcfromtimestamp(int(bitcoindata['timestamp'])).strftime('%Y-%m-%d-%H-%M-%S')        

        with open(args.outputfile, mode='a') as file:
            file.write('{},\n'.format(json.dumps(bitcoindata)))     

    except:        
        exc_type, exc_value, exc_traceback = sys.exc_info()
        with open(args.errorfile, mode='a') as file:           
           traceback.print_exc(file=file)
           file.write(('-'*100)+'\n\n')


while True:	
    getBitcoinPrice()
    sleep(10)