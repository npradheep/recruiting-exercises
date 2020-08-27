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
        '''
        This method iterates through the given inventory list and order dictionary
        to find if all the orders are available in the given inventory
        '''
        if not self.inventory or not self.order: return []  # Checks if inventory and order are properly initialized
        shipment = []  # Initializing output array

        for inventory in self.inventory:  # Iterating through given inventory
            available = {}  # This array keeps track of the availability of the item in each inventory
            for key in self.order.keys():  # Iterating through the given order
                #  Proceeds only if one or more quantity of the specific item in the order is required
                if self.order[key] > 0:
                    # If the item is available, add to shipment and update the inventory
                    if key in inventory['inventory'].keys():
                        #  If the requested quantity is fully available
                        if inventory['inventory'][key] > self.order[key]:
                            available[key] = self.order[key]
                            inventory['inventory'][key] -= self.order[key]
                            self.order[key] = 0
                        # If a portion of the requested quantity is available
                        else:
                            available[key] = inventory['inventory'][key]
                            self.order[key] -= inventory['inventory'][key]
                            inventory['inventory'][key] = 0
            shipment.append({inventory['name']: available}) # Update the shipment with
        
        #  If not all orders are present in the inventory, return 
        for key in self.order.keys():
            if self.order[key] > 0: return []
        return shipment