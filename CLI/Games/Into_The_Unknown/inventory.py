class Item(object):

    def __init__(self, name, attack, defense, weight, hitpoints):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.weight = weight
        self.hitpoints = hitpoints

class Inventory(object):
    
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        self.items[item.name] = item

    def __str__(self):
        out = '\t'.join(['Name', 'Atk', 'Def', 'Mass', 'Hit'])
        for item in self.items.values():
            out += '\n' + '\t'.join([str(x) for x in [item.name, item.attack, item.defense, item.weight, item.hitpoints]])
            return out

    
