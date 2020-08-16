class Cocktail:
    def __init__(self, vodka, whiskey, gin):
        self.vod = vodka
        self.whis = whiskey
        self.g = gin
        print("Your cocktail is ready!")
    def __del__(self):
        print("You ran out of Cocktail :( ")
    def add_ingredient(self, name, ml):
        self.ingedient = name
        self.quantity = ml
