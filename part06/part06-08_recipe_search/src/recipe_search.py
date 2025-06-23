def search_by_name():
    recipes = {}
    lines = []
    with open("recipes1.txt") as new_file:
        for line in new_file:
            if line == "\n":
                name = lines[0].strip()
                ingredients = [item.strip() for item in lines[1:]]
                recipes[name] = ingredients
                lines = []
            else:
                lines.append(line)
    print(recipes)

            
'''def hello():
    x = input("hello: ")
    list1 = ["hell","jello","mellow"]
    list2 = []
    for items in list1:
        print(items)
        if x in items:
            pass'''
search_by_name()