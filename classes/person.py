from classes.colors import bcolors
import random

def dice(ilosc_scianek):
    return random.randrange(1, ilosc_scianek)


def skill_main_display(skill):
    return bcolors.OKGREEN + skill + ":" + bcolors.ENDC


def skill_secondary_display(skill):
    return bcolors.OKBLUE + skill + ":" + bcolors.ENDC

class Person:
    def __init__(self, attacks, rasa, name):
        self.name = name
        self.actions = ["Zaatakuj", "Idź", "Zbadaj", "Spójrz w lewo", "Spójrz w prawo"]
        self.attacks = attacks
        self.action_points = 2
        if rasa == "człowiek":
            # main stats
            self.ww = 20 + 2*dice(11)
            self.us = 20 + 2*dice(11)
            self.k = 20 + 2*dice(11)
            self.odp = 20 + 2*dice(11)
            self.zr = 20 + 2*dice(11)
            self.int = 20 + 2*dice(11)
            self.sw = 20 + 2*dice(11)
            self.ogd = 20 + 2*dice(11)

            # secondary stats
            self.a = 1

            if dice(11) <= 3:
                self.zyw = 10
            elif dice(11) > 3 and dice(11) <= 6:
                self.zyw = 11
            elif dice(11) > 6 and dice(11) <= 9:
                self.zyw = 12
            else:
                self.zyw = 13

            self.maxzyw = self.zyw
            self.s_roll = divmod(self.k, 10)
            self.wt_roll = divmod(self.odp, 10)
            self.s = self.s_roll[0]
            self.wt = self.wt_roll[0]
            self.mag = 0
            self.po = 0
            if dice(11) <= 4:
                self.pp = 2
            else:
                self.pp = 3


        elif rasa == "elf":
            # main stats
            self.ww = 20 + 2 * dice(11)
            self.us = 30 + 2 * dice(11)
            self.k = 20 + 2 * dice(11)
            self.odp = 20 + 2 * dice(11)
            self.zr = 30 + 2 * dice(11)
            self.int = 20 + 2 * dice(11)
            self.sw = 20 + 2 * dice(11)
            self.ogd = 20 + 2 * dice(11)

            # secondary stats
            self.a = 1

            if dice(11) <= 3:
                self.zyw = 9
            elif dice(11) > 3 and dice(11) <= 6:
                self.zyw = 10
            elif dice(11) > 6 and dice(11) <= 9:
                self.zyw = 11
            else:
                self.zyw = 12

            self.maxzyw = self.zyw
            self.s_roll = divmod(self.k, 10)
            self.wt_roll = divmod(self.odp, 10)
            self.s = self.s_roll[0]
            self.wt = self.wt_roll[0]
            self.mag = 0
            self.po = 0
            if dice(11) <= 4:
                self.pp = 1
            else:
                self.pp = 2

        elif rasa == "krasnolud":
            # main stats
            self.ww = 30 + 2 * dice(11)
            self.us = 20 + 2 * dice(11)
            self.k = 20 + 2 * dice(11)
            self.odp = 30 + 2 * dice(11)
            self.zr = 10 + 2 * dice(11)
            self.int = 20 + 2 * dice(11)
            self.sw = 20 + 2 * dice(11)
            self.ogd = 10 + 2 * dice(11)

            # secondary stats
            self.a = 1

            if dice(11) <= 3:
                self.zyw = 11
            elif dice(11) > 3 and dice(11) <= 6:
                self.zyw = 12
            elif dice(11) > 6 and dice(11) <= 9:
                self.zyw = 13
            else:
                self.zyw = 14

            self.maxzyw = self.zyw
            self.s_roll = divmod(self.k, 10)
            self.wt_roll = divmod(self.odp, 10)
            self.s = self.s_roll[0]
            self.wt = self.wt_roll[0]
            self.mag = 0
            self.po = 0
            if dice(11) <= 4:
                self.pp = 1
            elif dice(11) > 4 and dice(11) <= 7:
                self.pp = 2
            else:
                self.pp = 3

        elif rasa == "niziołek":
            # main stats
            self.ww = 10 + 2 * dice(11)
            self.us = 30 + 2 * dice(11)
            self.k = 10 + 2 * dice(11)
            self.odp = 10 + 2 * dice(11)
            self.zr = 30 + 2 * dice(11)
            self.int = 20 + 2 * dice(11)
            self.sw = 20 + 2 * dice(11)
            self.ogd = 30 + 2 * dice(11)

            # secondary stats
            self.a = 1

            if dice(11) <= 3:
                self.zyw = 8
            elif dice(11) > 3 and dice(11) <= 6:
                self.zyw = 9
            elif dice(11) > 6 and dice(11) <= 9:
                self.zyw = 10
            else:
                self.zyw = 11

            self.maxzyw = self.zyw
            self.s_roll = divmod(self.k, 10)
            self.wt_roll = divmod(self.odp, 10)
            self.s = self.s_roll[0]
            self.wt = self.wt_roll[0]
            self.mag = 0
            self.po = 0
            if dice(11) <= 4:
                self.pp = 2
            else:
                self.pp = 3

    def rzut(self, stat):
        roll_result = False
        roll = dice(100)+1
        if stat == self.ww:
            print("Wykonałeś rzut na", skill_main_display("Walka Wręcz"))
        elif stat == self.us:
            print("Wykonałeś rzut na", skill_main_display("Umiejętności strzeleckie"))
        elif stat == self.k:
            print("Wykonałeś rzut na", skill_main_display("Krzepa"))
        elif stat == self.odp:
            print("Wykonałeś rzut na", skill_main_display("Odporność"))
        elif stat == self.zr:
            print("Wykonałeś rzut na", skill_main_display("Zręczność"))
        elif stat == self.int:
            print("Wykonałeś rzut na", skill_main_display("Inteligencja"))
        elif stat == self.sw:
            print("Wykonałeś rzut na", skill_main_display("Siła woli"))
        elif stat == self.ogd:
            print("Wykonałeś rzut na", skill_main_display("Ogłada"))

        if roll <= stat:
            print("Wyrzuciles", roll, "rzut się udał!")
            roll_result = True
        elif roll > stat:
            print("Wyrzuciłeś", roll, "rzut się nie udał!")
            roll_result = False
        else:
            print("Coś poszło nie tak")
            print(roll)
        return roll_result

    def roll_stats(self):
        stat = dice(101)
        return stat

    def generate_damage(self):
        roll = dice(10)+1
        dmg = roll + self.s
        return dmg

    def take_damage(self, dmg):
        self.zyw -= (dmg - self.wt)
        if self.zyw < 0:
            self.zyw = 0
        return self.zyw

    def get_zyw(self):
        return self.zyw

    def get_max_zyw(self):
        return self.get_max_zyw()

    def get_attack_name(self, i):
        return self.attacks[i]["name"]

    def get_attack_cost(self, i):
        return self.attacks[i]["cost"]

    def choose_action(self):
        i = 1
        print("Co chcesz zrobić?")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1
    #TODO
    def choose_attack(self):
        i = 0
        print("Jak chcesz zaatakować")
        for attack in self.attacks:
            print(str(i+1) + ":", attack["name"], "(zużywa", attack["cost"], "punktów akcji)." )
            i += 1