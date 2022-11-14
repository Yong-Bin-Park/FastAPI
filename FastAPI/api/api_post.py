from fastapi import APIRouter
from conn.db_conn import engineconn
from conn.db_class import Cud_Test
from pydantic import BaseModel

router = APIRouter()
engine = engineconn()
session = engine.sessionmaker()

class Item(BaseModel):
    user_id: str
    password: str 

@router.post("/post",tags=["post"])
async def first_post(item: Item):
    insert_data = Cud_Test(user_id=item.user_id, password=item.password)
    session.add(insert_data)
    session.commit()
    
    return item