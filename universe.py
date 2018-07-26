class Southeros:
    kingdom_emblem_map = {"Land":"Panda", "Water":"Octopus", "Ice":"Mammoth", "Air":"Owl", "Fire":"Dragon"}
    def __init__(self):
        self.ruler = "None"
        self.allies = []
    def checkRulerAndAllies(self):
        return self.ruler, self.allies
    def getKingdomEmblemMap(self):
        return self.kingdom_emblem_map
    
