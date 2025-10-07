from pydantic import BaseModel
from typing import Dict

class damage(BaseModel):
    damage_at_character_level: Dict[str, str]
    
class player_spell(BaseModel):
    name: str
    damage: damage
