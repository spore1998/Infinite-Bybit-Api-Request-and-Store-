import bybit
import time

client = bybit.bybit(test=True, api_key="", api_secret="")

while True:
    data = client.Market.Market_orderbook(symbol="BTCUSD").result() #reading data each run
    with open('myfile.txt','a') as f: #open for appending
        f.write('{}\n'.format(data)) #write data into a new line
    time.sleep(1) #sleep