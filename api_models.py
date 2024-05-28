from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.get('/')
async def index():
    return {
        "message": "index_api"
    }

@app.get('/items/')
async def create_item(item: Item) -> Item:
    return item


@app.post('/items/')
async def read_items() -> list:
    return [
        {
            "name": "John",
            'password': 'hond451'
        },
        {
            "name": "kamron",
            'password': '2604'
        },
        {
            "name": "anver",
            'password': '0515'
        }

    ]
