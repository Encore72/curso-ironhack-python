import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:  # Check for health less than or equal to 0
            self.health = 0  # Set health to 0 for consistency (optional)
            return f"{self.name} ha muerto en acto de combate"
        else:
            return f"{self.name} ha recibido {damage} puntos de daño"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0  # Set health to 0 for consistency
            return f"Un 'Saxon' ha muerto en combate"
        else:
            return f"Un 'Saxon' ha recibido {damage} puntos de daño"

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        if not self.saxonArmy or not self.vikingArmy:
            return
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        if random_saxon.receiveDamage(random_viking.strength) and random_saxon.health == 0:
            self.saxonArmy.remove(random_saxon)

    def saxonAttack(self):
        if not self.vikingArmy or not self.saxonArmy:
            return
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        if random_viking.receiveDamage(random_saxon.strength) and random_viking.health == 0:
            self.vikingArmy.remove(random_viking)

    def showStatus(self):
        if not self.saxonArmy:
            return "¡Los Vikingos han ganado la guerra del siglo!"
        elif not self.vikingArmy:
            return "Los Sajones han luchado por sus vidas y sobreviven otro día..."
        else:
            return "Los Vikingos y los Sajones todavía están en plena batalla."

    pass
