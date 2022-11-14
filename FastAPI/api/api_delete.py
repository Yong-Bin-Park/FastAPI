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

@router.delete("/delete",tags=["delete"])
async def first_delete(item: Item):
    message = ""
    try:
        if not item.user_id:
            raise Exception("missing user_id")
        delete_data = session.query(Cud_Test).filter(Cud_Test.user_id == item.user_id).first()
        session.delete(delete_data)
        session.commit()
        session.refresh(delete_data)
        message = "Delete success"

    except Exception as e:
        message = "{}".format(e)

    return {"message": message}