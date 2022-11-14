from sqlalchemy import Column,INT,String
from sqlalchemy.orm import declarative_base

#상속클래스들을 자동으로 인지하고 알아서 매핑해줌.
Base = declarative_base()

#Mapping
class Cud_Test(Base):
    __tablename__ = "cud_test"
    idx = Column(INT,primary_key=True,nullable=False,autoincrement=True)
    user_id = Column(String)
    password = Column(String)