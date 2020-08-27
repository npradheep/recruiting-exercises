import unittest
from InventoryAllocator import InventoryAllocator

class InventoryAllocatorTest(unittest.TestCase):

    def testHappyCase(self):
        order = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1}}]
        output = [{'owd': {'apple': 1}}]
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

    def testNotEnoughInventory(self):
        order = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 0}}]
        output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

    def testSplitWarehouses(self):
        order = {'apple': 10}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}]
        output = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

    def testItemNotFound(self):
        order = {'melon': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}]
        output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

    def testAbundantInventory(self):
        order = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}]
        output = [{'owd': {'apple': 1}}, {'dm': {}}]
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

    def testUpdateInventorySingleWarehouse(self):
        order = {'apple': 1}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}}]
        output = [{'name': 'owd', 'inventory': {'apple': 4}}]
        inventory_allocator = InventoryAllocator(order, inventory)
        inventory_allocator.shipment()
        self.assertEqual(inventory_allocator.inventory, output)

    def testUpdateInventoryMultipleWarehouse(self):
        order = {'apple': 3}
        inventory = [{'name': 'owd', 'inventory': {'apple': 1, 'orange':3}}, {'name': 'dm', 'inventory': {'apple': 2, 'mango':2}}]
        output = [{'name': 'owd', 'inventory': {'apple': 0, 'orange':3}}, {'name': 'dm', 'inventory': {'apple': 0, 'mango':2}}]
        inventory_allocator = InventoryAllocator(order, inventory)
        inventory_allocator.shipment()
        self.assertEqual(inventory_allocator.inventory, output)

    def testNone(self):
        order = {}
        inventory = []
        output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

        order = None
        inventory = None
        output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

    def testOrder(self):
        order = {}
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}]
        output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

        order = None
        inventory = [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}]
        output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

    def testInventory(self):
        order = {'apple': 10}
        inventory = []
        output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)

        order = {'apple': 10}
        inventory = None
        output = []
        inventory_allocator = InventoryAllocator(order, inventory)
        self.assertEqual(inventory_allocator.shipment(), output)


if __name__ == '__main__':
    unittest.main()
