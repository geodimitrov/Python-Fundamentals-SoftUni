class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []

    @staticmethod
    def no_avail_space(items, capacity):
        return capacity <= len(items)

    def add_item(self, item):
        if self.no_avail_space(self.items, self.__capacity):
            return "not enough room in the inventory"
        self.items.append(item)


    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity - len(self.items)}"


#Test Code
inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)

