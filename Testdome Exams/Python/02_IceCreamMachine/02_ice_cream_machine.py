from itertools import product


class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        all_scoops = []
        for i in self.ingredients:
            for t in self.toppings:
                scoop = [i, t]
                all_scoops.append(scoop)
        return all_scoops
        # return list(product(self.ingredients, self.toppings))


def main():
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce", "Strawberry sauce", "Blueberry Sauce"])
    print(machine.scoops())
    # [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]


if __name__ == '__main__':
    main()
