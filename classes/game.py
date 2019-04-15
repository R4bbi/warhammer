import random
from classes.colors import bcolors
from classes.person import Person


class Room:
    def __init__(self, room_name, room_difficult, room_danger, room_reward, room_options):
        self.room_name = room_name
        self.room_difficult = room_difficult
        self.room_danger = room_danger
        self.room_reward = room_reward
        self.room_options = room_options

class Map:
    rooms = []

    def __init__(self):
        pass
    def room_creation(self):
        room_names = [
            "Łazienka",
            "Rzeźnia",
            "Ogród",
            "Przedpokój",
            "Garaż",
            "Sklep",
            "Kuchnia",
            "Salon",
            "Piwnica",
        ]
        room_difficult = [
            "Low",
            "Medium",
            "Hard",
            "Insane"
        ]
        room_danger = [
            "Monster",
            "Trap",
        ]
        room_reward = [
            "Annihilator",
            "Defender",
            "Firestorm",
            "Necronomicon",
        ]

        room_options = [
            "Lewo",
            "Prawo",
            "Prosto"
        ]

        map_schema = (
            [], [], [],
            [], [], [],
            [], [], []
        )
        i = 0

        for rooms in room_names:
            random_room_name = random.randrange(0, 9)
            difficult = random.randrange(0,4)
            danger = random.randrange(0,1)
            reward = random.randrange(0,4)
            options = random.randrange(0,3)
            room = Room(
                room_names[random_room_name],
                room_difficult[difficult],
                room_danger[danger],
                room_reward[reward],
                room_options[options]
                    )
            map_schema[i].append(room.room_name)
            i += 1
        #TODO
        for item in map_schema:
            i = 0
            print(item)
            i += 1