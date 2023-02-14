from db import *

db = DB()
ret = db.customer_add("Testvorname", "Testnachname")
print(ret)
ret = db.getCustomer()
print(ret)
ret = db.getCustomerInfo(1)
print(ret)