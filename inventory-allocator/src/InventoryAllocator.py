class InventoryAllocator():
    """
    This class accepts order as a dictionary and inventory as a list of dictionaries to allocate the 
    orders from corresponding inventories and return the allocation as a list
    """
    def __init__(self, order, inventory):
        # Initializing variables with passed parameters
        self.inventory = inventory
        self.order = order

    def shipment(self):
        if not self.inventory or not self.order: return []  # Checks if inventory and order are properly initialized
        shipment = []  # Initializing output array

        for inventory in self.inventory:  
            available = {}
            for key in self.order.keys():
                if self.order[key] > 0:
                    if key in inventory['inventory'].keys():
                        if inventory['inventory'][key] > self.order[key]:
                            available[key] = self.order[key]
                            inventory['inventory'][key] -= self.order[key]
                            self.order[key] = 0
                        else:
                            available[key] = inventory['inventory'][key]
                            self.order[key] -= inventory['inventory'][key]
                            inventory['inventory'][key] = 0
            shipment.append({inventory['name']: available})

        for key in self.order.keys():
            if self.order[key] > 0: return []
        return shipment


if __name__ == '__main__':
    pass
