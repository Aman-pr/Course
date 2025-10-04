from pydantic import BaseModel
from typing import Optional,fields
class Detiels(BaseModel):
    age: Optional[int]=None
    address: str="unknown"
    phone: str ="000-0000"
    salary: float=fields(gt=0)

new_person={}
new_entery=Detiels(**new_person)
print(new_entery)