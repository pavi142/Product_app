from inventoryservices import InventoryServices
from Productinfo import Product

product_list = []

class Dmart(InventoryServices):

    def add_product(self,prod):
        if type(prod)==Product:
            product_list.append(prod)
            print('Product Successully Added...')
        else:
            print('Invalid Product')


    def delete_product(self,pid):
        for prod in product_list:
            if prod.product_id == pid:
                product_list.remove(prod)
                print("Product Successfully Deleted..")
                break


    def search_product(self,pid):
        for prod in product_list:
            if prod.product_id == pid:
                return prod


    def update_product(self):
        pass


    def product_in_price_range(self,start_price,end_price):
        temp_list = []
        if start_price<=end_price:
            for prod in product_list:
                if prod.product_price>=start_price and prod.product_price<=end_price:
                    temp_list.append(prod)
        else:
            print('Start Price Cannot be Greater Than End Price')
        return temp_list

    def check_for_discounted_price(self):
        pass


    def list_product(self):
        return product_list



