from pydantic import BaseModel
from damage import damage
from typing import List

class action(BaseModel):
    name: str
    damage: List[damage]