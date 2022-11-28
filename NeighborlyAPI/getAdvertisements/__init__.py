import azure.functions as func
import logging
import json
import os
import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = os.environ["mongodbconnection"]  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['appdb']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

