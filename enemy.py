from pydantic import BaseModel
from typing import List
from armor_class import armor_class
from damage import damage
from action import action

class enemy(BaseModel):
    name: str
    armor_class: List[armor_class]
    hit_points: int
    actions: List[action]