# resident.py
# Created by Misha at 14.03.2025
import random
import time
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


def chance(chance: int) -> bool:
    return random.randint(1, 100) <= chance


class Player():
    def __init__(self, name) -> None:
        """

        :param name: Имя ребёнка
        :param Gender: Пол ребёнка
        """
        self.x = 0
        self.y = 0
        self.name = name
        self.age = 1
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
        self.__day = 0
        self.immunity = 1

    def Live_day(self) -> None:
        """
        Жизнь один день
        :return: None
        """
        if not self.__day == 365:
            self.__day += 1
        else:
            self.age += 1
            self.__day = 1

        print(f"День {self.__day} прожит, Возврат {self.age}")


if __name__ == "__main__":
    user = Player("Никита")
    speed = 100
    while True:
        user.Live_day()
        time.sleep(1 / speed)
