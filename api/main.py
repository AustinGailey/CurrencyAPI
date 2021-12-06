from mangum import Mangum
from fastapi import FastAPI
import requests
import boto3

app = FastAPI()

@app.get("/health", status_code=200)
def get_health():
    cloudwatch = boto3.client('cloudwatch')
    paginator = cloudwatch.get_paginator('list_metrics')
    response = paginator.paginate(Dimensions=[{'Name': 'LogGroupName'}],MetricName='IncomingLogEvents',Namespace='AWS/Logs')
    return response


@app.get("/{currency}")
async def get_currency(currency):
    url = f'https://api.coinbase.com/v2/prices/spot?currency={currency}'
    response = requests.get(url)
    return response.json()

@app.get("/", status_code=200)
async def root():
    return {"message": "Currency API"}

handler = Mangum(app=app)