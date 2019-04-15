from classes.game import *
from classes.person import *

attacks = [{
    "name": "Atak", "cost": "1",
    "name": "Szarża", "cost": "2",
    "name": "Celowany Atak", "cost": "2",
}]

items = [{
    "name": "Annihilator", "type": "weapon", "weapon_type": "sword",
    "name": "Defender", "type": "shield",
    "name": "Firestorm", "type": "armor", "armor_type": "plate", "armor_cover": "body",
    "name": "Necronomicon", "type": "book", "book_type": "spell_book", "school": "Death",
}]

# tworzenie postaci
print(bcolors.BOLD + "Tworznie postaci" + bcolors.ENDC)
print("Dostępne rasy: Człowiek, Elf, Krasnolud, Niziołek")
race_choice = input("Wybierz rase: ").lower()
print("Wybrałeś", race_choice + "a")
name_choice = input("Jak chcesz się nazywać: ")

mapa = Map()
mapa.room_creation()

player = Person(attacks, race_choice, name_choice)
running = True
i = 0

print("Oto", name_choice + ",", "dumny", race_choice.lower())

print(skill_main_display("Walka Wręcz"), player.ww,
      skill_main_display("\nUmiejętnosci strzeleckie"), player.us,
      skill_main_display("\nKrzepa"), player.k,
      skill_main_display("\nOdporność"), player.odp,
      skill_main_display("\nZręczność"), player.zr,
      skill_main_display("\nInteligencja"), player.int,
      skill_main_display("\nSiła Woli"), player.sw,
      skill_main_display("\nOgłada"), player.ogd)

print(skill_secondary_display("Ataki"), player.a,
      skill_secondary_display("\nŻywotność"), player.zyw,
      skill_secondary_display("\nSiła"), player.s,
      skill_secondary_display("\nWytrzymałość"), player.wt,
      skill_secondary_display("\nPunkty Magii"), player.mag,
      skill_secondary_display("\nPunkty Obłędu"), player.po,
      skill_secondary_display("\nPunkty Przeznaczenia"), player.pp)

enemies = []
directions = ["Lewo", "Prawo", "Prosto"]
enemy = Person(attacks, race_choice, "Ohimura")
enemy2 = Person(attacks, race_choice, "Avalon")
enemies.append(enemy)
enemies.append(enemy2)

while running:
    print("=================================")
    player.choose_action()
    choice = input("> ")
    index = int(choice)

    if index == 1:
        print("Wybierz swój cel: ")
        target_list = 0
        for enemy in enemies:
            print(target_list + 1, ":", enemy.name, "Żywotność:", enemy.zyw)
            target_list += 1

        # Wybieranie przeciwnika
        target = int(input("> "))
        dmg = player.generate_damage()
        print("Obrażenia:", dmg)
        enemies[target - 1].take_damage(dmg)
        print(enemies[target - 1].name, "posiada", enemies[target - 1].wt, "wytrzymałości.")
        print("Zadałeś", dmg - enemies[target - 1].wt, "obrażeń.")
        print(enemies[target - 1].name, "ma", enemies[target - 1].zyw, "punktów życia")

    elif index == 2:
        print("Gdzie chcesz iść?")
        go_list = 0
        for direction in directions:
            print(go_list + 1, ":", direction)
            go_list += 1
        go_to = int(input("> "))
        if go_to == 1:
            print("Wchodzisz do:")

    elif index == 3:
        pass
    #TODO
        #for item in map_schema:
          #  i = 0
           # print(item)
            #i += 1

running = False
