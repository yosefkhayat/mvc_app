from pydantic import BaseModel

class Sales(BaseModel):
    date:str
    item_sold:int
    cost:int