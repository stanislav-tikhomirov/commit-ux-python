from enum import Enum

from entities import *


class ItemType(Enum):
    FIRST_NAME = 1
    SECOND_NAME = 2
    CITY = 3
    STREET = 4
    ORDER_DESCRIPTION = 5


class DataProvider:
    def __init__(self):
        self.account_managers: List[AccountManager] = [
            AccountManager(self.get_random_item(ItemType.FIRST_NAME), self.get_random_item(ItemType.SECOND_NAME),
                           "WestCorp"),
            AccountManager(self.get_random_item(ItemType.FIRST_NAME), self.get_random_item(ItemType.SECOND_NAME),
                           "EastCorp"),
            AccountManager(self.get_random_item(ItemType.FIRST_NAME), self.get_random_item(ItemType.SECOND_NAME),
                           "NorthCorp")]
        self.accounts: List[Account] = [
            Account(uuid4(), self.get_random_item(ItemType.FIRST_NAME), self.get_random_item(ItemType.SECOND_NAME),
                    self.account_managers[0]),
            Account(uuid4(), self.get_random_item(ItemType.FIRST_NAME), self.get_random_item(ItemType.SECOND_NAME),
                    self.account_managers[0]),
            Account(uuid4(), self.get_random_item(ItemType.FIRST_NAME), self.get_random_item(ItemType.SECOND_NAME),
                    self.account_managers[1]),
            Account(uuid4(), self.get_random_item(ItemType.FIRST_NAME), self.get_random_item(ItemType.SECOND_NAME),
                    self.account_managers[2])]
        self.addresses: List[Address] = [
            Address("United States", self.get_random_item(ItemType.CITY), self.get_random_item(ItemType.STREET),
                    random.randrange(0, 100), random.randrange(0, 100)),
            Address("United States", self.get_random_item(ItemType.CITY), self.get_random_item(ItemType.STREET),
                    random.randrange(0, 100), random.randrange(0, 100)),
            Address("United States", self.get_random_item(ItemType.CITY), self.get_random_item(ItemType.STREET),
                    random.randrange(0, 100), random.randrange(0, 100)),
            Address("United States", self.get_random_item(ItemType.CITY), self.get_random_item(ItemType.STREET),
                    random.randrange(0, 100), random.randrange(0, 100)),
            Address("United States", self.get_random_item(ItemType.CITY), self.get_random_item(ItemType.STREET),
                    random.randrange(0, 100), random.randrange(0, 100)),
            Address("United States", self.get_random_item(ItemType.CITY), self.get_random_item(ItemType.STREET),
                    random.randrange(0, 100), random.randrange(0, 100))]
        self.order_items: List[OrderItem] = [
            OrderItem(random.randrange(10, 100), self.get_random_item(ItemType.ORDER_DESCRIPTION)),
            OrderItem(random.randrange(10, 100), self.get_random_item(ItemType.ORDER_DESCRIPTION)),
            OrderItem(random.randrange(10, 100), self.get_random_item(ItemType.ORDER_DESCRIPTION)),
            OrderItem(random.randrange(10, 100), self.get_random_item(ItemType.ORDER_DESCRIPTION)),
            OrderItem(random.randrange(10, 100), self.get_random_item(ItemType.ORDER_DESCRIPTION)),
            OrderItem(random.randrange(10, 100), self.get_random_item(ItemType.ORDER_DESCRIPTION)),
            OrderItem(random.randrange(10, 100), self.get_random_item(ItemType.ORDER_DESCRIPTION)),
            OrderItem(random.randrange(10, 100), self.get_random_item(ItemType.ORDER_DESCRIPTION)),
            OrderItem(random.randrange(10, 100), self.get_random_item(ItemType.ORDER_DESCRIPTION)),
            OrderItem(random.randrange(10, 100), self.get_random_item(ItemType.ORDER_DESCRIPTION)),
            OrderItem(random.randrange(10, 100), self.get_random_item(ItemType.ORDER_DESCRIPTION)),
            OrderItem(random.randrange(10, 100), self.get_random_item(ItemType.ORDER_DESCRIPTION)),
            OrderItem(random.randrange(10, 100), self.get_random_item(ItemType.ORDER_DESCRIPTION)),
            OrderItem(random.randrange(10, 100), self.get_random_item(ItemType.ORDER_DESCRIPTION)),
            OrderItem(random.randrange(10, 100), self.get_random_item(ItemType.ORDER_DESCRIPTION)),
            OrderItem(random.randrange(10, 100), self.get_random_item(ItemType.ORDER_DESCRIPTION))]

    def get_random_item(self, item_type: ItemType) -> str:
        first_names = ["James", "John", "Robert", "Michael", "William", "Mary", "Patricia", "Jennifer", "Linda",
                       "Elizabeth"]
        second_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
        cities = ["New York", "Los Angeles", "Washington", "Denver", "Chicago", "Boston", "San Francisco",
                  "Philadelphia", "Seattle", "Portland"]
        streets = ["Bradford Road", "Church Road", "Hill Street", "Wharf Road", "Brown Street", "Pound Lane"]
        order_descriptions = ["Books", "Computers", "Electronics", "Fashion", "Health", "Household", "Music", "Sport",
                              "Tools", "Toys"]
        if item_type == ItemType.FIRST_NAME:
            return first_names[random.randrange(0, len(first_names))]
        elif item_type == ItemType.SECOND_NAME:
            return second_names[random.randrange(0, len(second_names))]
        elif item_type == ItemType.CITY:
            return cities[random.randrange(0, len(cities))]
        elif item_type == ItemType.STREET:
            return streets[random.randrange(0, len(streets))]
        elif item_type == ItemType.ORDER_DESCRIPTION:
            return order_descriptions[random.randrange(0, len(order_descriptions))]
        else:
            return 'NA'
