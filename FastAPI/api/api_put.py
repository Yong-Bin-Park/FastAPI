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

@router.put("/put",tags=["put"])
async def first_put(item: Item):
    message = ""
    try:
        if not item.user_id:
            raise Exception("missing user_id")
        update_data = session.query(Cud_Test).filter(Cud_Test.user_id == item.user_id).first()
        update_data.password = item.password
        session.commit()
        session.refresh(update_data)
        message = "Update success"

    except Exception as e:
        message = "{}".format(e)

    return {"message": message}