# resident.py
# Created by Misha at 14.03.2025
import random
from enum import Enum

from pydantic import BaseModel


class Gender(Enum):
    man: str = "Мужчина"
    woman: str = "Женщина"


class User(BaseModel):
    x: int = 0
    y: int = 0
    fuLL_name: str
    gender: Gender


class Player():
    def __init__(self, name) -> None:
        """

        :param name: Имя ребёнка
        :param Gender: Пол ребёнка
        """
        self.x = 0
        self.y = 0
        self.name = name
        self.age = 0
        self.real_age = 0
        self.gender = random.choice(["Женщина", "Мужчина"])
        a = 0
        b = 0
        if self.gender == "Мужчина":
            a = 0.2
            b = 1
        self.height = random.randint(28, 38) / 10 + a
        self.weight = random.randint(48, 51) / 100 + b
        randoms = random.randint(1, 100)
        if randoms <= 40:
            self.blood_type = "O+"
        elif 40 < randoms <= 49:
            self.blood_type = "O-"
        elif 49 < randoms <= 80:
            self.blood_type = "A+"
        elif 80 < randoms <= 87:
            self.blood_type = "A-"
        elif 87 < randoms <= 95:
            self.blood_type = "B+"
        elif 95 < randoms <= 97:
            self.blood_type = "B-"
        elif 97 < randoms <= 99:
            self.blood_type = "AB+"
        elif randoms == 100:
            self.blood_type = "AB-"
