class Ingredient:
    def __init__(self, i):
        split_i = i.split(',')
        self.name = split_i[0]
        self.aisle = split_i[1]
        self.price = split_i[2]
         
