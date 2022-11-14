from fastapi import APIRouter
from conn.db_conn import engineconn
from conn.db_class import Cud_Test

router = APIRouter()
engine = engineconn()
session = engine.sessionmaker()


@router.get("/",tags=["get"])
async def first_get():
    select_data = session.query(Cud_Test).all()
    return select_data