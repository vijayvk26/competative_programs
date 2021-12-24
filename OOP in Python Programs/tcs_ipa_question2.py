"""

Create a class Stock having attributes StockName,StockSector,StockValue.


Create a method getStockList with takes a list of Stock objects and a StockSector(string) and
returns a list containing stocks of the given sector having value more than 500.
"""



class stock:
    def __init__(self,name,sector,value):
        self.name = name
        self.sector = sector
        self.value = value


class show:
    def __init__(self,stock_list):
        self.stock_list = stock_list
    def getStockList(self):
        li = [(i.name,i.value) for i in self.stock_list if i.value>500]
        return li

no = int(input())
stock_li = []
for i in range(no):
    name = input()
    sector = input()
    value = int(input())
    stock_li.append(stock(name,sector,value))

obj = show(stock_li)

res = obj.getStockList()

for i in res:
    print(i[0],i[1])



