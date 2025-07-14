from pydantic import BaseModel

class KPAFormCreate(BaseModel):
    name: str
    email: str
    mobile: str

class KPAFormResponse(KPAFormCreate):
    id: int
    class Config:
        orm_mode = True
