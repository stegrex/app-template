import json
import pprint
from fastapi import FastAPI
from service.service import Service

app = FastAPI()

@app.post("/item/upsert")
async def upsert_item(id=None, title=""):
    service = Service()
    itemDict = {
        "title": title
    }
    if id:
        itemDict["id"] = id
    item, response = service.upsert_item(itemDict)
    itemOutput = {}
    if item:
        itemOutput = item.to_dictionary()
    return itemOutput

@app.get("/item/filter")
async def filter_items(ids=[], titles=[]):
    filters = {}
    if ids:
        filters["id"] = json.loads(ids)
    if titles:
        filters["title"] = json.loads(titles)
    service = Service()
    items, response = service.filter_items(filters)
    itemsOutput = []
    if items:
        for item in items:
            itemsOutput.append(item.to_dictionary())
    return itemsOutput

@app.get("/item/connect-to-openai")
async def connect_to_openai(messages="[\"Hello ChatGPT.\"]"):
    if messages:
        messages = json.loads(messages)
    service = Service()
    response = service.connect_to_openai(messages)
    return response
