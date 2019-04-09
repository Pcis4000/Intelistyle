import json
from botocore.vendored import requests
from urllib.request import urlopen
from ast import literal_eval

url = 'https://s3-eu-west-1.amazonaws.com/stylr-ai-engine-srv-data/srv/data/archive/zalando-women-07-10-2017/garment_items.jl'

def getSearchResults(query):
    search = query['searchQuery'].split("+")

    products = openProductFile()
    matches = []
    for productDetails in products: # iterate through product list
        found = True
        productDetails = json.loads(productDetails)
        for entry in search:
            if entry.lower() not in productDetails['product_title']:
                found = False
                break
        if found:
            matches.append(productDetails)
    print(len(matches))
    return matches

def openProductFile():
    data = urlopen(url)
    return data


def lambda_handler(event, context):

    processed_event = {event['body'].split("=")[0]:event['body'].split("=")[1]}
    matches = getSearchResults(processed_event)

    return {
        'statusCode': 200,
        'body': json.dumps(matches)
    }
