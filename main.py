from file_utils import get_random_from_file
from character import Hero, Villain

hero_name = get_random_from_file(r"C:\Users\37257\Documents\Python_projects\week_14\heroes.txt")
hero_weapon = get_random_from_file(r"C:\Users\37257\Documents\Python_projects\week_14\weapons.txt")
villain_name = get_random_from_file(r"C:\Users\37257\Documents\Python_projects\week_14\villains.txt")
villain_weapon = get_random_from_file(r"C:\Users\37257\Documents\Python_projects\week_14\weapons.txt")
round_number = 1



hero = Hero(hero_name, hero_weapon)
villain = Villain(villain_name, villain_weapon)

print("=== BATTLE BEGINS ===")

print(f"Hero: {hero.name}  HP: {hero.hp}   Weapon: {hero.weapon}")
print(f"Villian: {villain.name}  HP: {villain.hp}   Weapon: {villain.weapon}")

while hero.is_alive() and villain.is_alive():
    print(f"--- Round {round_number} --- ")

    hero.attack(villain)

    if not villain.is_alive():
        break

    villain.attact(hero)
    round_number = round_number + 1

    print("=== BATTLE ENDS ===")

    if hero.is_alive():
        print("Hero saves the day! ")
    else:
        print("Dark side wins")


# print(hero)
# print(hero_weapon)
# print(villain)
# print(villain_weapon)

