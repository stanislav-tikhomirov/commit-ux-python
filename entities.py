import random
import time
from typing import Dict, List
from uuid import uuid4, UUID


class AccountManager:
    def __init__(self, first_name: str, last_name: str, department: str):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.department: str = department


class Account:
    def __init__(self, account_id: UUID, first_name: str, last_name: str, account_manager: AccountManager):
        self.account_id: UUID = account_id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.account_manager: AccountManager = account_manager


class Address:
    def __init__(self, country: str, city: str, street: str, building_number: int, apartment_number: int):
        self.country: str = country
        self.city: str = city
        self.street: str = street
        self.building_number: int = building_number
        self.apartment_number: int = apartment_number


class OrderItem:
    def __init__(self, value: int, description: str):
        self.value: int = value
        self.description: str = description


class DeliveryContainer:
    def __init__(self):
        self.orders: Dict[UUID, OrderItem] = {}

    def pack_container(self, order_items: List[OrderItem]):
        for item in order_items:
            self.orders[uuid4()] = item


class DeliveryOrder:
    def __init__(self, containers: List[DeliveryContainer], account, manager, delivery_address):
        self.containers: Dict[UUID, DeliveryContainer] = {}
        for container in containers:
            self.containers[uuid4()] = container
        self.account: Account = account
        self.manager: AccountManager = manager
        self.delivery_address: Address = delivery_address


class Transport:
    def __init__(self):
        self.transport_id: UUID = uuid4()
        self.orders: Dict[UUID, DeliveryOrder] = {}
        self.current_destination: Address = None
        self.destination_time: int = 0
        self.progress_time: int = 0

    def load(self, orders: List[DeliveryOrder]):
        for order in orders:
            self.orders[uuid4()] = order

    def get_progress(self) -> str:
        return "{:.0f}%".format(float(self.progress_time) / float(self.destination_time) * 100)


class TransportJob:
    def __init__(self, transport: Transport):
        self.transport: Transport = transport
        self.is_active: bool = False
        self.current_delivery_id: str = None

    def execute(self):
        if len(self.transport.orders) > 0:
            print(f'Transport {self.transport.transport_id} has departed.')
            self.is_active = True
            for key, order in self.transport.orders.items():
                self.transport.current_destination = order.delivery_address
                self.transport.destination_time = random.randint(10, 100)
                self.transport.progress_time = 0
                self.current_delivery_id = str(key).split('-')[0]
                while self.transport.destination_time - self.transport.progress_time != 0:
                    time.sleep(0.2)
                    self.transport.progress_time += 1
            self.is_active = False
        else:
            print(f'Transport {self.transport.transport_id} is empty.')
