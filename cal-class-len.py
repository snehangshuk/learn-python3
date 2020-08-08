class Bag:
    def __init__(self, item_count):
        self.item_count = item_count

    def __len__(self):
        return self.item_count


mybag = Bag(10)

print(len(mybag))
