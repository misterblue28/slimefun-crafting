import math

global RECIPES
global CUSTOMBASE
global itemTotals


class ItemAmount:
    def __init__(self, txt):
        txt = txt.split("*")
        self.item = txt[1]
        self.quantity = int(txt[0])

class Recipe:
    def __init__(self, txt):
        txt = txt.replace("\n", "")
        txt = txt.split(" ")
        self.ingredients = []
        for index, term in enumerate(txt):
            if index == 0:
                self.product = ItemAmount(term)
                if self.product.item in CUSTOMBASE:
                    self.ingredients = []
                    return None
            else:
                self.ingredients.append(ItemAmount(term))

class Node:
    def __init__(self, product):
        self.product = product
        self.children = None
        for r in RECIPES:
            if r.product.item == self.product.item:
                self.children = []  # error checking: children stays None if recipe missing
                for i in r.ingredients:
                    childQuantity = i.quantity * math.ceil(self.product.quantity / r.product.quantity)
                    self.children.append(Node(ItemAmount(f"{childQuantity}*{i.item}")))
                break
        if self.children == None:
            print("Error: missing recipe for " + self.product.item)
            exit()
        if self.children == []:
            self.leafDist = 0
        else:
            childrenLDs = []
            for c in self.children:
                childrenLDs.append(c.leafDist)
            self.leafDist = max(childrenLDs) + 1
        for i in itemTotals[self.leafDist]:
            if i.item == self.product.item:
                i.quantity += int(self.product.quantity)
                return None
        itemTotals[self.leafDist].append(self.product)


CUSTOMBASE = []
with open("custombase.sf") as cb:
    cbLines = cb.readlines()
    for i in cbLines:
        i = i.replace("\n", "")
        CUSTOMBASE.append(i)

RECIPES = []
with open("crafting.sf") as crafting:
    craftLines = crafting.readlines()
    for r in craftLines:
        RECIPES.append(Recipe(r))


itemTotals = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

products = []
roots = []
with open("input.sf") as inputData:
    products = inputData.readlines()
    for p in products:
        p = p.replace("\n", "")
        roots.append(Node(ItemAmount(p)))

for level in range(20):
    print()
    for i in itemTotals[level]:
        print(str(i.quantity) + " * " + i.item + " ")