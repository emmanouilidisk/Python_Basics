class Cocktail:
    def __init__(self, vodka, whiskey, gin):
        self.vod = vodka
        self.whis = whiskey
        self.g = gin
        print("Your cocktail is ready!")
    def __del__(self):
        print("Bye")
    def add_ingredient(self, name, ml):
        self.ingedient = name
        self.quantity = ml
        
def main():
    print("Welcome to the Cocktail Bar!")
    ch = input("Do you want a cocktail? Press y for YES and n for NO")
    while(ch == "y" or ch == "Y"):
        vodka_ml = input("Give quantity of vodka")
        whiskey_ml = input("Give quantity of whiskey")
        gin_ml = input("Give quantity of gin")
        cockt = Cocktail(vodka_ml,whiskey_ml,gin_ml)
        d = input("Do you want any other ingredient? Press y for Yes, n for No")
        if(d == "y" or d == "Y"):
            extra_ingr = input("Name the extra ingredient you want to add")
            extra_ingr_ml = input("Give quantity of the extra ingredient")
            cockt.add_ingredient(extra_ingr,extra_ingr_ml)
        print("Your cocktail is ready!!!")
        ch = input("Do you want a cocktail? Press y for YES and n for No ")

main()






            





        
