from typing import Optional
from pydantic import BaseModel

class PersonInfo(BaseModel):
    name : str
    age : int
    dead : Optional[bool] = None