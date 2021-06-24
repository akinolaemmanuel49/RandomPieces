from .inventory import Inventory

STATES = ['HEALTHY', 'DEAD', 'UNDEAD', 'POISENED', 'LIMBO', 'INSANE', 'FRACTURED']
class Character:

    def __init__(self, name, hitpoints, defence, attack, agility):
        self.name = name
        self.hitpoints = hitpoints
        self.defence = defence
        self.attack = attack
        self.agility = agility
        self.inventory = Inventory
        self.state = "HEALTHY"
    
    def __repr__(self):
        return f"NAME: {self.name}, HIT: {self.hitpoints}, DEF: {self.defence}, ATK: {self.attack}, AGL: {self.agility}"
