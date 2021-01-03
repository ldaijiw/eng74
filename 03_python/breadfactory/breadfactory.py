class BreadFactory:
    
    def make_dough(self, *ingredients):
        print("\nMAKING DOUGH")
        # change all items to lowercase
        ingredients = [item.lower() for item in ingredients]
        # will only return dough if water and flour contained ingredient
        if 'water' in ingredients and 'flour' in ingredients:
            return 'dough'
        return 'Water and flour needed to make dough'
    

    def bake_dough(self, *ingredients):
        print("\nBAKING")
        # change all items to lowercase
        ingredients = [item.lower() for item in ingredients]
        # will only return bread if dough contained in ingredients
        if 'dough' in ingredients:
            return 'bread'
        return 'dough not supplied'


    def run_factory(self, *ingredients):
        # change all items to lowercase
        ingredients = [item.lower() for item in ingredients]
        
        # will attempt to make and bake dough
        product = self.make_dough(*ingredients)
        baked_product = self.bake_dough(product)

        # returns True only if final product is bread
        if baked_product == 'bread':
            print("\nSUCCESSFULLY PRODUCED BREAD")
            return True
        
        return 'Water and flour needed to make bread'
        


def main():
    new_factory = BreadFactory()
    new_factory.run_factory('water', 'flour')


if __name__ == "__main__":
    main()

