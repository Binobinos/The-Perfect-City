import time

from model.resident import Player

if __name__ == "__main__":
    user_list = []
    user = Player("Никита")
    user2 = Player("Маша")
    user_list.append(user)
    speed = 100000
    while True:
        for i in user_list:
            print(i.name)
            i.Live_day()
        time.sleep(1 / speed)
