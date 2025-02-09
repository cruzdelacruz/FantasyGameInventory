
class inventory():
    def __init__(self):
        self.inventory = {}
        self.max_capacity = 50
        self.total_inventory = sum(self.inventory.values())

    def add(self,item, count):
        if self.total_inventory < self.max_capacity:
            if item in self.inventory:
                self.inventory[item] += count
                self.total_inventory += count
                print(f"+{count} {item}")
            else:
                self.inventory[item] = count
                self.total_inventory += count
                print(f"new item!, +{count} {item}")
        else:
            print("not enough space in bag!!")
            

    
    def remove(self, item, count):
        if item not in self.inventory:
            print(f"you don't have any {item} to lose!!!")
        else:
            self.inventory[item] -= count
            self.total_inventory -= count
            return(f"-{count} {item}")
    def show_inventory(self):
        print(f"{self.inventory}, total_items={self.total_inventory}")

bag = inventory()

bag.add("apples", 56)
bag.add("rope", 1)

bag.show_inventory()
bag.remove("apples", 4)
bag.show_inventory()

bag.remove("cheese", 4)
