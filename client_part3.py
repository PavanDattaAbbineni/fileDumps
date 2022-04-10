import requests
import random as rd
import json
import time
import argparse

def parse():
    """
    This function will parse the input arguments to the program
    :return: arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8080)
    parser.add_argument('--n_requests', type=int, default=10)
    parser.add_argument('--host', type=str, default="127.0.0.1")
    parser.add_argument('--prob_to_buy', type=float, default=0.5)
    args = parser.parse_args()
    return args

def query(host,port,itemName,probToBuy):
    apiUrl = "http://127.0.0.1:8080"
    params = {"products": itemName }
    response = requests.get(apiUrl,params=params)
    a = str(response.headers)
    a=a.replace("'",'')
    startIdx = 0
    for i in range(1,len(a)):
        if(a[i]=='{'):
            startIdx = i
            break
    b = a[i:len(a)-1]
    c = json.loads(b)
    # print(c)
    if(c['data']['quantity']>0):
        params= {"name" : itemName ,"quantity" : 1}
        response = requests.post(apiUrl,params=params)
            # print(response)

if __name__ == "__main__":
    args = parse()
    host = args.host
    port = args.port
    probToBuy = args.prob_to_buy
    itemNames = ["Tux","Whale","Penguin"]
    start = time.time()

    for i in range(args.n_requests):
        itemName = rd.choice(itemNames)
        query(host,port,itemName,probToBuy)
    end=time.time()
    average_time = 10 * (end - start) / args.n_requests
    print("Total runs : %d, Average time taken : %f ms" % (args.n_requests, average_time))
    with open("results.txt", 'a') as f:
        f.write("%f " % average_time)
