from abc import ABC,abstractmethod


class InventoryServices(ABC):            # abstract --> this class is going to hold only -- abstract methods--> methods without body -> just

    @abstractmethod
    def add_product(self):
        pass

    @abstractmethod
    def delete_product(self):
        pass

    @abstractmethod
    def search_product(self):
        pass

    @abstractmethod
    def update_product(self):
        pass

    @abstractmethod
    def check_for_discounted_price(self):
        pass

    @abstractmethod
    def product_in_price_range(self):
        pass


    def m1(self):
        print("normal method --> it's not an abstract method")  # body