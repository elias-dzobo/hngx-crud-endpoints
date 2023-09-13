from typing import List
from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    id: str or None = None 
    name: str
    track: str 


    class Config:
        orm_mode = True 
        allow_population_by_field_name = True
        arbitrary_types_allowed = True 


class ListUserResponse(BaseModel):
    status: str
    results: int 
    users: List[UserBaseSchema]


    