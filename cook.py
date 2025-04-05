def open_file(file:str):
    book={}
    with open(file) as f:
        name_dishes= f.readline()
        while True:
            if not name_dishes:
                break
            elif name_dishes!="\n" :  
                book[name_dishes]=[]
                print(name_dishes)
                numder_ingredient = int(f.readline())
                for i in range(numder_ingredient):
                    ingredient = f.readline().split(' | ')
                    d = {"ingredient_name":ingredient[0],"quantity":int(ingredient[1]),"measure":ingredient[2]}
                    book[name_dishes].append(d)
                name_dishes= f.readline()       
            else:
                name_dishes= f.readline()
    return book

def get_shop_list_by_dishes(dishes, person_count):
    all_ingredient = {}
    cook_book = open_file('recipes.txt')
    for rep in dishes:
        if rep in cook_book:
            for ing in cook_book[rep]:
                if ing["ingredient_name"] in all_ingredient.keys:
                    all_ingredient[ing["ingredient_name"]]["quantity"] += int(ing["quantity"])*person_count
                else:
                    all_ingredient[ing["ingredient_name"]] = {"measure":ing["measure"],"quantity":int(ing["quantity"])*person_count}
    return all_ingredient


            
