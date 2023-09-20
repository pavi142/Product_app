from datetime import datetime
class Product:
    def __init__(self,pid,pnm,prc,pqty,pven,pcat,mnfdate,expdate,discount = 0):
        self.product_id = pid
        self.product_name = pnm
        self.product_price = prc
        self.product_qty = pqty
        self.product_vendor = pven
        self.product_category = pcat
        self.product_mdate = mnfdate
        self.product_edate = expdate
        self.product_discount = discount

    def __str__(self):
        return f'''\n
        Product Name : {self.product_name} 
        Product Price : {self.product_price}
        Product Vendor : {self.product_vendor}
        Product Manf Date : {self.product_mdate.year}-{self.product_mdate.month}-{self.product_mdate.day}
        Product Exp Date : {self.product_edate.year}-{self.product_edate.month}-{self.product_edate.day}'''

    def __repr__(self):
        return str(self)

def product_input():
    pid = int(input('Enter Product Id : '))
    pnm = input('Enter Product Name : ')
    prc = float(input('Enter Product Price : '))
    pqty = int(input('Enter Product Qty : '))
    pven = input('Enter Product Vendor : ')
    pcat = input('Enter Product Category : ')
    discount = input('Enter Discount Percentage : ')
    mnfdate = datetime(year=int(input('Enter Manf Year : ')),
                   month=int(input('Enter Manf Month : ')),
                   day=int(input('Enter Manf Day : ')))
    expdate = datetime(year=int(input('Enter Exp Year : ')),
                   month=int(input('Enter Exp Month : ')),
                   day=int(input('Enter Exp Day : ')))
    return Product(pid,pnm,prc,pqty,pven,pcat,mnfdate,expdate,discount)