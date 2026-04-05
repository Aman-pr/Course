from fastapi import FastAPI
import sys #import from termianl 
from typing import Any,Annotated # for documation validation    
from enum import Enum # for predefing the valus or set of value

#enum 
class emp_id_number(int,Enum):
        emp_101=1
        emp_102=2
        emp_103=3  
        emp_104=4
        emp_105=5
        emp_106=6



app=FastAPI()

def main(first_name :Annotated[str,"First name of person"] , last_name :Annotated[Any,"last name of person"] , Age : Annotated[int,"the age of person"]):
        full_name = f"{first_name.title()} {last_name.title()} {Age}"
        print(full_name)


@app.get("/")
async def greeting_root():
        return{"Message" :"welcome"}


@app.get("/emp_record/{emp_id}")
async def root(emp_id:emp_id_number):
        print("hwllo first post ")
        if emp_id is emp_id_number.emp_101:
                return{"id":emp_id,"Name":"Mohd Aman","Age":34}
        elif emp_id is emp_id_number.emp_102:
                return{"id":emp_id,"Name":"Rashi","Age":30}
        else:
                return{}

@app.get("/skip_limit")
async def limit(skip:int=1,limit:int=5):
        list_numgber = list(range(1,10))
        return list_numgber[skip: skip + limit]


if __name__ == "__main__":
        first_name=sys.argv[1]
        last_name=sys.argv[2]
        Age=sys.argv[3]
        main(first_name,last_name,Age)
        


