
from vikingsClasses import Soldier, Viking, Saxon, War
import random


soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]

war = War()

#Create 5 Vikings
for i in range(0,5):
    if i:
        viking = Viking(soldier_names[random.randint(0, 9)], 100, random.randint(0, 100))
        war.addViking(viking)

#Create 5 Saxons
for i in range(0,5):
    if i:
        saxon = Saxon(100, random.randint(0, 100))
        war.addSaxon(saxon)




round = 0
while war.showStatus() == "Los Vikingos y los Sajones todavía están en plena batalla.":
    war.vikingAttack()
    war.saxonAttack()
    print(f"\n*************** RONDA NÚMERO: {round} **************\n  Viking army: {len(war.vikingArmy)} warriors", f" ||  Saxon army: {len(war.saxonArmy)} warriors")
    print(war.showStatus())
    print("\n***Estado Ejercitos***")
    print("Ejército Vikingo:")
    for viking in war.vikingArmy:
        print(f"  Nombre: {viking.name}, Salud: {viking.health}, Fuerza: {viking.strength}")

    print("Ejército Sajón:")
    for saxon in war.saxonArmy:
        print(f"  Salud: {saxon.health}, Fuerza: {saxon.strength}")

    round += 1

