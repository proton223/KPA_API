from sqlalchemy import Column, Integer, String
from database import Base

class KPAForm(Base):
    __tablename__ = "kpa_forms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    mobile = Column(String)
