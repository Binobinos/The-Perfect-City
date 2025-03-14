# resident.py
# Created by Misha at 14.03.2025
import random

from pydantic import BaseModel, Enum


class Gender(Enum):
    man: str = "Мужчина"
    woman: str = "Женщина"


class User(BaseModel):
    x: int = 0
    y: int = 0
    fuLL_name: str
    gender: Gender
