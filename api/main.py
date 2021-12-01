from mangum import Mangum
from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/health", status_code=200)
def get_health():
    return {"status_code": "200"}


@app.get("/{currency}")
async def get_currency(currency):
    url = f'https://api.coinbase.com/v2/prices/spot?currency={currency}'
    response = requests.get(url)
    return response.json()

@app.get("/")
async def root():
    return {"message": "Hello World"}

handler = Mangum(app=app)