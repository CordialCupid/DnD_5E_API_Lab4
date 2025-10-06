from pydantic import BaseModel

class enemy(BaseModel):
    name: str
    hit_points: int
    damage_dice: str