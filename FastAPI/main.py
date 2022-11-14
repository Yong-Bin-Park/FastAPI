from fastapi import FastAPI
from api import api_get, api_post, api_put, api_delete

def include_router(app):
    app.include_router(api_get.router, prefix='/main')
    app.include_router(api_post.router, prefix='/main')
    app.include_router(api_put.router, prefix='/main')
    app.include_router(api_delete.router, prefix='/main')

def start_application():
    app = FastAPI()
    include_router(app)
    return app

app = start_application()



# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Optional[bool] = None

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

# @app.post("/test")
# async def post_test(item: Item):
#     return item