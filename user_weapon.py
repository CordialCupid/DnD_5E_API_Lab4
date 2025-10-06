from pydantic import BaseModel

class weapon(BaseModel):
    name: str
    damage_dice: str

